import json
import requests
from pathlib import Path

# Schema Registry URL
SCHEMA_REGISTRY_URL = "http://localhost:8085"

# 스키마 파일 경로
schema_file = Path(__file__).parent / "user_schema.json"

# 토픽과 스키마 주제 설정
TOPIC_NAME = "user-topic"
SUBJECT_NAME = f"{TOPIC_NAME}-value"

# 스키마 읽기
with schema_file.open("r") as f:
    schema = json.load(f)

# 스키마 등록 요청
response = requests.post(
    f"{SCHEMA_REGISTRY_URL}/subjects/{SUBJECT_NAME}/versions",
    headers={"Content-Type": "application/vnd.schemaregistry.v1+json"},
    data=json.dumps({"schema": json.dumps(schema)}),
)

# 응답 처리
if response.status_code == 200:
    print(f"Schema registered successfully for subject '{SUBJECT_NAME}':", response.json())
else:
    print("Failed to register schema:", response.text)
