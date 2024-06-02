# api_rag.py

from ncbi_data import search_ncbi, fetch_ncbi_data
from initialize_llm import client
from vector_store import create_vector_store
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Define a function to retrieve and process data from NCBI
def retrieve_ncbi_data(query, database="pubmed"):
    ids = search_ncbi(query, database)
    data = fetch_ncbi_data(ids, database)
    return data

# Example function call configuration
function_calls = {
    "retrieve_ncbi_data": {
        "function": retrieve_ncbi_data,
        "params": {"query": "{query}", "database": "pubmed"}
    }
}

# Define the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer solely based on the following context:\n<Documents>\n{context}\n</Documents>"),
    ("user", "{question}"),
])

# Example query and data retrieval
user_query = "What is known about the BRCA1 gene?"
user_context = {"query": "BRCA1", "database": "pubmed"}

# Process the function call to get data
retrieved_data = function_calls["retrieve_ncbi_data"]["function"](
    function_calls["retrieve_ncbi_data"]["params"]
)
documents = [str(record) for record in retrieved_data]

# Update the vector store with the retrieved documents
store = create_vector_store(documents)
retriever = store.as_retriever()

# Create and execute the chain
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | client.chat.completions.create(
        model="mistralai/mixtral-8x7b-instruct-v0.1",
        messages=[{"role": "user", "content": "{question}"}],
        temperature=0.5,
        top_p=1,
        max_tokens=1024,
        stream=False
    )
    | StrOutputParser()
)

result = chain.invoke(user_query)
print(result)
