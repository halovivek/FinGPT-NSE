from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings()

db = Chroma(
    persist_directory="../data/vector_db",
    embedding_function=embedding
)

def retrieve_context(query):

    docs = db.similarity_search(query, k=3)

    context = "\n".join([d.page_content for d in docs])

    return context
