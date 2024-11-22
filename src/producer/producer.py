from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
from pathlib import Path
import json

# Kafka 및 Schema Registry 설정
KAFKA_BOOTSTRAP_SERVERS = "localhost:29092"
SCHEMA_REGISTRY_URL = "http://localhost:8085"
TOPIC_NAME = "user-topic"

# 스키마 파일 경로
schema_file = Path(__file__).parent.parent / "schemas" / "user_schema.json"

# 스키마 로드
with schema_file.open("r") as f:
    value_schema = avro.loads(json.dumps(json.load(f)))

# AvroProducer 설정
producer_config = {
    "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
    "schema.registry.url": SCHEMA_REGISTRY_URL,
}
producer = AvroProducer(producer_config, default_value_schema=value_schema)


# 메시지 전송 함수
def send_message(record):
    try:
        producer.produce(topic=TOPIC_NAME, value=record)
        producer.flush()
        print(f"Message sent to topic '{TOPIC_NAME}': {record}")
    except Exception as e:
        print(f"Failed to send message: {e}")


test_record = {"name": "Alice", "age": 30, "email": "alice@example.com"}
send_message(test_record)
