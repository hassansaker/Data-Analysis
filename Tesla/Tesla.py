# Step 1: Load necessary libraries import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
# Step 2: Load the dataset
data = pd.read_csv("Tesla-csv.csv")
# Step 3: Check for missing values
missing_values = data.isnull().sum()
# Step 4: Drop rows with missing "Volume"
# Missing values typically occur in the Column [Volume]
cleaned_data = data.dropna (subset=["Volume"])
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
# What are the minimum, maximum, and mean closing prices and trading volumes for Tesla stock?
v_mean = cleaned_data["Volume"].mean() 
v_min=cleaned_data["Volume"].min() 
v_max = cleaned_data["Volume"].max()
c_avg = cleaned_data["Close"].mean() 
c_min=cleaned_data["Close"].min() 
c_max = cleaned_data["Close"].max()
print(f"Volume - Mean: {v_mean}") 
print(f"Volume - Min: {v_min}") 
print(f"Volume - Max: {v_max}")
print(f"Close price - Mean: {c_avg}") 
print(f"Close price - Min: {c_min}") 
print(f"Close price - Max: {c_max}")

# Question2
# How many days did Tesla's stock volume exceed 20 million
vol_days = cleaned_data[cleaned_data['Volume'] > 2e7]
print(f"\nThe number of Days with Volume greater than 20M: {len(vol_days)}")
print(vol_days[['Date','Volume']].head(10))

# Question 3
# How many days where closing price > opening price?
excess = cleaned_data[(cleaned_data['Close'] > cleaned_data['Open'] )]
print(f"The number of Days with Price Increase: {len(excess['Date'])}")
print(excess[['Date','Open','Close']].head(10))

# Question 4
# What is the average annual closing price from 2010 to 2023?
# Convert 'Date' to datetime format and extract Year
cleaned_data['Date'] = pd.to_datetime(cleaned_data['Date'])
cleaned_data['Year'] = cleaned_data['Date'].dt.year
annual_avg = cleaned_data.groupby('Year')['Close'].mean()
print("\nAnnual Average Closing Price is:")
print(annual_avg)

# Question 5 
# Which dates recorded the highest and lowest trading volumes for Tesla?
vol_asc = cleaned_data.sort_values('Volume')
vol_desc = cleaned_data.sort_values('Volume', ascending=False)
print("Lowest Volume Dates:")
print(vol_asc[['Date','Volume']].head(5))
print("\nHighest Volume Dates:")
print(vol_desc[['Date','Volume']].head(5))

# Question 6
# Which days had the most significant price swings? How did the trading volume behave on these days?
# Filter rows with high Volatility (High - Low > 1)
high_swings = cleaned_data[cleaned_data['High'] - cleaned_data['Low'] > 1]
sorted = high_swings.sort_values('Volume', ascending=False)
print("Top 10 High Volatility Days:")
print(sorted[['Date','High','Low','Volume']].head(10))


# Question 7
# Which months recorded the highest number of high-volatility trading days?
# Convert 'Date' to datetime format and extract Month
cleaned_data['Date'] = pd.to_datetime(cleaned_data['Date'])
cleaned_data['Month'] = cleaned_data['Date'].dt.month
volatile_months = cleaned_data.groupby('Month').size()
# Sort months by volatility count in descending order
sorted_months = volatile_months.sort_values(ascending=False)
print("\nMost Volatile Months:")
print(sorted_months)


# Question 8
# Bar Chart - Annual Trading Volume
annual_volume = cleaned_data.groupby('Year')['Volume'].mean()
annual_volume.plot(kind='bar', color='indigo', title="Annual Average Trading Volume")
plt.ylabel('Volume')
plt.show()

# Question 9
# TesLa High Prices Over Time
plt.figure()
plt.plot(cleaned_data['Date'], cleaned_data['High'], color='red')
plt.xlabel('Date')
plt.ylabel('High')
plt.title('TESLA High Prices Over Time')
plt.show()

# Question 10
# optimistic Days by Year 
cleaned_data['Gain_Day'] = cleaned_data['Close'] > cleaned_data['Open']
yearly_gains = cleaned_data.groupby('Year')['Gain_Day'].mean() * 100
yearly_gains.plot(kind='pie', autopct='%1.1f%%',title='optimistic Days by Year')
plt.ylabel('')
plt.show()




