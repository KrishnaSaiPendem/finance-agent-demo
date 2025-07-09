# finance-agent-demo
Autonomous Personal Finance Agent with Kafka, Chroma, and Streamlit

# Autonomous Personal Finance Agent

An end-to-end, local demo of an **agentic AI**–powered personal finance assistant using mock data. No paid services required.

## Features

- **Transaction ingestion** (CSV → Kafka)
- **Vector indexing** of transaction descriptions (Chroma + Sentence-Transformers)
- **Retrieval-Augmented Generation** (RAG) via local LLaMA model
- **Agentic ReAct loop** for question answering
- **Demo UI** with Streamlit

## 🛠 Tech Stack

- **Kafka** (via Docker Compose)
- **Chroma** vector database
- **Sentence-Transformers** for embeddings
- **Llama CPP** for local LLM inference
- **FastAPI** for serving the agent
- **Streamlit** for interactive demo
- **Docker** for environment consistency

## Setup Guide

1. **Clone & install dependencies**  
   ```bash
   git clone https://github.com/yourusername/finance-agent-demo.git
   cd finance-agent-demo
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
