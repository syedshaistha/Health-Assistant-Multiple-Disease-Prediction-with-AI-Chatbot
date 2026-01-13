#📌 Health Assistant – Multiple Disease Prediction with AI Chatbot

An AI-powered health assistant web application that predicts multiple diseases such as Diabetes, Heart Disease, and Parkinson’s Disease using Machine Learning models, and also provides an interactive AI chatbot to assist users with health-related queries. The application is built using Python and Streamlit.

#🧠 Features

-🔬 Multiple Disease Prediction

-Diabetes Prediction

-Heart Disease Prediction

-Parkinson’s Disease Prediction

-🤖 AI Health Chatbot

--Interactive chatbot interface

--Provides basic health guidance and explanations

-📊 Machine Learning Models

--Pre-trained ML models for accurate predictions

-🌐 User-Friendly Interface

--Clean and simple Streamlit UI

#🛠️ Technologies Used

-Python

-Streamlit

-Machine Learning (Scikit-learn)

-NumPy

-Pandas

-Pickle

-Streamlit Option Menu

#📁 Project Structure

Health-Assistant-Multiple-Disease-Prediction-with-AI-Chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENCE
├── .gitignore
│
├── saved_models/
│   ├── diabetes_model.pkl
│   ├── heart_model.pkl
│   └── parkinsons_model.pkl
│
├── collab_files_to_train_models/
│   ├── diabetes.py
│   ├── heart.py
│   └── parkinsons.py
│
├── datasets/
│   ├── diabetes.csv
│   ├── heart.csv
│   └── parkinsons.csv
│
├── MediChat/
│   └── app.py
│   └── src/
│        └── _init_.py
│   └── static/
│        └── style.css
│   └── templates/
│        └── chatbot.html

#⚙️ How to Clone and Run the Project (Disease Prediction + Chatbot)
🔹 Step 1: Clone the Repository

git clone https://github.com/<your-username>/Health-Assistant-Multiple-Disease-Prediction-with-AI-Chatbot.git

cd Health-Assistant-Multiple-Disease-Prediction-with-AI-Chatbot

🔹 Step 2: Create a Virtual Environment (Optional but Recommended)

python -m venv venv

Activate it:

Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate

🔹 Step 3: Install Required Dependencies

pip install -r requirements.txt

🔹 Step 4: Run the Application

streamlit run app.py

🔹 Step 5: Access the Application

Open your browser and go to:

http://localhost:8501

You can now:

Predict diseases using ML models

Interact with the AI health chatbot

#⚠️ Disclaimer

This application is intended for educational and academic purposes only.
It should not be used as a substitute for professional medical advice.

#👩‍💻 Author

Shaistha Sulthana
Mini Project – Health Assistant - Multiple Disease Prediction with AI Chatbot
