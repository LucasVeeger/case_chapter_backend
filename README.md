# Parts Catalog AI Assistant

This AI-powered application helps users search through parts catalogs using natural language queries. It processes PDF catalogs into a vector database and provides intelligent responses based on the catalog contents.

## Features

- PDF catalog processing with text chunking
- Vector similarity search using FAISS
- Conversational AI interface using OpenAI's GPT models
- FastAPI backend for quick and efficient responses
- Support for conversation history and context

## Setup

1. Clone the repository
2. Create a virtual environment and activate it
3. Install the dependencies
4. Run the application with `uvicorn app.main:app --reload`

## Vector Database preprocessing

0. Put the PDF catalogs in the `app/assets/` folder and add file in the process_pdf.py file's main
1. Run `python app/database/process_pdf.py` to process the PDF catalogs into a vector database
2. Run `python app/database/search.py` to test search the vector database

## Usage

1. Start the application
2. Interact with the AI assistant through the API chat endpoint


