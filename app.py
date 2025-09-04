import streamlit as st
import cv2 
import numpy as np
from PIL import Image 
import easyocr as ocr 

st.title("Extracting Text From Image")


reader = ocr.Reader(['en', 'ar'])  

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None :

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image",use_column_width=True)

    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    with st.spinner("Extracting Text"):
        results = reader.readtext(image_cv)
    
    extracted_text = "\n".join([res[1] for res in results])

    st.subheader("Extracted Text:")
    st.text_area("Text from image:", extracted_text, height=200)