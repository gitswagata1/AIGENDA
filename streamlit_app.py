import streamlit as st
import os
from PIL import Image 
import google.generativeai as genai

genai.configure(api_key ="AIzaSyBT6vZr600t5Yl5AHJRlyWoROcThqhtGZQ")

model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input_text, image_data, prompt):
    response = model.generate_content([input_text, image_data[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file was uploaded")
    
st.set_page_config(page_title = "WIE's Invoice Generator")
st.sidebar.header("RoboBill")
st.sidebar.write("Made by Swagata Banerjee")
st.sidebar.write("powered By google gemini ai")
st.header("Robobill")
st.subheader("by IEEE WEI")
st.subheader("manage your expenses with Robobill")
input = st.text_input ("What do you want me to do?", key = "input")
uploaded_file = st.file_uploader("Choose an image", type=["jpg,","jpeg", "png"])
image = " "
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "Uploaded Image", use_column_width= True)

ssubmit = st.button("Lets Go!")

input_prompt = """
You are an expext in Invoice bill analysis
"""
if ssubmit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("Here's what you nee to know!")
    st.write(response)
