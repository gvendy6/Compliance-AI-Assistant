# src/agent.py

import google.generativeai as genai
from src.config import GEMINI_API_KEY, GEMINI_MODEL
from src.retriever import retrieve


# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)


def ask_agent(question):
    docs = retrieve(question)

    if not docs:
        return "No relevant regulatory text retrieved."

    context = "\n\n".join(
        [f"Source: {doc['source']}\n{doc['text']}" for doc in docs]
    )

    prompt = f"""
You are a Senior US Banking Compliance Officer.

Use ONLY the provided regulatory text.

You must:
- Identify applicable regulation or policy.
- Explain why the regulation applies to the scenario.
- Provide compliance interpretation.
- Assess the action as:
  ✓ Permissible
  ⚠ Risky
  ✖ Likely Non-Compliant
- Explain risk level clearly.
- Cite source filenames.

If no relevant regulatory principle exists, say:
"Not found in provided documents."

Answer in this format:

1. Applicable Regulation
2. Why It Applies
3. Compliance Analysis
4. Risk Assessment (Permissible / Risky / Non-Compliant)
5. Required Controls (if any)
6. Source Citation

REGULATORY TEXT:
{context}

QUESTION:
{question}
"""

    model = genai.GenerativeModel(GEMINI_MODEL)

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.2
        }
    )

    return response.text