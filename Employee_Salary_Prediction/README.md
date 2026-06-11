Employee Salary Prediction System
Project Overview
The Employee Salary Prediction System is a Machine Learning project that predicts an employee's annual salary based on their personal details, skills, experience, and work environment.
This project demonstrates a complete end-to-end ML workflow including:

Synthetic Dataset Generation
Data Preprocessing
Exploratory Data Analysis (EDA)
Data Visualization
Machine Learning Model Training
Model Evaluation
Console-Based Salary Prediction System


Dataset Features
The dataset contains 2000 records with the following features:
FeatureDescriptionEmployeeIDUnique identifier for each employeeAgeAge of the employee (21–60)GenderGender of the employee (Male / Female)EducationLevelHighest education level (Bachelor's / Master's / PhD)YearsOfExperienceTotal years of work experience (0–20)JobRoleJob designation (Developer / Data Analyst / Manager / Designer / Tester)SkillsScoreTechnical and non-technical skills score (1–10)CertificationsNumber of certifications completed (0–10)CompanyTypeType of company (Startup / MNC / Medium Scale)WorkHoursPerWeekWeekly working hours (30–60)SalaryTarget variable — Annual salary in ₹

Technologies Used

Python — Core programming language
Pandas — Data manipulation and analysis
NumPy — Numerical computations
Matplotlib — Data visualization
Seaborn — Statistical data visualization
Scikit-learn — Machine learning models and evaluation
VS Code — Development environment


Project Workflow

Synthetic dataset generation (dataset_generation.py)
Data loading and inspection
Handling missing values and duplicates
Data validation (negative salaries, invalid ages, invalid work hours)
Categorical feature encoding using Label Encoding
Feature scaling using Standard Scaler
Exploratory Data Analysis
Data visualization
Train-test split (80% train / 20% test)
Machine learning model training
Model evaluation
Console-based salary prediction system


Visualizations Included

Scatter Plot — Experience vs Salary
Box Plot — Salary Distribution by Education Level
Bar Chart — Average Salary by Job Role
Histogram — Salary Distribution
Correlation Heatmap — Feature Relationships


Machine Learning Models Used
ModelTypeLinear RegressionRegressionDecision Tree RegressorRegressionRandom Forest RegressorRegression (100 estimators)

Model Evaluation Metrics

MAE (Mean Absolute Error)
RMSE (Root Mean Squared Error)
R² Score (Coefficient of Determination)


How to Run the Project
Step 1: Install Required Libraries
bashpip install pandas numpy matplotlib seaborn scikit-learn
Step 2: Generate the Dataset
bashpython dataset_generation.py
This generates employee_salary_dataset.csv with 2000 synthetic employee records.
Step 3: Open and Run the Notebook
bashjupyter notebook salary_prediction_model.ipynb
Run all cells sequentially. The notebook covers:

Preprocessing
EDA
Visualization
Model Training & Evaluation
Prediction System

Step 4: Use the Prediction System
At the end of the notebook, a console-based prediction system will prompt you to enter:
Enter Age:
Enter Gender (Male/Female):
Enter Education Level (Bachelor's/Master's/PhD):
Enter Years of Experience:
Enter Skills Score (1-10):
Enter Number of Certifications:
Enter Job Role (Developer/Data Analyst/Manager/Designer/Tester):
Enter Company Type (Startup/MNC/Medium Scale):
Enter Work Hours Per Week:
Output:
------------------------------------
 PREDICTED EMPLOYEE SALARY
------------------------------------

Estimated Annual Salary: ₹X,XX,XXX.XX

Project Structure
Employee_Salary_Prediction/
│
├── dataset_generation.py              # Synthetic dataset generation script
├── employee_salary_dataset.csv        # Generated raw dataset (2000 records)
├── preprocessed_employee_salary_dataset.csv  # Cleaned and encoded dataset
└── salary_prediction_model.ipynb      # Main notebook (preprocessing → prediction)

Key Insights

Employees with more years of experience earn significantly higher salaries.
PhD holders earn more on average compared to Bachelor's and Master's graduates.
Managers have the highest average salary among all job roles.
MNC employees are better paid than Startup and Medium Scale employees.
Higher skills score and more certifications positively impact salary.


Future Improvements

Streamlit Web Application for user-friendly salary prediction
Hyperparameter tuning for improved model accuracy
Feature importance analysis and visualization
Model deployment using Flask or FastAPI
Cross-validation for more robust evaluation


👩‍💻 Author
Vakiti Hansika Reddy