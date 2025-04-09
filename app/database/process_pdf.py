# import os
# import pickle
# from uuid import uuid4

# import fitz  # This is the proper import for pymupdf
# import faiss
# from langchain.schema import Document
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_community.docstore.in_memory import InMemoryDocstore
# from langchain_community.vectorstores import FAISS

# def process_pdf_to_vector_db(pdf_path, add_to_existing=False):
#     # read the pdf file
#     doc = fitz.open(pdf_path)
    
#     # Extract text from PDF
#     text = ""
#     for page in doc:
#         text += page.get_text()
    
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=200,  # Larger chunk size to keep related information together
#         chunk_overlap=50,  # Increased overlap to maintain context between chunks
#         length_function=len,
#         separators=["\n\n", "\n", ".", "!", "?", ","]
#     )
    
#     # Split text into chunks
#     chunks = text_splitter.split_text(text)
    
#     # Initialize embeddings
#     embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')

#     # Initialize FAISS index
#     index = faiss.IndexFlatL2(len(embeddings.embed_query(chunks[0])))

#     if add_to_existing:
#         vector_store = FAISS.load_local("app/database/vector_store", embeddings, allow_dangerous_deserialization=True)
#     else:
#         # Create vector store
#         vector_store = FAISS(
#             embedding_function=embeddings,
#             index=index,
#             docstore=InMemoryDocstore(),
#             index_to_docstore_id={},
#         )
        
#     # Add documents to vector store
#     for i, chunk in enumerate(chunks):
#         id = str(uuid4())
#         vector_store.add_documents([Document(page_content=chunk, metadata={"source": pdf_path.split("/")[-1], "id": id})], ids=[id])
    
#     # Save the vector store
#     vector_store.save_local("app/database/vector_store")



# if __name__ == "__main__":
#     print("Processing PDFs to vector database...")
#     print("Processing 89b637e633d862c2ac076d27b4104cd3_85f6d305f1.pdf")
#     process_pdf_to_vector_db("assets/89b637e633d862c2ac076d27b4104cd3_85f6d305f1.pdf")
#     print("Processing 81998407_Onderdelenboek_Xtreme_a0bba19ac3.pdf")
#     process_pdf_to_vector_db("assets/81998407_Onderdelenboek_Xtreme_a0bba19ac3.pdf", add_to_existing=False)
#     print("Processing onderdelenlijst.pdf")
#     process_pdf_to_vector_db("assets/onderdelenlijst.pdf", add_to_existing=True)
