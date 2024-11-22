import json
from pathlib import Path

from fastavro import writer


# 현재 스크립트 파일의 디렉토리 기준으로 상대 경로 설정
current_dir = Path(__file__).parent  # 현재 스크립트 파일의 디렉토리

schema_name = current_dir / "schemas" / "user_schema.json"
data_file_name = current_dir / "data" / "user_data_2024-11-22.avro"

# 스키마 파일 읽기
with schema_name.open("r") as schema_file:
    schema = json.load(schema_file)

# 데이터 준비
records = [
    {"name": "Alice", "age": 30, "email": "alice@example.com"},
    {"name": "Bob", "age": 25, "email": None},
]

# Avro 파일 작성
with data_file_name.open("wb") as f:
    writer(f, schema, records)

print(f"Avro data file created: {data_file_name}")
