from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
loader=PyPDFLoader("sample_employee.pdf")
documents=loader.load()
splitter=RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=200
)
chunks=splitter.split_documents(documents)
print(len(chunks))
embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vector_store=FAISS.from_documents(
    chunks,embeddings
)
print("vector store created")
retriever=vector_store.as_retriever()
question=input("what is question:")
docs=retriever.invoke(question)
print(docs[0].page_content)