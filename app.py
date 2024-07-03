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
    """
    input: the message that the llm model will behave like
    prompt: my input that I'm giving what kind of information I want 

    """
    ## loading the gemini model
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
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