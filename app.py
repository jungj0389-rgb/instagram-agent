import streamlit as st
import time
import openai
import os

# OpenAI API-Key über Streamlit Secrets
openai.api_key = os.environ["OPENAI_API_KEY"]

def generate_instagram_reply(question):
    """
    Instagram Answer Agent:
    - freundlich, locker, positiv, kurz
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # aktuelles Modell
        messages=[
            {"role": "system", "content": "Du bist ein Instagram-Assistant. Antworte freundlich, locker und kurz."},
            {"role": "user", "content": question}
        ],
        max_tokens=100
    )
    return response['choices'][0]['message']['content'].strip()

st.title("Instagram Answer Agent")
st.write("Gib eine Frage ein und erhalte eine perfekte Antwort für Instagram.")

frage = st.text_area("Frage eingeben")
if st.button("Antwort generieren"):
    with st.spinner("Antwort wird erstellt..."):
        antwort = generate_instagram_reply(frage)
        time.sleep(0.5)
        st.success(antwort)
