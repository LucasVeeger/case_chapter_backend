from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def similarity_search(query: str, k: int = 5, filter_dict: dict = None) -> list:
    """
    Perform similarity search on the vector store with optional filtering.
    
    Args:
        query (str): The search query text
        k (int): Number of results to return (default: 2)
        filter_dict (dict): Optional filter criteria (default: None)
        
    Returns:
        list: List of search results with content and metadata
    """
    try:
        # Load the vector store from disk
        embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
        vector_store = FAISS.load_local("app/database/vector_store", embeddings, allow_dangerous_deserialization=True)
        
        results = vector_store.similarity_search(
            query,
            k=k,
            filter=filter_dict
        )
        
        return results
        
    except Exception as e:
        print(f"Error performing similarity search: {str(e)}")
        return []

if __name__ == "__main__":
    results = similarity_search("7773663", k=5)
    for res in results:
        print(f"* {res.page_content} [{res.metadata}]")
