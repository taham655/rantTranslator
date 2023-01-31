import streamlit as st
import openai
import os
from rant_translator.functions import summarize

openai.api_key = "" #this is where your open ai api key goes



if "rant" not in st.session_state:
    st.session_state["rant"] = ""

st.title("Rant Translator")

input_text = st.text_area(label="Please Rant here:", value="", height=250)

st.button(
    "Translate",
    on_click=summarize,
    kwargs={"prompt": input_text},
)

output_text = st.text_area(label="AI generated politness:", value=st.session_state["rant"], height=250)

#streamlit run app.py
