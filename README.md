# 🏥 Health Assistant – Multiple Disease Prediction with AI Chatbot

An AI-powered health assistant web application that predicts multiple diseases such as **Diabetes**, **Heart Disease**, and **Parkinson’s Disease** using **Machine Learning models**, along with an **AI-based health chatbot** for interactive assistance.  
The application is built using **Python** and **Streamlit**.

---

## ✨ Key Highlights

### 🧠 Multiple Disease Prediction
- Diabetes
- Heart Disease
- Parkinson’s Disease

### 🤖 AI Health Chatbot
- Interactive chatbot for health-related guidance
- API-based (secure key handling)

### 📊 Pre-trained ML Models
- Accurate and efficient predictions

### 🎨 User-Friendly UI
- Simple, clean Streamlit interface

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Web Framework:** Streamlit  
- **Machine Learning:** Scikit-learn  
- **Data Handling:** NumPy, Pandas  
- **Model Storage:** Pickle  
- **UI Components:** Streamlit Option Menu  
- **Chatbot:** API-based AI chatbot  

---

## 📂 Project Structure

Health-Assistant-Multiple-Disease-Prediction-with-AI-Chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── saved_models/
│ ├── diabetes_model.pkl
│ ├── heart_model.pkl
│ └── parkinsons_model.pkl
│
├── collab_files_to_train_models/
│ ├── diabetes.py
│ ├── heart.py
│ └── parkinsons.py
│
├── datasets/
│ ├── diabetes.csv
│ ├── heart.csv
│ └── parkinsons.csv
│
├── MediChat/
│ └── app.py
│
├── src/
│ └── init.py
│
├── static/
│ └── style.css
│
└── templates/
└── chatbot.html

---

## 🚀 How to Clone and Run the Project

### 🔹 Step 1: Clone the Repository
```bash
git clone https://github.com/<your-username>/Health-Assistant-Multiple-Disease-Prediction-with-AI-Chatbot.git
cd Health-Assistant-Multiple-Disease-Prediction-with-AI-Chatbot

### 🔹 Step 2: (Optional) Create a Virtual Environment

python -m venv venv

Activate it:

Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate

### 🔹 Step 3: Install Dependencies

pip install -r requirements.txt

### 🔹 Step 4: Run the Application

streamlit run app.py

🔹 Step 5: Open in Browser

http://localhost:8501

###🤖 Chatbot API Configuration (Important)

The chatbot feature uses an external API.
For security reasons, API keys are NOT included in this repository.

##🔐 Option 1: Using .env File (Local Setup)

Create a .env file in the root directory:

CHATBOT_API_KEY=your_api_key_here


Ensure .env is added to .gitignore.

##🔐 Option 2: Using Streamlit Secrets

Create the file:

.streamlit/secrets.toml


Add:

CHATBOT_API_KEY = "your_api_key_here"

📌 Without Configuring the API Key

✅ Disease prediction features will work

❌ Chatbot feature will be disabled

###⚠️ Disclaimer

This application is developed only for educational and academic purposes.
It is not a substitute for professional medical advice or diagnosis.

###👩‍💻 Author

Shaistha Sulthana
Mini Project – Health Assistant: Multiple Disease Prediction with AI Chatbot

###🌟 Future Enhancements

- More disease prediction modules
- Advanced chatbot responses
- User authentication
- Cloud deployment
