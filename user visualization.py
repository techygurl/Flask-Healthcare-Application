
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  using seaborn style for better visuals
sns.set(style="whitegrid")


# In[2]:


df = pd.read_csv(r"C:\Users\Varnosafety INT\Downloads\user.csv")


# In[3]:


df.head(20)


# In[4]:


top_ages_income = df.groupby('Age')['Total Income'].mean().sort_values(ascending=False).head(10)


# In[5]:


plt.figure(figsize=(10, 6))
sns.barplot(x=top_ages_income.index, y=top_ages_income.values, palette="viridis")
plt.title('Top 10 Ages with Highest Average Income')
plt.xlabel('Age')
plt.ylabel('Average Income')
plt.tight_layout()
plt.savefig('top_ages_income.png')  # Exported for PowerPoint
plt.show()


# In[6]:


spending_columns = ['Utilities', 'Entertainment', 'School_fees', 'Shopping', 'Healthcare']
df_spending = df[['Gender'] + spending_columns]


# In[10]:


df_melted = pd.melt(df_spending, id_vars='Gender', var_name='Spending Category', value_name='Amount')

plt.figure(figsize=(12, 6))
sns.boxplot(
    data=df_melted,
    x='Spending Category',
    y='Amount',
    hue='Gender',
    palette={'Male': 'blue', 'Female': 'red'},
    showfliers=False  # hiding extreme outliers for clarity
)
plt.title('Gender Distribution Across Spending Categories')
plt.ylabel('Amount Spent')
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig('gender_spending_distribution_fixed.png')
plt.show()

