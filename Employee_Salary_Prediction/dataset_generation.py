# Synthetic dataset means it is an artificial dataset that looks realistic and useful for machine learning pratices and no privacy isuues

# Loading the libraries that are required
import pandas as pd
import numpy as np
import random

np.random.seed(42) # seed() helps to keep the generated random values same every time we execute

n=2000 # n is the total number of records of data

# Initializing some categorical values
education_levels = ["Bachelor's", "Master's", "PhD"]
job_roles = ["Developer", "Data Analyst", "Manager", "Designer", "Tester"]
company_types = ["Startup", "MNC", "Medium Scale"]
genders = ["Male", "Female"]

# The rows which are going to be generated will be stored in the below list
data=[]

for i in range(n):
    age = np.random.randint(21, 60) # selects the age randomly between 21 to 60
    gender=np.random.choice(genders) # selects male or female
    experience = np.random.randint(0, 20) # selects experience randomly between 0 to 20 years
    education = random.choice(education_levels) # selects education from the above initialized educational levels
    job_role = random.choice(job_roles) # selects job role from the above initialized job roles
    company = random.choice(company_types) # selets company types
    skills_score = np.random.randint(1, 11) # gives skills score based thier technical and non technical skills
    certifications = np.random.randint(0, 11) # gives random number of certifications that are done
    work_hours = np.random.randint(30, 60) # selects work hours per week between 30 to 60
    
    base_salary=300000 #initializing base salary to 300000 

    # formula for generating salary
    # salary is based on experience,skills score,certifications
    salary = (
    base_salary
    + (experience * 50000) #experience * 50000 rupees 
    + (skills_score * 15000)#skills_score * 15000 rupees
    + (certifications * 10000)#number of certifications * 10000 rupees
    )

    #eduction impact
    if education == "Master's":
        salary += 100000
    elif education == "PhD":
        salary += 200000

    #job role impact
    if job_role == "Manager":
        salary += 250000
    elif job_role == "Developer":
        salary += 150000
    elif job_role == "Data Analyst":
        salary += 120000
    elif job_role == "Designer":
        salary += 80000
    elif job_role == "Tester":
        salary += 70000

    #company type impact
    if company == "MNC":
        salary += 200000
    elif company == "Startup":
        salary += 50000
    elif company == "Medium Scale":
        salary += 100000
    
    # Work Hours Bonus
    salary += work_hours * 1000

    #adding some noise because in real life two people having same experience can have different salaries and to make the data more realistic
    salary += np.random.randint(-50000, 50000) 

    #each employee row is added to the data
    data.append([
    i + 1,
    age,
    gender,
    education,
    experience,
    job_role,
    skills_score,
    certifications,
    company,
    work_hours,
    salary
    ])

# these are the columns that are mentioned to create 
columns = [
    "EmployeeID",
    "Age",
    "Gender",
    "EducationLevel",
    "YearsOfExperience",
    "JobRole",
    "SkillsScore",
    "Certifications",
    "CompanyType",
    "WorkHoursPerWeek",
    "Salary"
]

# this step helps to convert the data into a dataframe i.e., in table format
df = pd.DataFrame(data, columns=columns)

# converts the generated dataframe into a csv file which helps to do further steps
df.to_csv("employee_salary_dataset.csv", index=False)

print("Dataset Generated Successfully!")
print(df.head()) # prints the starting 5 rows