import os
import json
from PIL import Image
import streamlit as st
import google.generativeai as genai

def ask_and_get_answer(prompt, img):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([prompt, img])
    return response.text
    


if __name__ == "__main__":
    with open("../config.json", "r") as f:
        config = json.load(f)
    genai.configure(api_key=config['gemini_api_key'])