https://suminii.tistory.com/entry/Garbage-In-Garbage-Out-%EB%8B%B9%EC%8B%A0%EC%9D%98-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%AF%BF%EC%9D%84%EB%A7%8C%ED%95%9C%EA%B0%80%EC%9A%94


```sh

1. schema를 정의한다.  # /Users/kyungjunlee/git_project/personal/airflow_lab/src/schemas/user_schema.json 
2. schema registry 내 schema를 등록한다.  # /Users/kyungjunlee/git_project/personal/airflow_lab/src/schemas/register_schema.py
3. curl http://localhost:8085/subjects  # 등록 여부 확인
4. topic 만들기 -> 코드로 자동화 예정(우선 admin 이용)
cf) 토필 만들 때 확인되는 kafka의 log
2024-11-22 18:45:03 [2024-11-22 09:45:03,292] INFO Creating topic user-topic with configuration {cleanup.policy=delete, retention.ms=86400000} and initial partition assignment HashMap(0 -> ArrayBuffer(1)) (kafka.zk.AdminZkClient)
2024-11-22 18:45:03 [2024-11-22 09:45:03,305] INFO [Controller id=1] New topics: [Set(user-topic)], deleted topics: [HashSet()], new partition replica assignment [Set(TopicIdReplicaAssignment(user-topic,Some(r7f3FPi7ToqqjvlLOeZb2g),Map(user-topic-0 -> ReplicaAssignment(replicas=1, addingReplicas=, removingReplicas=))))] (kafka.controller.KafkaController)
2024-11-22 18:45:03 [2024-11-22 09:45:03,305] INFO [Controller id=1] New partition creation callback for user-topic-0 (kafka.controller.KafkaController)  


5. 
```