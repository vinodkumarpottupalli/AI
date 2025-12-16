"""
AI interaction example using Gemini model for basic text completion.
"""

from client import create_ai_client


def ask_simple_question(client, question: str):
    """
    Ask a simple question to the AI model and print the response.
    """

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": question
            }
        ],
        top_p=1,      # Use full vocabulary
        temperature=0.2  # Low creativity
    )

    ai_response = response.choices[0].message.content

    print("_" * 50)
    print("AI Response:", ai_response)
    print("-" * 50)

    return ai_response

def ask_multiple_questions(client):
    """
    Ask multiple questions to the AI model and print the responses.
    """
    questions =[
        "How do large language models work?",
        "What is the word reprasentation technique used in NLP?"
    ]

    for question in questions:
        ask_simple_question(client, question)


if __name__ == "__main__":
    ai_client = create_ai_client()
    ask_multiple_questions(ai_client)
