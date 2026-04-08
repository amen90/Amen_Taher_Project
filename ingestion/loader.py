"""
File loader module for the ingestion pipeline.
Routes files to the appropriate LangChain loaders based on extension.
"""
import os
from langchain_community.document_loaders import PyPDFLoader, UnstructuredFileLoader
from langchain_core.documents import Document

def load_document(file_path: str) -> list[Document]:
    """
    Accepts a file path, detects the extension, and routes it to the correct LangChain loader.
    
    Args:
        file_path (str): The path to the file to load.
        
    Returns:
        list[Document]: A list of LangChain Document objects.
        
    Raises:
        ValueError: If the file type is unsupported.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
        
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == '.pdf':
        print(f"Loading PDF: {file_path}")
        loader = PyPDFLoader(file_path)
        return loader.load()
    elif ext in ['.docx', '.pptx', '.txt']:
        print(f"Loading {ext.upper()} using Unstructured: {file_path}")
        loader = UnstructuredFileLoader(file_path)
        return loader.load()
    else:
        raise ValueError(f"Unsupported file extension: {ext}. Supported types are .pdf, .docx, .pptx, .txt")
