import csv
import time
import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode()
)

with open("data/transactions.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["amount"] = float(row["amount"])
        producer.send("transactions", row)
        print("Produced:", row)
        time.sleep(0.01)
