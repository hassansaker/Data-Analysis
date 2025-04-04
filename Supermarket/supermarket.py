# Step 1: Load necessary libraries import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
# Step 2: Load the dataset
data = pd.read_csv("supermarket_sales.csv")
# Step 3: Check for missing values
missing_values = data.isnull().sum()
# Step 4: Drop rows with missing 'Data' or 'Time'
# Missing values typically occur due to missleading in the...
# writting data ot forget the precise data or when it happen
cleaned_data = data.dropna (subset=["Date", "Time"])
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
q1_1_avg = cleaned_data["gross income"].mean() 
q1_1_min=cleaned_data["gross income"].min() 
q1_1_max = cleaned_data["gross income"].max()
q1_2_avg = cleaned_data["gross margin percentage"].mean() 
q1_2_min=cleaned_data["gross margin percentage"].min() 
q1_2_max = cleaned_data["gross margin percentage"].max()
print(f"Average Growth Rate: {q1_1_avg}") 
print(f"Minimum Growth Rate: {q1_1_min}") 
print(f"Maximum Growth Rate: {q1_1_max}")
print(f"Average Growth Rate: {q1_2_avg}") 
print(f"Minimum Growth Rate: {q1_2_min}") 
print(f"Maximum Growth Rate: {q1_2_max}")

# Question 2
# Transactions by Gender
q2=cleaned_data['Gender'].value_counts()
print(f"\nThe number of Male and Female is: {q2.to_string()}") 

# Question 3
# Revenue per Branch
q3=cleaned_data.groupby('Branch')['Total'].sum()
print(f"\nTotal Revenue by Branch: {q3.to_string()}")

# Question 4 
# Group transactions by product line and calculate the average sales per category.
q4 = cleaned_data.groupby('Product line')['Total'].mean()
print(f"\nAverage Sales by Product Line: {q4.to_string()}")

# Question 5
# Sort the sales data in descending order based on the total amount the costumor spents.
q5 = cleaned_data.sort_values('Total', ascending=False)
print("\nSales Sorted by Total Amount (Descending Order):")
print(q5[['Invoice ID', 'Total']].head())

# Question 6
# Determine the most common payment method used by customers.
q6 = cleaned_data['Payment'].value_counts()
print(f"\nMost Common Payment Method: {q6.to_string()}")
print(f"Most common payment method: {q6.idxmax()}")

# Question 7
# print the top 5 most frequently purchased in product lines.
q7 = cleaned_data['Product line'].value_counts().head(5)
print(f"\nTop 5 Most Frequently Purchased Product Lines: {q7.to_string()} \n")

# Question 8 
# Visualize the total sales distribution across different branches using bar chart.
plt.figure(figsize=(8, 5))
q3.plot(kind='bar', color=['blue', 'red', 'green'])
plt.title('Total Sales by Branch')
plt.xlabel('Branch')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('branch_sales.png')
plt.show()

# Question 9
# Create a pie chart showing the proportion of each customer type (Member vs. Normal).
plt.figure(figsize=(8, 5))
customer_counts = cleaned_data['Customer type'].value_counts()
customer_counts.plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'lightcoral'])
plt.title('Customer Type Distribution')
plt.ylabel('')
plt.tight_layout()
plt.savefig('customer_types.png')
plt.show()

# Question 10
# Create plot chart to analyze sales trends over time.

# First, convert date column to datetime and set as index
cleaned_data['Date'] = pd.to_datetime(cleaned_data['Date'])
cleaned_data.set_index('Date', inplace=True)

# Resample by day and calculate total sales
daily_sales = cleaned_data['Total'].resample('D').sum()

plt.figure(figsize=(10, 5))
daily_sales.plot(kind='line', color='teal')
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.tight_layout()
plt.savefig('sales_trend.png')
plt.show()