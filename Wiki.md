# Zero-Cost Enterprise AI Knowledge Agent - Wiki

## 1. Project Overview & Constraints
**Goal:** Build a Proof of Concept (PoC) for a Retrieval-Augmented Generation (RAG) system to process 4,000+ internal documents.
**Constraints:** Strict zero-cost overhead using entirely free-tier or open-source solutions. 
**Target:** A functional chat interface MVP to secure future budget.

## 2. Current State & Progress
* **Phase 1 (Ingestion):** In Progress
  * [x] Initialize Wiki & memory protocol
  * [x] Environment setup (requirements, gitignore, env templates, config)
  * [x] Ingestion scripts (loader, chunker)
  * [x] Create public README.md for GitHub
  * [ ] Run `pip install` and configure `.env`
  * [ ] Data audit and raw document collection
  * [ ] Implement OCR pipeline
* **Phase 2 (Indexing):** Pending
* **Phase 3 (RAG Engine):** Pending
* **Phase 4 (UI & Hand-over):** Pending

## 3. Architecture & Tech Stack
* **Ingestion:** Python, LangChain (`PyPDFLoader`, `Unstructured`)
* **Embeddings:** HuggingFace `sentence-transformers/all-MiniLM-L6-v2` (Local)
* **Vector DB:** MongoDB Atlas (Free Tier / M0 cluster)
* **LLM Orchestration:** LangChain
* **Inference:** Gemini 1.5 Flash (Google AI Studio Free Tier API)
* **UI/Hosting:** Streamlit on GCP Always-Free Tier (e2-micro)

## 4. Directory Structure
```text
Taher-Amen-project/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── Wiki.md
├── config/
│   └── settings.py
└── ingestion/
    ├── chunker.py
    └── loader.py
```

## 5. Configuration Details
* **Chunk Size:** 512 tokens
* **Chunk Overlap:** 50 tokens
* **Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2`

## 6. Module Relationships
* `ingestion.loader`: Detects file type and returns raw documents using appropriate LangChain loaders.
* `ingestion.chunker`: Takes loaded documents from `loader.py` and processes them into standardized chunks based on `config.settings`, preserving metadata.
