import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image
import google.generativeai as genai

# ✅ Load .env file
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# ✅ Configure Gemini
genai.configure(api_key=API_KEY)

# ✅ Streamlit UI setup
st.set_page_config(page_title="ChartWhisperer with Gemini", layout="centered")
st.title("📊 ChartWhisperer")
st.markdown("Upload a chart image and let Gemini Vision generate business insights.")

# ✅ File uploader
uploaded_file = st.file_uploader("Upload your chart", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Chart", use_container_width=True)

    if st.button("Get Business Insights"):
        with st.spinner("Analyzing chart using Gemini Vision..."):
            try:
                model = genai.GenerativeModel("models/gemini-1.5-flash")  # faster, cheaper
                response = model.generate_content([
                    "Give 3 business insights from this chart in bullet points.", image
                ])
                st.markdown("### 🧠 Gemini Insights")
                st.success(response.text)
            except Exception as e:
                st.error(f"Gemini API error: {e}")
