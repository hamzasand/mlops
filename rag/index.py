from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore

pdf_path = "C:\\Users\\92324\\Desktop\\mlops\\mlops\\rag\\nodejs.pdf"

# load documents
loader = PyPDFLoader(file_path = pdf_path)
docs = loader.load()

#make chunking 
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=100)
chunks = text_splitter.split_documents(documents=docs)

#vector  embbedings model
embedding_model = OllamaEmbeddings(
    model = "qwen3-embedding:0.6b",
)

# store vector embeddings in vector db
vector_store = QdrantVectorStore.from_documents(
    documents = chunks,
    embedding = embedding_model,
    url = "http://localhost:6333",
    collection_name = "learning_rag"
)

print("Indexing of docuemnts is done ......")

