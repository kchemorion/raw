# initialize_embeddings.py

import requests
import json

# Define the NVIDIA API key and endpoint
api_key = "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"  # Replace with your actual NVIDIA API key
base_url = "https://ai.api.nvidia.com/v1/retrieval/nvidia/embeddings"

# Function to create embeddings
def create_embeddings(text, model="NV-Embed-QA"):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    payload = {
        "input": text,
        "model": model,
        "input_type": "query",  # Set to "query" or "passage" based on the example
        "encoding_format": "float",
        "truncate": "NONE",
        "user": "string"  # This can be any string, representing the user
    }
    # Print the request URL and payload for debugging
    print(f"Request URL: {base_url}")
    print(f"Payload: {json.dumps(payload, indent=2)}")

    response = requests.post(base_url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()['data'][0]['embedding']
    else:
        raise Exception(f"Request failed: {response.status_code}\n{response.text}")

# Function to test embedding initialization
def test_embeddings():
    text = "This is a test text for embeddings."
    embeddings = create_embeddings(text)
    print(embeddings)

if __name__ == "__main__":
    test_embeddings()
