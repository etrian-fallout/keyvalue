# keyvalue
``python key value storage! ``<br>
[![Build Status](https://travis-ci.org/etrian-fallout/keyvalue.svg?branch=master)](https://travis-ci.org/etrian-fallout/keyvalue)

# Installation

```
pip3 install -r reqirements.txt
```

## function 

| function | 기능 | 인자 |
|---|:---:|---|
| set | 저장 | key, value|
| get | 조회 | key|
| del | 삭제 | key|
| incr | 1 증가 | key|
| ttl | ttl 저장 | key, value, time|

## Running
1. run server
``` sh
cd db
python db_main.py
```

2. run cli
``` sh
cd cli
python cli_req.py
```

## Example
1. run cli
```sh
cd cli
python cli_req.py
```

2. set cnt 
```
set cnt 10
```

3. get cnt
```
get cnt 
```

4. incr cnt
```
incr cnt
```

5. del cnt
```
del cnt
```

6. ttl 
```
ttl time live 10
# 10초후 
get time 
# None
```

## dir
* db: db 서버

* cli: 요청 보내기 & 클라이언트

## TODO 
- value type이 collection인 entry 지원(list, hashmap 등) 많을수록 좋음 (easy)
- entry에 TTL 지원 (medium)
- primitive key-value entry에 대해 concurrent operation 지원 (test and set) (medium)
- persistent 지원 (medium)
- multithreaded 모델로 변경 시도 (redis는 싱글 스레드), 같은 키에 대해서는 serializability 지원 (medium~hard)
- distributed로 확장, fail-over 고려 (hard)
