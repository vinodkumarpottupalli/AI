"""Document processing script using AI model."""
import os
import base64
from client import create_ai_client


def encode_file_to_base64(file_path):
    """Encodes a file to a base64 string."""
    with open(file_path, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode("utf-8")
    return encoded_string


def process_document(client, file_path):
    """Processes a document using the specified AI model."""

    encoded_file = encode_file_to_base64(file_path)

    response = client.chat.completions.create(
        model=os.getenv("MODEL", "gemini-2.5-flash"),
        temperature=0.2,
        messages=[
            {
                "role": "system",
                "content": "Analyse the business report and extract:"
                "1. key performance metrix"
                "2. Main challenges mentioned"
                "3. Growth opprtunities indetified"
                "4. Overall business health assessment",
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url":{
                            "url": f"data:text/plain;base64,{encoded_file}"
                        }
                    }
                ]
            }
        ],
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    if os.path.exists("scripts\\sample_report.txt"):
        client = create_ai_client()
        result = process_document(client, "scripts\\sample_report.txt")
        print("Processing Result:", result)
