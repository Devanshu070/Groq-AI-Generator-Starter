import streamlit as st
import requests
import os
from groq import Groq

# Load API key (store securely in environment variables)
GROQCLOUD_API_KEY = os.getenv("GROQ_API_KEY")  # Set this in your terminal or .env file

# Initialize Groq client
client = Groq(api_key=GROQCLOUD_API_KEY)

# Set up the Streamlit app
st.title("AI Text Generation with Streamlit")



# User input for text prompt
prompt = st.text_input("Enter a prompt:", "Once upon a time")

if st.button("Generate Response"):
    if not GROQCLOUD_API_KEY:
        st.error("API key is missing! Please set the GROQCLOUD_API_KEY environment variable.")
    else:
        with st.spinner("Generating response..."):
            try:
                response = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    model="llama-3.3-70b-versatile",
                    temperature=0.7,
                    max_completion_tokens=150
                )
                st.subheader("AI Response:")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {e}")