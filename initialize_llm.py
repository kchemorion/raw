# initialize_llm.py

from openai import OpenAI

# Initialize the OpenAI client with NVIDIA API key
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"  # Replace with your actual NVIDIA API key
)

# Function to test LLM initialization
def test_llm():
    completion = client.chat.completions.create(
        model="mistralai/mixtral-8x7b-instruct-v0.1",
        messages=[{"role": "user", "content": "Write a ballad about LangChain."}],
        temperature=0.5,
        top_p=1,
        max_tokens=1024,
        stream=False
    )

    # Print the generated content
    for choice in completion.choices:
        if hasattr(choice.message, 'content'):
            print(choice.message.content, end="")

if __name__ == "__main__":
    test_llm()
