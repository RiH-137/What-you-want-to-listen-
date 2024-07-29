
import requests
import streamlit as st
import json

# Define the URL and headers for the API request
url = "http://localhost:11434/api/generate"
headers = {
    'Content-Type': 'application/json',
}

history = []

def generate_response(prompt):
    history.append(prompt)

    final_prompt = "\n".join(history)

    data = {
        "mode": "Thought1",
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data['response']
        return actual_response
    else:
        return "Error: " + response.text

# Streamlit UI
st.title("What you want to listen")

# Input for URL
url_input = st.text_input("Paste your URL here:")

# Dropdown menu
options = ["appreciate", "roast"]
selected_option = st.selectbox("Choose an option", options)

if st.button("Generate Response"):
    if url_input and selected_option:
        prompt = f"URL: {url_input}\nOption: {selected_option}"
        response = generate_response(prompt)
        st.write(response)
    else:
        st.warning("Please enter a URL and select an option.")
