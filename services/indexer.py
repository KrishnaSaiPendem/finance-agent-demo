import json
from kafka import KafkaConsumer
from sentence_transformers import SentenceTransformer
import chromadb

consumer = KafkaConsumer(
    "transactions",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode())
)

embedder = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client()
collection = client.create_collection("transactions")

for msg in consumer:
    tx = msg.value
    text = f"{tx['merchant']} ({tx['category']}): ${tx['amount']}"
    emb = embedder.encode(text).tolist()
    collection.add(
        ids=[f"{tx['user_id']}_{tx['date']}_{tx['merchant']}"],
        embeddings=[emb],
        metadatas=[tx],
        documents=[text]
    )
    print("Indexed:", text)
