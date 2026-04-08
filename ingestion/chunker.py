"""
Document chunking module for the ingestion pipeline.
Splits loaded documents into smaller chunks for vectorization.
"""
import sys
import os

# Add project root to path so we can import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from config import settings

def chunk_documents(documents: list[Document]) -> list[Document]:
    """
    Takes loaded documents and splits them using RecursiveCharacterTextSplitter
    based on the parameters in config/settings.py.
    
    Args:
        documents (list[Document]): List of loaded LangChain Document objects.
        
    Returns:
        list[Document]: List of chunked Document objects with preserved metadata.
    """
    if not documents:
        return []
        
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP,
    )
    
    # split_documents automatically preserves the input metadata into the output chunks.
    chunked_docs = splitter.split_documents(documents)
    
    print(f"Split {len(documents)} document(s) into {len(chunked_docs)} chunk(s).")
    return chunked_docs
