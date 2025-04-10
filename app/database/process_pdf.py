# import os
# import pickle
# from uuid import uuid4

# import pdfplumber
# import fitz  # This is the proper import for pymupdf
# import faiss
# from langchain.schema import Document
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_community.docstore.in_memory import InMemoryDocstore
# from langchain_community.vectorstores import FAISS
# import re

# def process_pdf_to_vector_db(pdf_path, add_to_existing=False):
#     # read the pdf file
#     all_rows = []
#     with pdfplumber.open(pdf_path) as pdf:
#         print(len(pdf.pages))
#         for page in pdf.pages:
#             if page.page_number < 400 or page.page_number > 600:
#                 continue
#             table = page.extract_table()
#             if table:
#                 print('new table')
#                 print(page.page_number)
#                 print('length of table: ', len(table))
#                 column_names = table[0]
#                 data_rows = table[1:]
#                 for row in data_rows:
#                     row_with_headers = dict(zip(column_names, row))
#                     all_rows.append(row_with_headers)


#     chunks = []
#     for row in all_rows:
#         # Convert dictionary items to "column:value" format and join with commas
#         chunk_group = []
        
#         row_text = ",".join(f"{key if isinstance(key, str) else 'unknown_value_type'}:{value if isinstance(value, str) else ''}" for key, value in row.items())
#         chunk_group.append(row_text)
#         if row_text != "":
#             for key, value in row.items():
#                 chunk_group.append(f"{key}:{value}")
#             chunks.append(chunk_group)
        

#     # Initialize embeddings
#     embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')

#     # Initialize FAISS index
#     index = faiss.IndexFlatL2(len(embeddings.embed_query(chunks[0][0])))

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
#         group_id = str(uuid4())
#         whole_chunk_metadata = chunk[0] # this is the metadata for the whole chunk
#         for c in chunk[1:]:
#             document_id = str(uuid4())
#             vector_store.add_documents([Document(page_content=c, metadata={"source": pdf_path.split("/")[-1], "group_id": group_id, 'group_content': whole_chunk_metadata})], ids=[document_id])
    
#     # Save the vector store
#     vector_store.save_local("app/database/vector_store")



# if __name__ == "__main__":
#     print("Processing PDFs to vector database...")
#     # print("Processing 89b637e633d862c2ac076d27b4104cd3_85f6d305f1.pdf")
#     # process_pdf_to_vector_db("assets/89b637e633d862c2ac076d27b4104cd3_85f6d305f1.pdf", add_to_existing=False)
#     # print("Processing onderdelenlijst.pdf")
#     # process_pdf_to_vector_db("assets/onderdelenlijst.pdf", add_to_existing=True)
#     # print("Processing 81998407_Onderdelenboek_Xtreme_a0bba19ac3.pdf")
#     # process_pdf_to_vector_db("assets/81998407_Onderdelenboek_Xtreme_a0bba19ac3.pdf", add_to_existing=True)

