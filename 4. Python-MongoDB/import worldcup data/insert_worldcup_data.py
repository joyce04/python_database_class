import sys
import pandas as pd
import numpy as np
from pymongo import MongoClient

def get_client(murl, id, pw):
    url = ''
    if murl != 'localhost':
        url = 'mongodb://%s:%s@cluster0-shard-00-00-%s:27017,cluster0-shard-00-01-%s:27017,cluster0-shard-00-02-%s:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true' % (id,pw, murl, murl, murl)
    else:
        url = murl
    port = 27017
    return MongoClient(url, port)

def insert_data(murl, id, pw):
    wc_match = pd.read_csv('./wc_match.tsv', sep='\t')
    team = pd.read_csv('./team.tsv', sep='\t')
    players = pd.read_csv('./players.tsv', sep='\t')

    players.stat_value = players.stat_value.apply(lambda x: pd.to_numeric(x.replace('%', '')) / 100 if '%' in x \
                                                else pd.to_numeric(x.replace(',', '')) if ',' in x \
                                                else pd.to_numeric(x.split('\'')[0]) * 60 + pd.to_numeric(x.split('\'')[1].split('\"')[0]) if '\'' in x \
                                                else pd.to_numeric(x.replace('\"', '')) if '\"' in x \
                                                else pd.to_numeric(x) if ord(x[0]) < 60\
                                                else x)

    documents = []
    for match in wc_match.iterrows():
        document = {}
        home_players = list((v.dropna().to_dict()) for k, v in players[(players.match_id == match[1]['id']) & (players.team_id == match[1]['home_team_id']) & (players.half == 'total') & \
            (~players.stat_type.isin(['POS', 'SUB', 'DZONE1', 'DZONE2', 'DZONE3', 'DZONE4', 'DZONE5', 'TZONE1', 'TZONE2', 'TZONE3', 'TZONE4', 'TZONE5']))]\
    .pivot_table(values='stat_value', index=['num', 'name', 'club', 'position'], columns='stat_type', aggfunc='first')\
    .reset_index().iterrows())
        away_players = list((v.dropna().to_dict()) for k, v in players[(players.match_id == match[1]['id']) & (players.team_id == match[1]['away_team_id']) & (players.half == 'total') & \
            (~players.stat_type.isin(['POS', 'SUB', 'DZONE1', 'DZONE2', 'DZONE3', 'DZONE4', 'DZONE5', 'TZONE1', 'TZONE2', 'TZONE3', 'TZONE4', 'TZONE5']))]\
    .pivot_table(values='stat_value', index=['num', 'name', 'club', 'position'], columns='stat_type', aggfunc='first')\
    .reset_index().iterrows())
        
        document['date'] = match[1]['match_date']    
        document['home_team'] = {
            'country': team[team.id == match[1]['home_team_id']].country.values[0], 
            'score': match[1]['home_team_score'],
            'players': home_players
        }
        document['away_team'] = {
            'country': team[team.id == match[1]['away_team_id']].country.values[0], 
            'score': match[1]['away_team_score'],
            'players': away_players
        }
        documents.append(document)

    client = get_client(murl, id, pw)

    client.Football.wc_match.remove()
    client.Football.wc_match.insert_many(documents)
    print(client.Football.wc_match.count())

if len(sys.argv) == 1:          # 옵션 없으면 도움말 출력하고 종료
    print("Insert your mongodb database url and id, pass")
    exit(1)
elif len(sys.argv) < 4:
    print("Insert your mongodb database url and id, pass")
    exit(1)

insert_data(sys.argv[1].replace('cluster0-', ''), sys.argv[2], sys.argv[3])