# 🧠 Employee Retention Predictor

A machine learning web application that predicts whether an employee will **stay or leave** the company based on satisfaction level, work hours, salary, and promotion status.

## Why Retention ??
![img alt](https://github.com/Tridibesh-033/Employee_Retention_Predictor/blob/main/reasons.png?raw=true)
## Some Benefits of Employee Retention within an Organization
![img alt](https://github.com/Tridibesh-033/Employee_Retention_Predictor/blob/main/benefits.png?raw=true)

## Some exploratory data analysis to figure out which variables have direct and clear impact on employee retention
Plot bar charts showing impact of employee salaries on retention
![img alt](https://github.com/Tridibesh-033/Employee_Retention_Predictor/blob/main/output.png?raw=true)

Plot bar charts showing corelation between department and employee retention
![img alt](https://github.com/Tridibesh-033/Employee_Retention_Predictor/blob/main/output_1.png?raw=true)

### Built using **Pandas, Scikit-learn, Random Forest**, and **Streamlit**.

## 📌 Features
- 🔍 Predicts employee retention using historical HR data
- 📊 Visual insights using salary and department-based retention analysis
- 🧪 Trained using Random Forest Classifier (91.3% accuracy)
- 🌐 Interactive web app using Streamlit
- 💾 Model serialization using Pickle

## 🛠️ Tech Stack
### Tool/Library
- Python           
- Pandas           
- Matplotlib       
- Scikit-learn     
- Streamlit        
        
## 📁 Project Structure
<img width="280" height="123" alt="{E62A8983-5B01-4E45-BFC9-A99AD76AE14E}" src="https://github.com/user-attachments/assets/ce104c43-f32b-44e9-b819-bb74307e75f5" />

## 🚀 Getting Started
### 🔧 Prerequisites
- Python 3.8 or above

## 📦 Installation
- git clone https://github.com/Tridibesh-033/Employee_Retention_Predictor.git
- cd Employee_Retention_Predictor
- pip install -r requirements.txt

## Run the web app:
streamlit emp_retention_UI.py

### Streamlit User Application 
![img alt](https://github.com/Tridibesh-033/Employee_Retention_Predictor/blob/main/Screenshot%20(212).png?raw=true)

#### Enter values for:
1. Satisfaction level
2. Average monthly hours
3. Promotion in last 5 years
4. Salary level (Low, Medium, High)

### Click on "Predict" to get the result:
#### ✅ The Employee will Stay
![img alt](https://github.com/Tridibesh-033/Employee_Retention_Predictor/blob/main/Screenshot%202024-12-13%20231546.png?raw=true)
#### ❌ The Employee will Leave
![img alt](https://github.com/Tridibesh-033/Employee_Retention_Predictor/blob/main/Screenshot%202024-12-13%20231437.png?raw=true)

## 📊 Model Training Summary
1. Dataset: 14,999 employee records from HR_comma_sep.csv
2. Model: RandomForestClassifier (sklearn)
3. Accuracy: 91.3% on test data
4. Features Used: Satisfaction level || Average monthly hours || Promotion in last 5 years || Salary category (one-hot encoded)

## 🧠 Future Improvements
1. Add more HR factors like number of projects, time at company, etc.
2. Deploy online using Streamlit Cloud or Heroku
3. Enable batch predictions via CSV upload

## 📬 Contact
- Tridibesh Debnath
- 📧 tridibeshdebnath@gmail.com
- Linkedin: https://www.linkedin.com/in/tridibesh-debnath-46b37924a/
