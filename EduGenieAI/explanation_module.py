from gemini_client import generate_text


def explain_concept(topic: str) -> str:
    prompt = f"""
Explain the following concept clearly for a college student:

{topic}

Give a simple, student-friendly explanation with important points and a short example when useful.
""".strip()

    return generate_text(
        prompt,
        system_instruction=(
            "You are a patient teacher. "
            "Prefer concise, student-friendly explanations."
        ),
        temperature=0.25,
        max_output_tokens=1000,
    )