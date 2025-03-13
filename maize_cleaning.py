import pandas as pd

# Loading datasets
production_data = pd.read_csv("most_cleaned_production_data.csv")
price_data = pd.read_csv("most_cleaned_price_data.csv")

# Print datasets
print(production_data.head())
print(price_data.head())


# Check for missing values
print(production_data.isnull().sum())
print(price_data.isnull().sum())


# I will drop the 'Note' column because its the one having missing values and is not useful for my analysis
production_data_clean = production_data.drop(columns=['Note'])

# I will verify that the column is dropped
print(production_data_clean.head())


# The next is, I will check for duplicates in the two datasets
print("Duplicates in Production Data:", production_data_clean.duplicated().sum())
print("Duplicates in Price Data:", price_data.duplicated().sum())   # From the output it shows I dont have any duplicate. So I will proceed with my cleaning


# Converting data types
production_data_clean['Year'] = pd.to_numeric(production_data_clean['Year'], errors='coerce')
production_data_clean['Value'] = pd.to_numeric(production_data_clean['Value'], errors='coerce')
price_data['Year'] = pd.to_numeric(price_data['Year'], errors='coerce')
price_data['Value'] = pd.to_numeric(price_data['Value'], errors='coerce')

# Verifying data types
print("Production Data Types after conversion:\n", production_data_clean.dtypes)
print("Price Data Types after conversion:\n", price_data.dtypes)

# Making text standard
production_data_clean['Area'] = production_data_clean['Area'].str.lower()
production_data_clean['Element'] = production_data_clean['Element'].str.lower()
production_data_clean['Area'] = production_data_clean['Area'].str.strip()
production_data_clean['Element'] = production_data_clean['Element'].str.strip()

price_data['Area'] = price_data['Area'].str.lower()
price_data['Element'] = price_data['Element'].str.lower()
price_data['Area'] = price_data['Area'].str.strip()
price_data['Element'] = price_data['Element'].str.strip()

# Let's fix typos
production_data_clean['Area'] = production_data_clean['Area'].replace('nigeria', 'Nigeria')
price_data['Area'] = price_data['Area'].replace('nigeria', 'Nigeria')

# Now let's verify the consistency of those text
print("Unique Areas:", production_data_clean['Area'].unique())
print("Unique Elements:", production_data_clean['Element'].unique())
print("Unique Areas:", price_data['Area'].unique())
print("Unique Elements:", price_data['Element'].unique())


# Let's merge the datasets on 'Year' and  save
agriculture_datasets = pd.merge(production_data_clean, price_data, on='Year', how='outer')
agriculture_datasets.to_csv("cleaned_agriculture_datasets", index=False)



