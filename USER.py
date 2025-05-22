


# In[2]:


get_ipython().system('pip install pymongo')


# In[5]:


from pymongo import MongoClient
import pandas as pd

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client['survey_db']
collection = db['participants']

# Fetch all documents
data = list(collection.find())

#  remove MongoDB internal ID 
for d in data:
    d.pop('_id', None)

# Converting to DataFrame
df = pd.DataFrame(data)

# Show the first few records
print(df.head())


# In[7]:


import csv

class User:
    def __init__(self, age, gender, income, expenses, total_expense):
        self.age = age
        self.gender = gender
        self.income = income
        self.expenses = expenses
        self.total_expense = total_expense

    def to_row(self):
        row = {
            'Age': self.age,
            'Gender': self.gender,
            'Total Income': self.income,
            'Total Expense': self.total_expense
        }
        for category in ['utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']:
            row[category.capitalize()] = self.expenses.get(category, 0.0)
        return row


# In[12]:


client = MongoClient("mongodb://localhost:27017")
db = client['survey_db']
collection = db['participants']

users = []
for doc in collection.find():
    user = User(
        age=doc['age'],
        gender=doc['gender'],
        income=doc['total_income'],
        expenses=doc['expenses'],
        total_expense=doc['total_expense']
    )
    users.append(user)

print(f"{len(users)} users loaded.")


# In[14]:


csv_file = 'user.csv'
with open(csv_file, 'w', newline='') as file:
    fieldnames = ['Age', 'Gender', 'Total Income', 'Total Expense', 'Utilities', 'Entertainment', 'School_fees', 'Shopping', 'Healthcare']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for user in users:
        writer.writerow(user.to_row())

print(f"CSV saved to {csv_file}")

