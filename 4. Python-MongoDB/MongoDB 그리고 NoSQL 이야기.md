# MongoDB 그리고 NoSQL 이야기

## NoSQL

* 1998년 카를로스 스토리치가 표준 SQL 인터페이스를 사용하지 않는 자신의 오픈소스 RDBMS를 NoSQL이라고 명명
* 2009년 요한 오스칼손이 오픈소스 세미나에서 NoSQL이라는 용어를 기존 RDBMS의 주요 특징인 ACID(Atomic, Consistency, Integrity, Duarabity)를 제공하지 않지만 확장성과 성능의 특성을 갖는 데이터베이스의 의미로 사용하면서 대중화가 시작
* Key-Value DB(Riak, Vodemont 등), Wide Columnar DB(Google의 BigTable에서 유래, HBase, Cassandra 등), Document DB(Mongo DB가 대표적), Graph DB(Neo4J가 유명) 등의 종류가 존재

## Why NoSQL?

* 기존 RDBMS 의 경우 대용량의 데이터 처리에 있어서 속도의 이슈가 늘 존재
* Scheme기반의 동작(Table의 구조가 정해져있음)
* 실제 객체와 DB의 Scheme가 서로 상이
  * 객체: 이름, 나이, 학번, 수강과목들, 과목별 담당교수, 과목별 학점들 ....
  * RDB: 학생(이름, 나이, 학번), 수업(과목명, 담당교수), 학점(과목명, 학번, 학점) ....
  * 학생이란 객체를 표현하기 위해 여러개의 Table이 존재
* 이런 RDBMS의 단점을 보완하고 집합 지향하기 위해 Key-Value, Document 등의 개념 등장
  * 학생 A의 Document에는 Key-Value를 이용하여 학생의 모든 정보가 저장(Table Join 불필요)
* 성능적인 이슈 해결을 위한 샤딩(데이터를 여러 노드에 분산 저장), Scale-out(하드웨어를 업그레이드 하는 것이 아니라 갯수를 늘리는 확장 정책), 리플리카(모든 데이터를 복제하여 보관) 등을 이용한 고가용성(High Availability, HA)를 구현하고자 노력

## But...

* NoSQL의 쿼리 문법은 복잡하고, 기존 RDBMS에 익숙한 개발자 및 DBA 들에게는 매우 불편함을 야기
* 대용량 데이터의 Insert 시 사실상 데이터베이스가 정지
  * 대부분의 RDBMS가 Row 단위의 Lock을 사용하지만, Mongo DB 등 많은 NoSQL의 DB 단위의 Lock을 사용
  * 또한, Write Lock과 Read Lock 중 Write Lock이 우선시되면서 Write 중에는 Read가 Queue에 대기
  * 즉, 많은 양의 데이터를 한번에 Insert 하면 해당 Insert가 종료되기 전까지 DB 접근이 불가능
* MongoDB와 같은 Document DB의 경우 데이터 구조가 복잡해 질 수록 Nested Document가 계속 생성
  * 전체적인 구조를 파악하기가 여려워지고,
  * Join이 존재하지 않는 NoSQL의 특성 상 Nested Document의 속성을 Grouping 하기 어렵고,
  * Document size가 계속 늘어나게 되면 결국 성능적 이슈가 발생하게 되어,
  * MongoDB의 Document를 기존 RDBMS의 1:N 을 표현하는 것처럼 분리하게 됨으로써,
  * NoSQL이 가지는 특징을 포기하게 됨

 ## In the end...

* 기존 RDBMS를 NoSQL로 대체하는 것은 매우 신중하게 결정할 필요가 있음
* 특정 서비스에 있어서는 NoSQL이 장점을 가질 수 있으나 아직까지는 RDBMS를 대체하기 어려움
* 메시징 서비스(메신저 등), IoT 센서 데이터, 주기적으로 스키마가 변경되는 데이터, 정규화 시 2개 정도의 Table이 나오는 매우 간단한 구조의 Database 구축 등에서 활용도가 높아보이나 그 외에는 그다지....
* Scale-out 및 분산처리라는 장점을 극대화 할 수 있는 사용처가 필요

## References

* https://www.slideshare.net/WonchangSong1/no-sqlsimpleintro

* http://eincs.com/2012/06/nosql-is-not-useful/

* http://jwprogramming.tistory.com/70

* http://bigmatch.i-um.net/2013/12/09/mongodb를-쓰면서-알게-된-것들/