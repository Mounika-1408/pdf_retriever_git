# PDF Retriever

## Overview
PDF Retriever is a simple document retrieval application built using LangChain and FAISS. It loads a PDF document, splits it into chunks, creates embeddings, stores them in a FAISS vector database, and retrieves the most relevant text based on the user's query.

## Features
- Load PDF documents
- Split text into chunks
- Generate embeddings
- Store embeddings using FAISS
- Retrieve relevant document content based on user queries

## Technologies Used
- Python
- LangChain
- FAISS
- HuggingFace Embeddings
- PyPDFLoader

## Project Structure

pdf_retriever/
├── pdf_retriever.py
├── sample_employee.pdf
├── requirements.txt
├── README.md
└── .gitignore


## Installation


pip install -r requirements.txt


## Run


python pdf_retriever.py


## Example Questions
- What is the employee name?
- What is the employee designation?
- What is the salary?
- What is the joining date?
