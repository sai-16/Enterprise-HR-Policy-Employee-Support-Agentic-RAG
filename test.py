# from app.core.config import get_settings

# settings = get_settings()

# print(f"App Name : {settings.app_name}")
# print(settings.pinecone_index_name)

from app.services.ingestion import load_file, chunk_documents
from pathlib import Path


docs = load_file(Path("data/sample_kb/company_hr_handbook.md"))
chunked_docs = chunk_documents(docs)

print(len(chunked_docs))