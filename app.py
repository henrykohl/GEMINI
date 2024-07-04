## Invoice Extractor

from dotenv import load_dotenv

load_dotenv() ## load all environment variables from .env

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

## configuring API key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini Pro vision model and get response

def get_gemini_response(input,image,prompt):
    ## """
    ## input: the message that the llm model will behave like
    ## image: a LIST of <class 'dict'> ，所以 image[0] 就是 {"mime_type": ...,"data": ...} 
    ## prompt: my input that I'm giving what kind of information I want 

    ##"""
    ## loading the gemini model
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    ## """
    ## 設定回傳的物件是一個 list
    ## """
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type, # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

## initialize our streamlit app

st.set_page_config(page_title="Invoice Extractor")

st.header("Gemini Application")
## """"
## input 結果是 str 類型
## """
input=st.text_input("Input Prompt: ",key="input") ## key 是 optional
## """
## uploaded_file  是 <class 'streamlit.runtime.uploaded_file_manager.UploadedFile'> 類型
## """
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image=""
if uploaded_file is not None:
    # """image 類型是 <class 'PIL.PngImagePlugin.PngImageFile'>"""
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Tell me about the invoice")

input_prompt="""
You are an expert in understanding invoices. You will 
receive input images as invoices and you will have to
answer questions based on the input image.
"""

## If submit button is clicked

if submit:
    ## """image_data 將是 list 類型"""
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)

    st.subheader("The Response is")
    st.write(response)    