import streamlit as st
import openai

# Initialize the GPT-3 API client using the secret key stored in Streamlit secrets
openai.api_key = st.secrets["openai_api_key"]

st.title("ChatGPT Clone Web App")

# Create a text input field for user messages
user_input = st.text_input("You:", "")

if user_input:
    # Send user input to the GPT-3 model
    response = openai.Completion.create(
        engine="text-davinci-002",  # Replace with your preferred engine
        prompt=user_input,
        max_tokens=50  # Adjust as needed
    )

    # Display the model's response
    st.text("ChatGPT Clone:", response.choices[0].text)
    
