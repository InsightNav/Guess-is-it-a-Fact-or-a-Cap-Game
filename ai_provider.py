import os

provider = os.getenv("AI_PROVIDER", "gemini")  # change this in .env


def use_gemini(prompt):
    from google import genai
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    res = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return res.text


def use_openai(prompt):
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content


def use_claude(prompt):
    import anthropic
    client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))

    res = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}]
    )
    return res.content[0].text


def generate(prompt):
    if provider == "gemini":
        return use_gemini(prompt)
    elif provider == "openai":
        return use_openai(prompt)
    elif provider == "claude":
        return use_claude(prompt)
    else:
        raise ValueError("unknown provider")