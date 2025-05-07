# 📊 ChartWhisperer

**ChartWhisperer** is a Streamlit-based AI assistant powered by Google's Gemini Vision. It analyzes uploaded chart images and provides actionable business insights in plain English.

---

## 🚀 Features

- 🖼️ Upload PNG, JPG, or JPEG chart images
- 🔍 Uses Google Gemini 1.5 Vision models (`flash` or `pro`)
- 💡 Returns 3 business insights per chart
- 🧠 Built with Streamlit and Gemini API

---

## 🖼️ Demo

<img width="259" alt="output1" src="https://github.com/user-attachments/assets/71903d43-2112-4f80-90cb-497306c75d43" />

---

## ⚙️ Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/chartwhisperer.git
cd chartwhisperer

2. Create and Activate Virtual Environment
bash
Copy
Edit

python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

3. Install Requirements
pip install -r requirements.txt


4. Add Your API Key
Create a .env file in the root directory:

env
Copy
Edit
GOOGLE_API_KEY=your_google_gemini_api_key_here

You can generate your API key here:
👉 https://makersuite.google.com/app/apikey

▶️ Run the App
bash
Copy
Edit

streamlit run app.py

🧠 Example Use Cases
Explain dashboards for stakeholders
Generate executive summaries from visual reports
Help students interpret complex charts


📦 Requirements
Python 3.8 – 3.11
Streamlit
Pillow
python-dotenv
google-generativeai

✨ Author
Built by Varshitha Yanamala
