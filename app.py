from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

st.title("Simple Query with OpenAI")
user_content = st.text_area("Enter your message here", "Hello, what would you like me to do?")
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": user_content
        }
    ]
)

st.write(completion.choices[0].message.content)