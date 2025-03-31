# Step 1: Load necessary libraries import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
# Step 2: Load the dataset
data = pd.read_csv("Pokemon.csv")
# Step 3: Check for missing values
missing_values = data.isnull().sum()
# Step 4: Drop rows with missing 'Type 1' or 'Type 2'
# Missing values typically occur in the Column [Type 1,Type 2]
cleaned_data = data.dropna (subset=["Type 1", "Type 2"])
# Step 5: Drop duplicate rows if there any 
cleaned_data = cleaned_data.drop_duplicates()
# Step 6: Final check after cleaning 
final_missing = cleaned_data.isnull().sum() 
final_shape = cleaned_data.shape
# print("Final Missing Values:")
# print(final_missing)
# print("\nFinal Shape of cleaned Data:")
# print(final_shape)

# Question 1
q1_1_avg = cleaned_data["Attack"].mean() 
q1_1_min=cleaned_data["Attack"].min() 
q1_1_max = cleaned_data["Attack"].max()
q1_2_avg = cleaned_data["Speed"].mean() 
q1_2_min=cleaned_data["Speed"].min() 
q1_2_max = cleaned_data["Speed"].max()
print(f"Attack - Mean: {q1_1_avg}") 
print(f"Attack - Min: {q1_1_min}") 
print(f"Attack - Max: {q1_1_max}")
print(f"Speed - Mean: {q1_2_avg}") 
print(f"Speed - Min: {q1_2_min}") 
print(f"Speed - Max: {q1_2_max}")

# Question 2
# Find all Fire-type Pokémon with Attack > 100
q2=cleaned_data[(cleaned_data['Type 1'] == 'Fire') & (cleaned_data['Attack'] > 100)]
print(f"All Fire type Pokemon: \n{q2.to_string()}") 

# Question 3
# Identify Legendary Pokémon with Speed > 120.
q3 = cleaned_data[(cleaned_data['Legendary'] == True) & (cleaned_data['Speed'] > 120)]
print(f"All Legendary Pokemon with Speed > 120: \n{q3.to_string()}") 

# Question 4 
# Group by Type 1 and calculate average HP per type.
q4 = cleaned_data.groupby('Type 1')['HP'].mean()
print(f"\nAverage HP by {q4.to_string()}")

# Question 5
# Sort Pokémon by Total (sum of all stats) in descending order.
q5 = cleaned_data.sort_values('Total', ascending=False)
print("\nSort Pokemon by Total in descending order:")
print(q5[['Name','Total']].head(20))

# Question 6
# Find Water-type Pokémon with sp.Atk > 80, sorted by Defense.
q6 = cleaned_data[(cleaned_data['Type 1'] == "Water") & (cleaned_data['Sp. Atk'] > 80)]
q6= q6.sort_values('Defense', ascending=False)
print("Water-type Pokemon with sp.Atk > 80, sorted by Defense:")
print(q6[['Name','Defense', 'Sp. Atk']].head(20))


# Question 7
# Group by Generation and count Legendary Pokémon per generation.
q7 = cleaned_data[cleaned_data['Legendary'] == True]
q7 = q7.groupby('Generation')['Name'].count().reset_index(name='Legendary Count')
print(q7)

# Question 8 
# Bar chart of average Attack by Type 1.
plt.figure(figsize=(8, 5))
fig=cleaned_data.groupby('Type 1')['Attack'].mean()
fig.plot(kind='bar', title='Average Attack by Type', color='teal')
plt.ylabel('Attack')
plt.show()


# Question 9
#Pie chart showing distribution of Generation counts.
plt.figure(figsize=(8, 5))
fig=cleaned_data['Generation'].value_counts()
fig.plot(kind='pie',autopct='%1.1f%%', title='Distribution of Pokémon by Generation')
plt.ylabel('')
plt.tight_layout()
plt.show()

# Question 10
# Evolution of Combat Stats by Generation
plt.figure(figsize=(8, 5))
fig = cleaned_data.groupby('Generation')[['Attack', 'Defense', 'Speed']].mean()
plt.plot(fig.index, fig['Attack'], label='Attack', linewidth=3, color='red')
plt.plot(fig.index, fig['Defense'],label='Defense', linewidth=3, color='blue')
plt.plot(fig.index, fig['Speed'],label='Speed', linewidth=3, color='green')
plt.title('Average Combat Stats by Pokémon Generation')
plt.xlabel('Generation')
plt.ylabel('Average Stat Value')
plt.legend(title='Stat Type')
plt.tight_layout()
plt.show()