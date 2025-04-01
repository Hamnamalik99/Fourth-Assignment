import streamlit as st  # Import Streamlit library for creating the app

# Custom CSS for light theme
st.markdown(
    """
    <style>
        /* Basic body styling */
        body {
            background-color: #f7f7f7;  /* Light gray background */
            color: #333;  /* Dark text color */
        }

        /* App background styling */
        .stApp {
            background-color: #f7f7f7;  /* Keeping the app's background light gray */
        }

        /* Button styling */
        .stButton>button {
            background-color: #4CAF50;  /* Green button */
            color: white;  /* White text */
            font-size: 16px;  /* Text size */
            padding: 8px 16px;  /* Padding inside the button */
            border-radius: 8px;  /* Rounded corners for the button */
            border: none;  /* No border */
        }

        /* Button hover effect */
        .stButton>button:hover {
            background-color: #45a049;  /* Darker green when hovered */
        }

        /* Input fields styling */
        .stNumberInput>div>input {
            font-size: 14px;  /* Font size */
            padding: 8px;  /* Padding inside the input fields */
            border-radius: 6px;  /* Rounded corners */
            border: 1px solid #ddd;  /* Light gray border */
        }

        /* Card container styling */
        .card {
            padding: 20px;  /* Padding inside the card */
            border-radius: 10px;  /* Rounded corners */
            background: white;  /* White background for the card */
            color: black;  /* Black text */
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);  /* Light shadow effect */
            text-align: center;  /* Centering the text */
            margin: 20px auto;  /* Margin for spacing */
            max-width: 400px;  /* Maximum width of the card */
        }
    </style>
    """,
    unsafe_allow_html=True  # Allow HTML and CSS styling in the app
)

# Title of the app
st.markdown("<h1 style='text-align: center; color: #333;'>💪 BMI Calculator</h1>", unsafe_allow_html=True)

# Centered container for inputs (using card class for styling)
st.markdown("<div class='card'>", unsafe_allow_html=True)

# Input fields for weight and height using Streamlit's number input
weight = st.number_input("⚖️ Enter your weight (kg)", min_value=1.0, step=0.1)  # Weight input field
height = st.number_input("📏 Enter your height (m)", min_value=0.1, step=0.01)  # Height input field

st.markdown("</div>", unsafe_allow_html=True)  # Closing the card div tag

# Calculate BMI when button is clicked
if st.button("Calculate BMI"):  # If the "Calculate BMI" button is clicked
    if height > 0:  # Check if height is greater than 0 to avoid division by zero
        bmi = weight / (height ** 2)  # BMI formula: weight (kg) / height (m) squared
        # Display the calculated BMI
        st.markdown(f"<h2 style='text-align: center; color: #444;'>📊 Your BMI is: **{bmi:.2f}**</h2>", unsafe_allow_html=True)

        # Categorize the BMI into different groups and display corresponding message
        if bmi < 18.5:
            st.warning("⚠️ You are **Underweight**. Consider a healthy diet.")
        elif 18.5 <= bmi < 24.9:
            st.success("✅ You have a **Normal Weight**. Keep it up!")
        elif 25 <= bmi < 29.9:
            st.warning("⚠️ You are **Overweight**. Try to stay active.")
        else:
            st.error("❌ You are **Obese**. Consider a healthier lifestyle.")
    else:
        st.error("⚠️ Height must be greater than zero.")  # Display error if height is zero or less
