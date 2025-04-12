# Step 1: Load necessary libraries import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
# Step 2: Load the dataset
data = pd.read_csv("player_stats.csv")
# Step 3: Check for missing values
missing_values = data.isnull().sum()
# Step 4: Drop rows with missing "team" or "player"
# Missing values typically occur in the Column [team,player]
cleaned_data = data.dropna (subset=["team","player"])
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
# What are the average,max and min goals and assists?
g_mean = cleaned_data["goals"].mean() 
g_min=cleaned_data["goals"].min() 
g_max = cleaned_data["goals"].max()
as_avg = cleaned_data["assists"].mean() 
as_min=cleaned_data["assists"].min() 
as_max = cleaned_data["assists"].max()
print('')
print(f"Average goals: {g_mean}") 
print(f"Minimum goals: {g_min}") 
print(f"Maximum goals: {g_max}")
print(f"Average assists: {as_avg}") 
print(f"Minimum assists: {as_min}") 
print(f"Maximum assists: {as_max}")

# Question2
# Which defenders (DF) scored at least 1 goal?
DF = cleaned_data[(cleaned_data['position'] == 'DF') & (cleaned_data['goals'] >= 1)]
print(f"\nThe number of defenders scored at least 1 goal: {len(DF)}")
print(DF[['player','position','goals']].head(10))

# Question 3
# List midfielders (MF) who played over 500 minutes and provided at least 1 assist.
MF = cleaned_data[(cleaned_data['position'] == 'MF') & (cleaned_data['minutes'] > 500) & (cleaned_data['assists'] >= 1)]
print(f"The number of midfielders who played over 500 minutes and provided at least 1 assist: {len(MF)}")
print(MF[['player','position','minutes']].head(10))

# Question 4
# Which teams had the highest average player age?
cleaned_data['age'] = cleaned_data['age'].str.split('-').str[0].astype(int)
high_team=cleaned_data.groupby('team')['age'].mean().sort_values(ascending=False)
print("\nTop 10 Teams with highest average player age:")
print(high_team.head(10))

# Question 5 
# Who are the top 10 players with the most minutes played?
top_pl=cleaned_data.sort_values('minutes',ascending=False)
print("top 10 players with the most minutes played:")
print(top_pl[['player','minutes']].head(10))

# Question 6
# Which young players (age ≤ 23) scored more than 1 goal? Group by position.
young_pl=cleaned_data[cleaned_data['goals'] > 1]
young_pl = young_pl.sort_values('age').groupby('position')
print("Top 10 young players (age ≤ 23) scored more than 1 goal:")
print(young_pl[['player','position','age','goals']].head(10))


# Question 7
# Show the top 5 teams with the most goals by forwards (FW).
top_tm=cleaned_data[cleaned_data['position'] == 'FW'].groupby('team')['goals'].sum()
top_tm=top_tm.sort_values(ascending=False)
print("\ntop 5 teams with the most goals by forwards:")
print(top_tm.head(5))


# Question 8
# Bar Chart -Compare total goals by team 
cp_tm=cleaned_data.groupby('team')['goals'].sum()
cp_tm.plot(kind='bar', title='Total Goals by Team')
plt.ylabel('Gaols')
plt.show()

# Question 9
# Player distribution by position
pl_ds=cleaned_data['position'].value_counts()
pl_ds.plot(kind='pie', autopct='%1.1f%%',title='Player distribution by position')
plt.ylabel('')
plt.show()

# Question 10
# Relationship between age and goals.
cleaned_data.plot.scatter(x='age', y='goals', title='Age vs. Goals Scatter Plot')
plt.ylabel('Goals')
plt.xlabel('Age')
plt.show()




