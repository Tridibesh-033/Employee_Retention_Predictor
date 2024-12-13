import pickle
import pandas as pd
import streamlit as st


model = pickle.load(open('emp_reten.pkl', 'rb'))


def load_css(file_path):
    with open(file_path, "r") as f:
        return f"<style>{f.read()}</style>"
    
css_styles = load_css("style.css")

st.markdown(css_styles, unsafe_allow_html=True)


def main():
    st.title("Employee Retention Analytics")
    st.write("This application predicts whether an employee will stay or leave based on input features")

    # Input fields for user to enter data
    col1, col2 = st.columns(2)

    with col1:
        satisfaction_level = st.number_input("Satisfaction Level", min_value=0.0, max_value=1.0, step=0.01, value=0.5)
        promotion_last_5years = st.selectbox("Promotion in Last 5 Years", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        salary_medium = st.selectbox("Salary: Medium", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
       
    with col2:
        average_monthly_hours = st.number_input("Average Monthly Hours", min_value=0, max_value=500, step=1, value=160)
        salary_high = st.selectbox("Salary: High", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        salary_low = st.selectbox("Salary: Low", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")


    # Prepare input data for prediction
    if st.button("Predict"):
        input_data = pd.DataFrame({
        'satisfaction_level': [satisfaction_level],
        'average_montly_hours': [average_monthly_hours],
        'promotion_last_5years': [promotion_last_5years],
        'salary_high': [salary_high],
        'salary_low': [salary_low],
        'salary_medium': [salary_medium]
      })

    
        prediction = model.predict(input_data)

        
        if prediction[0] == 0:
            st.success("The Employee will Stay")
        else:
            st.error("The Employee will Left")

if __name__ == "__main__":
    main()

