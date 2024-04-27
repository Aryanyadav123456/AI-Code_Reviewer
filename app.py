import streamlit as st
import google.generativeai as genai

# Title of the Streamlit app with emoji
st.snow()
st.title('🔍🔍🔍🔍📃AI Code_Reviewer')

# Text area for user to input code
user_code = st.text_area("Enter your code here:", height=200)

# Load API key from a file (assuming gemini.txt contains the API key)
with open("gemini.txt", "r") as f:
    api_key = f.read().strip()

# Configure Google Generative AI with the API key
genai.configure(api_key=api_key)

# Initialize the GenerativeModel
model = genai.GenerativeModel(
    model_name="models/gemini-1.5-pro-latest",
    system_instruction="you have to check input code given by the user and give the report about the errors and atlast give the correct code"
)

# Function to generate content based on user input
def generate_code_prediction(user_prompt):
    response = model.generate_content(user_prompt)
    return response.text

# Check if the user has clicked the Predict button
if st.button('Predict'):
    st.balloons()
    # Check if the user has entered any code
    if user_code.strip() == "":
        st.error("Please enter some code to predict.")
    else:
        # Generate code prediction
        prediction = generate_code_prediction(user_code)
        st.write("Predicted Code:")
        st.code(prediction, language='python')  # Display the predicted code
