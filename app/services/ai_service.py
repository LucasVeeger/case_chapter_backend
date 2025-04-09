from openai import OpenAI
import os
from dotenv import load_dotenv
from app.database.search import similarity_search

load_dotenv()

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY")
)

def chat_with_history(new_message, previous_messages=None):
    # Clean the question first
    clean_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": "Extract only the essential search terms from the user's question. Remove conversational elements and keep only what's needed for a vector search. In case of a product code, respond with the product code, nothing else. Respond with only the search terms, nothing else."
        }, {
            "role": "user",
            "content": new_message.content
        }]
    )
    cleaned_query = clean_response.choices[0].message.content
    print(f"Cleaned query: {cleaned_query}")
    # search with cleaned message in the database
    search_results = similarity_search(cleaned_query)
    search_results_str = "\n\n".join([
        f"Result: {res.page_content} [{res.metadata}]" 
        for i, res in enumerate(search_results)
    ])
    
    if previous_messages is None:
        previous_messages = []
    
    # Define system instructions for the AI
    system_message = {
        "role": "system",
        "content": """You are a helpful AI assistant. Use the following search results to inform your responses:

{search_results_str}

Pick relevant information from the search results to answer the user's question that follows. For each reference to a search result, include the source file name from the metadata in your response.
If the user's question is not answered by the search results, make up an answer based on your knowledge.
Keep responses focused and relevant.""".format(search_results_str=search_results_str)
    }
    
    # Construct the message list
    messages = [system_message]
    if previous_messages:
        messages.extend(previous_messages)  # Add previous conversation turns
    
    # Add the new user message
    messages.append({
        "role": "user",
        "content": new_message.content
    })
    
    print(messages)
    response = client.responses.create(
        model="gpt-4o-mini",  # or "gpt-3.5-turbo"
        input=messages  # Changed from 'input' to 'messages'
    )
    print(response)
    

    return response.output_text



if __name__ == "__main__":
    print(chat_with_history("Tell me about the article number 203207"))