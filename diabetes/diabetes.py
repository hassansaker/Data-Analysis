# Step 1: Load necessary libraries import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
# Step 2: Load the dataset
data = pd.read_csv("diabetes.csv")
# Step 3: Check for missing values
missing_values = data.isnull().sum()
# Step 4: Drop rows with missing "Outcome"
# Missing values typically occur in the Column [Outcome]
cleaned_data = data.dropna (subset=["Outcome"])
# Step 5: Drop duplicate rows if there any 
cleaned_data = cleaned_data.drop_duplicates()
# Step 6: Final check after cleaning 
final_missing = cleaned_data.isnull().sum() 
final_shape = cleaned_data.shape
print("Final Missing Values:")
print(final_missing)
print("\nFinal Shape of cleaned Data:")
print(final_shape)



# Question 1
# Mean ,Min and Max  of BloodPressure and Glucose
BP_mean = cleaned_data["BloodPressure"].mean() 
BP_min=cleaned_data["BloodPressure"].min() 
BP_max = cleaned_data["BloodPressure"].max()
Gl_avg = cleaned_data["Glucose"].mean() 
Gl_min=cleaned_data["Glucose"].min() 
Gl_max = cleaned_data["Glucose"].max()
print(f"BloodPressure - Mean: {BP_mean}") 
print(f"BloodPressure - Min: {BP_min}") 
print(f"BloodPressure - Max: {BP_max}")
print(f"Glucose - Mean: {Gl_avg}") 
print(f"Glucose - Min: {Gl_min}") 
print(f"Glucose - Max: {Gl_max}")


# Question2
# How many patients aged over 50 with BMI > 30 have diabetes?
q2 = cleaned_data[(cleaned_data['Age'] > 50) & (cleaned_data['BMI'] > 30) & (cleaned_data['Outcome'] == 1)]
print(f"The number of Patients with age over 50 and with BMI over 30: {q2['Age'].count()}")
print(f"The top ten Patients are: \n {q2[['BMI','Age','Outcome']].head(10)}")

# Question 3
# What percentage of patients with Glucose > 140 and Blood Pressure > 90 are diabetic?
q3_total = cleaned_data[(cleaned_data['Glucose'] > 140) & (cleaned_data['BloodPressure'] > 90)]
q3 = q3_total[q3_total['Outcome'] == 1]
percentage = (len(q3)/len(q3_total)) * 100
print(f"\nThe percentage of patients with Glucose > 140 and Blood Pressure > 90 is: {percentage}")

# Question 4
# What is the average BMI for diabetic vs. non-diabetic patients?
q4 = cleaned_data.groupby(['Outcome'])['BMI'].mean()
print(f"Average BMI by Age Group and Diabetes Status :")
print(f"zero for non-diabetic and one for diabetic \n {q4}")

# Question 5
# Sort patients by Insulin level in descending order and display the top 10?
q5 = cleaned_data.sort_values('Insulin', ascending=False).head(10)
print('\nTop 10 Patients by Insulin Level:')
print(q5[['Age', 'Insulin', 'Outcome']])

# Question 6
# Filter patients with Pregnancies > 3, group by Outcome, and sort by average Glucose level?
q6 = cleaned_data[cleaned_data['Pregnancies'] > 3].groupby('Outcome')['Glucose'].mean()
q6=q6.sort_values(ascending=False)
print(f'Average Glucose of Patients with Pregnancies > 3:\n {q6}')


# Question 7
# Find the 10 youngest diabetic patients with BMI > 25 and display their Glucose levels?
q7 = cleaned_data[(cleaned_data['Outcome'] == 1) & (cleaned_data['BMI'] > 25)]
q7=q7.sort_values('Age').head(10)
print('Top 10 Young Diabetics (BMI>25)')
print(q7[['Age', 'BMI', 'Glucose']])


# Question 8
# Compare the average Glucose, BMI, and Blood Pressure between diabetic and non-diabetic
q8 = cleaned_data.groupby("Outcome")[['Glucose', 'BMI', 'BloodPressure']].mean()
q8.plot(kind='bar', title="Average Scores per Gender")
plt.xlabel("Outcome")
plt.ylabel("Average Score")
plt.show()

# Q9: Scatter Plot of Glucose vs BMI
cleaned_data.plot( kind='scatter', x='Glucose', y='BMI',c='Outcome' ,colormap='winter',title="Glucose vs BMI by Diabetes Status" )
plt.xlabel('Glucose Level')
plt.ylabel('Body Mass Index (BMI)')
plt.show()

# Question 10
# Analyze the proportion of diabetic vs. non-diabetic patients within different BMI categories
# Step 1: Create BMI categories (if not already done)
cleaned_data['BMI_Category'] = pd.cut(
    cleaned_data['BMI'],
    bins=[20, 30, 40, 50, 100],
    labels=['Underweight', 'Normal', 'Overweight', 'Obese']
)
# Step 2: Count diabetic patients per BMI category
diabetic_bmi_counts = cleaned_data[cleaned_data['Outcome'] == 1]['BMI_Category'].value_counts()
# Step 3: plotting
plt.pie(diabetic_bmi_counts,labels=diabetic_bmi_counts.index, autopct='%1.1f%%')
plt.title("Ethnicity Distribution")
plt.ylabel('')
plt.show()



