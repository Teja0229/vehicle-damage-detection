import streamlit as st
from model_helper import predict

st.title("Vehicle Damage Detection")
st.caption("AI-powered vehicle damage classification using ResNet50")


uploaded_file = st.file_uploader("Upload the file", type=["jpg", "png"])

if  uploaded_file:
    image_path = "temp_file.png"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        st.image(uploaded_file, caption="Uploaded File", use_container_width=True)
        prediction = predict(image_path)
        st.info(f"predicted Class: {prediction}")


st.markdown(
    '<div class="footer-note"> Vehicle Damage Detection • ResNet50 Deep Learning Model </div>',
    unsafe_allow_html=True
)

