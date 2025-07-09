from sentence_transformers import SentenceTransformer
import chromadb

embedder = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client()
col = client.get_collection("transactions")

def retrieve_transactions(query: str, k: int = 5):
    q_emb = embedder.encode(query).tolist()
    results = col.query(query_embeddings=[q_emb], n_results=k)
    return results["metadatas"][0]

def react_agent(user_id: str, user_query: str) -> str:
    txns = retrieve_transactions(user_query)
    total = sum(t["amount"] for t in txns if t["user_id"] == user_id)
    return f"You spent ${total:.2f} on \"{user_query}\"."

if __name__ == "__main__":
    print(react_agent("u1", "dining"))
