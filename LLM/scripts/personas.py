"""Generate responses using different system prompts to simulate various personas."""

from client import create_ai_client


def demonstrate_system_prompts(client):
    """Generate responses using different system prompts."""
    user_question = "How AI will impact the future of work?"

    personas = {
        "Business Consultant": { 
            "system": "You are a senior busniess consultant with 20 years of experiance"
                "helping companies to implement technology solutions. you speak in a professional, strategic manner and"
                "and always focus on ROI and business value."
        },
        "Friendly Teacher": {
            "system": "You are a friendly and patient teacher who explains complex topics in simple terms."
                "You use relatable examples and encourage curiosity and learning."
        }
    }

    for persona_name, prompts in personas.items():
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[
                {"role": "system", "content": prompts["system"]},
                {"role": "user", "content": user_question}
            ],
            temperature=0.1
        )
        print(f"--- {persona_name} Response ---")
        print(response.choices[0].message.content)
        print("" + "-" * 100)


if __name__ == "__main__":
    ai_client = create_ai_client()
    demonstrate_system_prompts(ai_client)
