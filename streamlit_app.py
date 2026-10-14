"""AIGENDA (RoboBill) — AI-powered invoice and expense analyzer using Google Gemini."""

from __future__ import annotations

import os
from typing import Any

import streamlit as st
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")


def get_gemini_response(
    input_text: str, image_data: list[dict[str, Any]], prompt: str
) -> str:
    """Send image and prompt to Gemini and return the text response."""
    response = model.generate_content([input_text, image_data[0], prompt])
    return response.text


def extract_image_parts(uploaded_file: st.runtime.uploaded_file_manager.UploadedFile) -> list[dict[str, Any]]:
    """Convert an uploaded Streamlit file into the format Gemini expects."""
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        return [{"mime_type": uploaded_file.type, "data": bytes_data}]
    raise FileNotFoundError("No file was uploaded")


st.set_page_config(page_title="AIGENDA — AI Invoice Analyzer")
st.sidebar.header("RoboBill")
st.sidebar.write("Made by Swagata Banerjee")
st.sidebar.write("Powered by Google Gemini AI")
st.header("RoboBill")
st.subheader("by IEEE WIE")
st.subheader("Manage your expenses with RoboBill")

user_query = st.text_input("What do you want me to do?", key="input")
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Let's Go!")

SYSTEM_PROMPT = """You are an expert in invoice and bill analysis."""

if submit:
    image_data = extract_image_parts(uploaded_file)
    response = get_gemini_response(SYSTEM_PROMPT, image_data, user_query)
    st.subheader("Here's what you need to know!")
    st.write(response)
