# MongoDB

[TOC]

## 1. MongoDB와 NoSQL

* MongoDB는 문서지향(Document-Oriented)적 Cross-platform 데이터베이스
* 확장성과 성능이 뛰어나며, 대표적인 NoSQL Database

### 1) NoSQL?

* NoSQL은 Not Only SQL의 약자로 기존 RDBMS의 한계를 극복하고자 고정된 스키마나 JOIN이 존재하지 않는 데이터베이스의 형태

### 2) 기존 RDBMS와의 차이

| **RDBMS**           | **MongoDB**        |
| ------------------- | ------------------ |
| Database            | Database           |
| Table               | Collection         |
| Tuple / Row         | Document           |
| Column              | Key / Field        |
| Table Join          | Embedded Documents |
| Primary Key         | Primary Key (_id)  |
| Oracle DB, MySQL 등 | MongoDB 등         |

#### Document

* Document는 하나의 의미를 지닌 데이터로 기존 RDBMS에서는 주로 Record, Tuple 등의 형태로 불리는 단위
* 기존 RDMBS와의 가장 큰 차이는 고정된 스키마가 존재하지 않기 때문에 하나의 Collection(Table)에 포함되는 Document(Record)가 서로 다른 데이터를 가지는 것이 가능
* Key-Value pair로 구성(JSON 구조와 유사)

```json
{
    "_id": ObjectId("5bdd4d949b7e8a4674fa3014"),
	"name": "grace",
	"age": 31,
	"address": "seoul"
}
```

#### 기존 RDBMS 대비 장점 및 단점

* 장점
  * 고정된 스키마가 존재하지 않고, Document의 Value로 Document를 사용하는 것이 가능하기 때문에 기존 RDBMS에서 여러개의 Table로 구성하는 데이터를 하나의 Document로 구성하는 것이 가능
  * 고정된 스키마가 존재하지 않기 때문에 어떠한 형태의 데이터라도 쉽게 저장하는 것이 가능하며, JSON 형태를 띄고 있어서 직관적이고 개발이 용이
*  단점
  * RDBMS에 비해 정합성이 떨어져 금용, 결제 등에서는 부적합한 부분이 존재
  * 기존 SQL을 모두 이전할 수 없어서 RDMBS에서 변경 시 별도의 작업이 필요
  * 메모리 관리를 DBMS가 아닌 OS에 위임함에 따라 성능의 차이가 발생
