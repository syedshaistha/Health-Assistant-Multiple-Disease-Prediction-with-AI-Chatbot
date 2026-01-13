import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# ------------------- Page Config -------------------
st.set_page_config(
    page_title="Health Assistant",
    layout="wide",
    page_icon="🧑‍⚕️"
)

# ------------------- Custom Styling (enhanced sidebar) -------------------
st.markdown("""
    <style>
    /* keep your app background */
    .stApp {
        background-color: #f5f7fa;
    }
            
    /* Sidebar background */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e3c72, #2a5298);
        color: white;
    }

    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] li {
        color: white !important;
    }

    /* Make the sidebar collapse/hide arrow visible (white) */
    .st-emotion-cache-pd6qx2 {
        color: white !important;
        background-color: rgba(0,0,0,0.5) !important;
        border-radius: 50%;
        box-shadow: 0 2px 6px rgba(0,0,0,0.2);
    }

    /* nav-link styling from streamlit-option-menu (scoped to sidebar) */
    [data-testid="stSidebar"] .nav-link {
        color: white !important;
        background: transparent !important;
        border-radius: 8px;
        padding: 10px 12px;
        margin: 6px 0;
        display: flex;
        align-items: center;
        gap: 12px;
        transition: transform 0.12s ease, background-color 0.12s ease, box-shadow 0.12s;
    }
            
    [data-testid="stSidebar"] .nav-link:hover {
        background-color: rgba(255,255,255,0.06) !important;
        transform: translateX(4px);
    }

    /* Selected/active item */
    [data-testid="stSidebar"] .nav-link.selected,
    [data-testid="stSidebar"] .nav-link.active,
    [data-testid="stSidebar"] .nav-link[aria-current="true"] {
        background: linear-gradient(90deg,#36d1dc,#5b86e5) !important;
        color: white !important;
        box-shadow: 0 6px 18px rgba(59,130,246,0.18) !important;
        transform: translateX(2px);
        font-weight: 600;
    }

    /* keep the rest of your original styles unchanged (inputs/buttons/titles) */
    h1, h2, h3 {
        color: #1e3c72;
        font-weight: bold;
    }

    .st-emotion-cache-r44huj h1 {
        padding: 8px 0px 1rem;
    }        

    /* ------------------ FORM INPUT STYLING (right side) ------------------ */
    .stTextInput > div > div > input,
    .stNumberInput input,
    .stSelectbox select,
    .stTextArea textarea {
        background-color: #ffffff !important;
        border: 2px solid #d1d5db !important; /* neutral gray */
        border-radius: 10px !important;
        padding: 10px 14px !important;
        font-size: 15px !important;
        transition: all 0.2s ease !important;
        box-shadow: none !important;
    }

    /* On hover */
    .stTextInput > div > div > input:hover,
    .stNumberInput input:hover,
    .stSelectbox select:hover,
    .stTextArea textarea:hover {
        border-color: #5b86e5 !important;
    }

    /* On focus (clicked into input) */
    .stTextInput > div > div > input:focus,
    .stNumberInput input:focus,
    .stSelectbox select:focus,
    .stTextArea textarea:focus {
        border-color: #36d1dc !important;
        box-shadow: 0 0 6px rgba(54,209,220,0.3) !important;
        outline: none !important;
    }
    .st-br, .st-bq, .st-bp, .st-bo, .st-bn {  /* remove borders from st.beta_columns and similar */
        border-color: white !important;}


    /* ------------------ BUTTON STYLING ------------------ */
    
    div.stButton > button {
        background: linear-gradient(to right, #36d1dc, #5b86e5);
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: bold;
        border: none;
        cursor: pointer;
        transition: 0.3s;
        display: block;
        margin: 0 auto;
    }

    div.stButton > button:hover {
        background: linear-gradient(to right, #5b86e5, #36d1dc);
        transform: scale(1.05);
    }

    /* ------------------ RESULT DISPLAY STYLING ------------------ */
    .stDataFrame, .stAlert {
        border: 1px solid #e0e7ff !important;
        border-radius: 14px !important;
        margin-top: 12px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06) !important;
        font-size: 15px !important;
        line-height: 1.6 !important;
    }

    /* Optional: fancy gradient border wrapper */
    .result-box {
        border: 2px solid transparent;
        border-radius: 14px;
        background: linear-gradient(#fff, #fff) padding-box,
                    linear-gradient(90deg, #36d1dc, #5b86e5) border-box;
        padding: 16px 20px;
        box-shadow: 0 6px 16px rgba(91,134,229,0.15);
    }

    /*----------------------- Center the main block container ---------------*/
    .stMainBlockContainer {
        border-radius: 14px;
        background: linear-gradient(#fff, #fff) padding-box,
                    linear-gradient(90deg, #36d1dc, #5b86e5) border-box;
        padding: 16px;
        box-shadow: 0 6px 16px rgba(91,134,229,0.15);
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 90%;
        margin-top: 27px;
        max-height: 90vh;
        overflow-y: auto;
        padding-top: 0px;
    }

    @media screen and (max-width: 768px) {
        .stMainBlockContainer {
            width: 95%;          /* make it slightly smaller on small screens */
            max-height: 90vh;    /* prevent it from overflowing vertically */
            overflow-y: auto;    /* scroll if content is too tall */
            padding: 12px 16px;  /* adjust padding for small screens */
            top: 50%;            /* still center vertically */
            left: 50%;           /* still center horizontally */
            transform: translate(-50%, -50%);
        }
    }

    /* Success box override */
    .stSuccess {
        background-color: #e3f9e5;
        border: 1px solid #27ae60;
        border-radius: 8px;
        color: #2d572c;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)



# ------------------- Working Directory -------------------
working_dir = os.path.dirname(os.path.abspath(__file__))

# ------------------- Load Saved Models -------------------
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

# ------------------- Import MediChat -------------------
from MediChat.app import run_medichat  # Make sure set_page_config() is removed from MediChat/app.py

with st.sidebar:
    selected = option_menu(
        menu_title="Multiple Disease Prediction System",
        options=['Diabetes Prediction', 'Heart Disease Prediction', "Parkinson's Prediction", 'MediChat', 'Health Tips', 'Calculators'],
        icons=['activity', 'heart', 'person', 'chat-dots', 'lightbulb', 'calculator'],
        menu_icon='hospital',
        default_index=0,
        orientation="vertical",
        styles={
            "menu-title": {"text-align": "center"},
            "container": {"padding": "1rem", "background": "transparent"},
            "icon": {"color": "black", "font-size": "20px"},
            "nav-link": {
                "font-size": "16px",
                "color": "black",
                "padding": "10px 12px",
                "border-radius": "8px",
                "margin": "6px 0"
            },
            "nav-link-selected": {
                "background": "linear-gradient(90deg,#36d1dc,#5b86e5)",
                "color": "white",
                "font-weight": "600",
                "box-shadow": "0 6px 18px rgba(59,130,246,0.18)"
            }
        }
    )


# ------------------- Diabetes Prediction -------------------
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    # Ensure keys exist in session_state
    keys = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", 
            "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]
    for k in keys:
        if k not in st.session_state:
            st.session_state[k] = ""

    col1, col2, col3 = st.columns(3)

    with col1:  Pregnancies = st.text_input('Number of Pregnancies', key="Pregnancies", value=st.session_state["Pregnancies"], placeholder="Enter value", autocomplete="off")

    with col2:  Glucose = st.text_input('Glucose Level', key="Glucose", value=st.session_state["Glucose"], placeholder="Enter value", autocomplete="off")

    with col3:  BloodPressure = st.text_input('Blood Pressure value', key="BloodPressure", value=st.session_state["BloodPressure"], placeholder="Enter value", autocomplete="off")

    with col1:  SkinThickness = st.text_input('Skin Thickness value', key="SkinThickness", value=st.session_state["SkinThickness"], placeholder="Enter value", autocomplete="off")

    with col2:  Insulin = st.text_input('Insulin Level', key="Insulin", value=st.session_state["Insulin"], placeholder="Enter value", autocomplete="off")

    with col3:  BMI = st.text_input('BMI value', key="BMI", value=st.session_state["BMI"], placeholder="Enter value", autocomplete="off")

    with col1:  DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', key="DiabetesPedigreeFunction", value=st.session_state["DiabetesPedigreeFunction"], placeholder="Enter value", autocomplete="off")

    with col2:  Age = st.text_input('Age of the Person', key="Age", value=st.session_state["Age"], placeholder="Enter value", autocomplete="off")

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        try:
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            user_input = [float(x) for x in user_input]
            diab_prediction = diabetes_model.predict([user_input])
            diab_diagnosis = '🩸 The person is diabetic' if diab_prediction[0] == 1 else '✅ The person is not diabetic'
        except ValueError:
            diab_diagnosis = "⚠️ Please enter valid numeric values."

    st.success(diab_diagnosis)

# ------------------- Heart Disease Prediction -------------------
elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    # Keys for heart disease form
    heart_keys = [
        "age", "sex", "cp", "trestbps", "chol", "fbs",
        "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"
    ]

    # Initialize session_state values
    for k in heart_keys:
        if k not in st.session_state:
            st.session_state[k] = ""

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age", key="age", value=st.session_state["age"], placeholder="Enter value", autocomplete="off")
    with col2:
        sex = st.text_input("Sex", key="sex", value=st.session_state["sex"], placeholder="Enter value", autocomplete="off")
    with col3:
        cp = st.text_input("Chest Pain types", key="cp", value=st.session_state["cp"], placeholder="Enter value", autocomplete="off")

    with col1:
        trestbps = st.text_input("Resting Blood Pressure", key="trestbps", value=st.session_state["trestbps"], placeholder="Enter value", autocomplete="off")
    with col2:
        chol = st.text_input("Serum Cholestoral in mg/dl", key="chol", value=st.session_state["chol"], placeholder="Enter value", autocomplete="off")
    with col3:
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl", key="fbs", value=st.session_state["fbs"], placeholder="Enter value", autocomplete="off")

    with col1:
        restecg = st.text_input("Resting Electrocardiographic results", key="restecg", value=st.session_state["restecg"], placeholder="Enter value", autocomplete="off")
    with col2:
        thalach = st.text_input("Maximum Heart Rate achieved", key="thalach", value=st.session_state["thalach"], placeholder="Enter value", autocomplete="off")
    with col3:
        exang = st.text_input("Exercise Induced Angina", key="exang", value=st.session_state["exang"], placeholder="Enter value", autocomplete="off")

    with col1:
        oldpeak = st.text_input("ST depression induced by exercise", key="oldpeak", value=st.session_state["oldpeak"], placeholder="Enter value", autocomplete="off")
    with col2:
        slope = st.text_input("Slope of the peak exercise ST segment", key="slope", value=st.session_state["slope"], placeholder="Enter value", autocomplete="off")
    with col3:
        ca = st.text_input("Major vessels colored by flourosopy", key="ca", value=st.session_state["ca"], placeholder="Enter value", autocomplete="off")

    with col1:
        thal = st.text_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect", key="thal", value=st.session_state["thal"], placeholder="Enter value", autocomplete="off")

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        try:
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            user_input = [float(x) for x in user_input]
            heart_prediction = heart_disease_model.predict([user_input])
            heart_diagnosis = '❤️ The person is having heart disease' if heart_prediction[0] == 1 else '✅ The person does not have any heart disease'
        except ValueError:
            heart_diagnosis = "⚠️ Please enter valid numeric values."

    st.success(heart_diagnosis)

# ------------------- Parkinson's Prediction -------------------
elif selected == "Parkinson's Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    # List of all input keys
    parkinson_keys = [
    "fo", "fhi", "flo", "Jitter_percent",
    "Shimmer", "NHR", "HNR",
    "RPDE", "DFA", "spread1",
    "spread2", "PPE"
    ]

    # Initialize in session_state
    for k in parkinson_keys:
        if k not in st.session_state:
            st.session_state[k] = ""

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        fo = st.text_input("MDVP:Fo(Hz)", key="fo", placeholder="Enter value")
    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)", key="fhi", placeholder="Enter value")
    with col3:
        flo = st.text_input("MDVP:Flo(Hz)", key="flo", placeholder="Enter value")
    with col4:
        Jitter_percent = st.text_input("MDVP:Jitter(%)", key="Jitter_percent", placeholder="Enter value")


    with col1:
        Shimmer = st.text_input("MDVP:Shimmer", key="Shimmer", placeholder="Enter value")
    with col2:
        NHR = st.text_input("NHR", key="NHR", placeholder="Enter value")
    with col3:
        HNR = st.text_input("HNR", key="HNR", placeholder="Enter value")
    with col4:
        RPDE = st.text_input("RPDE", key="RPDE", placeholder="Enter value")


    with col1:
        DFA = st.text_input("DFA", key="DFA", placeholder="Enter value")
    with col2:
        spread1 = st.text_input("spread1", key="spread1", placeholder="Enter value")
    with col3:
        spread2 = st.text_input("spread2", key="spread2", placeholder="Enter value")
    with col4:
        PPE = st.text_input("PPE", key="PPE", placeholder="Enter value")


    parkinsons_diagnosis = ""
    if st.button("Parkinson's Test Result"):
        try:
            user_input = [
                fo, fhi, flo, Jitter_percent, Shimmer,
                NHR, HNR, RPDE, DFA, spread1, spread2, PPE
            ]

            # check empty
            if any(val.strip() == "" for val in user_input):
                raise ValueError("Empty input")

            user_input = [float(val) for val in user_input]

            parkinsons_prediction = parkinsons_model.predict([user_input])

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "🧠 The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "✅ The person does not have Parkinson's disease"

        except ValueError:
            parkinsons_diagnosis = "⚠️ Please enter valid numeric values in all fields."

    st.success(parkinsons_diagnosis)


# ------------------- MediChat Integration -------------------
elif selected == 'MediChat':
    run_medichat()  # Directly call the Streamlit MediChat app

# ------------------- Health Tips -------------------
elif selected == 'Health Tips':
    st.title("💡 Health & Wellness Tips")

    tip_category = st.selectbox("Select a Category", ["General", "Diabetes", "Heart", "Parkinson's"])
    
    tips = {
        "General": [
            "💧 Drink at least 2-3 liters of water daily",
            "🏃‍♀️ Exercise for 30 minutes a day",
            "😴 Get 7-8 hours of sleep",
            "🚭 Avoid smoking & alcohol"
        ],
        "Diabetes": [
            "🩸 Monitor blood sugar regularly",
            "🥗 Eat high-fiber, low-carb meals",
            "🥤 Avoid sugary drinks",
            "🚶‍♂️ Stay active daily"
        ],
        "Heart": [
            "🍎 Eat more fruits and vegetables",
            "🧂 Limit salt and processed foods",
            "🧘‍♀️ Practice stress management",
            "❤️ Go for regular heart check-ups"
        ],
        "Parkinson's": [
            "🧘‍♂️ Do regular light exercises",
            "🥦 Maintain a balanced diet",
            "🧩 Engage in mental activities like puzzles",
            "👥 Join support groups for motivation"
        ]
    }

    for tip in tips[tip_category]:
        st.markdown(f"- {tip}")

elif selected == 'Calculators':
    st.title("🧮 Calculators")

    calculator_type = st.selectbox("Select a Calculator", ["BMI", "Calorie", "Blood Pressure", "Body Fat"])

    if calculator_type == "BMI":
        st.subheader("BMI Calculator")
        weight = st.number_input("Enter your weight (kg)", min_value=0.0)
        height = st.number_input("Enter your height (m)", min_value=0.0)
        if st.button("Calculate BMI"):
            if height > 0:
                bmi = weight / (height ** 2)
                st.success(f"Your BMI is: {bmi:.2f}")
            else:
                st.error("Invalid Inputs")

    elif calculator_type == "Calorie":
        st.subheader("Calorie Calculator")
        import streamlit as st
        # First row
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.number_input("Enter your age", min_value=0)
        with col2:
            weight = st.number_input("Enter your weight (kg)", min_value=0.0)
        with col3:
            height = st.number_input("Enter your height (cm)", min_value=0.0)
            
        # Second row
        col4, col5 = st.columns(2)
        with col4:
            gender = st.selectbox("Select your gender", ["Male", "Female"])
        with col5:
            activity_level = st.selectbox("Select your activity level", ["Sedentary", "Light", "Moderate", "Active"])

        if st.button("Calculate Calories"):
            # Simple calorie estimation formula
            if gender == "Male":
                bmr = 10 * weight + 6.25 * height - 5 * age + 5
            else:
                bmr = 10 * weight + 6.25 * height - 5 * age - 161
            if activity_level == "Sedentary":
                calories = bmr * 1.2
            elif activity_level == "Light":
                calories = bmr * 1.375
            elif activity_level == "Moderate":
                calories = bmr * 1.55
            else:
                calories = bmr * 1.725
            st.success(f"Your daily calorie needs are: {calories:.2f}")

    elif calculator_type == "Blood Pressure":
        st.subheader("Blood Pressure Calculator")
        systolic = st.number_input("Enter systolic pressure (mmHg)", min_value=0)
        diastolic = st.number_input("Enter diastolic pressure (mmHg)", min_value=0)
        if st.button("Check Blood Pressure"):
            if systolic > 0 and diastolic > 0:
                if systolic < 120 and diastolic < 80:
                    st.success("Your blood pressure is normal.")
                elif systolic < 130 and diastolic < 80:
                    st.warning("Your blood pressure is elevated.")
                else:
                    st.error("You may have hypertension.")
            else:
                st.error("Invalid blood pressure readings.")

    elif calculator_type == "Body Fat":
        st.subheader("Body Fat Calculator")
        col1, col2 = st.columns(2)
        with col1:
            weight = st.number_input("Enter your weight (kg)", min_value=0.0)
        with col2:
            height = st.number_input("Enter your height (m)", min_value=0.0)

        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Enter your age", min_value=0)
        with col2:
            gender = st.selectbox("Select your gender", ["Male", "Female"])
        
        if st.button("Calculate Body Fat"):
            BMI = weight / (height ** 2) if height > 0 else 0
            if gender == "Male":
                body_fat = (1.20 * BMI) + (0.23 * age) - 16.2
            else:
                body_fat = (1.20 * BMI) + (0.23 * age) - 5.4
            st.success(f"Your body fat percentage is:  {body_fat:.2f}%")

    