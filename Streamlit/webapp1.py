import streamlit as st
from PIL import Image
import io

st.title("Image to PDF Converter!")
file = st.file_uploader("Upload your image!", type=['jpg','jpeg','png'])

if file:
    st.image(file)

    if st.button("Convert to PDF"):
        img = Image.open(file)
        pdf_bytes = io.BytesIO()
        img.convert('RGB').save(pdf_bytes, format="PDF")

        st.download_button(
            label='Download PDF', 
            data=pdf_bytes, 
            file_name="converted.pdf")
        
