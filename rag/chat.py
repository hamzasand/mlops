from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_ollama import ChatOllama

#vector  embbedings model
embedding_model = OllamaEmbeddings(
    model = "qwen3-embedding:0.6b",
)

vector_db = QdrantVectorStore.from_existing_collection(
    embedding = embedding_model,
    url = "http://localhost:6333",
    collection_name = "learning_rag"
)

user_query = input("Ask something")
search_results = vector_db.similarity_search(query=user_query)
context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_results])


SYSTEM_PROMPT = f"""
You are a helpfull AI Assistant who answeres user query based on the available context retrieved from a PDF file along with page_contents and page number.

 You should only ans the user based on the following context and navigate the user to open the right page number to know more.

 Context:
 {context}
"""

# response = ChatOllama(
#     model = "gemma3:1b",
#     messages=[
#         { "role": "system", "content":SYSTEM_PROMPT  },
#         { "role": "user", "content":user_query  },
#     ]
#     ai_msg = llm.invoke(messages)
# )



# print(ai_msg.content)


llm = ChatOllama(
    model="gemma3:1b",
    temperature=0,
)

messages = [
    { "role": "system", "content":SYSTEM_PROMPT  },
        { "role": "user", "content":user_query  }
]
ai_msg = llm.invoke(messages)
ai_msg

print(ai_msg.content)