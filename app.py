import streamlit as st
from openai import OpenAI

# Access the secret API key stored in Streamlit Cloud
api_key = st.secrets["OPENAI_API_KEY"]

# Pass the API key when creating the OpenAI client
client = OpenAI(api_key=api_key)

st.title("Simple Query with OpenAI")
user_content = st.text_area("Enter your message here", "Hello, what would you like me to do?")
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_content}
    ]
)

st.write(completion.choices[0].message.content)
