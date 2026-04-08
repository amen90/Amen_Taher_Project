# Zero-Cost Enterprise AI Knowledge Agent

This repository hosts a Proof of Concept (PoC) for an Enterprise Retrieval-Augmented Generation (RAG) system capable of processing 4,000+ internal documents.

**Key Highlight:** The entire architecture is built under a **strict zero-cost constraint**, relying exclusively on free-tier cloud services and open-source models running locally.

## Architecture

* **Ingestion:** Python & LangChain (`PyPDFLoader`, `Unstructured`, `Tesseract`)
* **Embeddings:** HuggingFace `sentence-transformers/all-MiniLM-L6-v2` (Local Execution)
* **Vector Database:** MongoDB Atlas (M0 Free Tier Cluster)
* **Orchestration:** LangChain
* **LLM Inference:** Gemini 1.5 Flash (via Google AI Studio Free Tier API)
* **Hosting & UI:** Streamlit deployed on Google Cloud Platform (e2-micro Always-Free Tier)

## Setup Instructions

### Prerequisites
* Python 3.11+
* MongoDB Atlas Account (Free Tier)
* Google AI Studio API Key

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Taher-Amen-project
   ```

2. **Setup virtual environment:**
   ```bash
   python -m venv .venv
   # On MacOS/Linux:
   source .venv/bin/activate
   # On Windows:
   .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   * Copy the example `.env` template:
     ```bash
     cp .env.example .env
     ```
   * Edit `.env` to include your actual `MONGO_URI` and `GEMINI_API_KEY`.

## Project Structure
- `config/` - Centralized settings (e.g., chunk size, embedding model)
- `ingestion/` - Document loading and chunking scripts
- `rag/` - Core RAG logic, chain configuration, and retriever setups
- `app/` - Streamlit application
- `data/raw/` - Raw document storage (git-ignored)

*Note: For detailed active state tracking during development, see our local root `Wiki.md` file (which is git-ignored).*

## Contributors
* AmenAllah Brahem
* Mohamed Taher Jouida
