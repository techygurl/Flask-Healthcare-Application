# Flask App - User Healthcare Application

This project processes and visualizes user spending data by gender and category using MongoDB and Python.

## link to deployed flask app
http://51.20.185.107/


## Features

- Connects to a local MongoDB database to retrieve survey data.
- Converts user data into a structured CSV file (`user.csv`).
- Visualizes average income by age and spending behavior by gender.
- Outputs high-quality visualizations suitable for presentation.


## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/flask-app.git
cd flask-app
2. Set Up Virtual Environment (Optional)
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Required Packages
bash
Copy
Edit
pip install pymongo pandas matplotlib seaborn
4. Configure MongoDB
Ensure your MongoDB server is running locally and has a database named survey_db with a participants collection containing documents like:

json
Copy
Edit
{
  "age": 30,
  "gender": "Male",
  "total_income": 50000,
  "total_expense": 20000,
  "expenses": {
    "utilities": 100,
    "entertainment": 150,
    "school_fees": 300,
    "shopping": 200,
    "healthcare": 250
  }
}
5. Run the Scripts
Extract and save data to CSV:

bash
Copy
Edit
python USER.py
Generate visualizations:

bash
Copy
Edit
python "user visualization.py"
Output
top_ages_income.png: Bar chart of top 10 ages by average income.

gender_spending_distribution_fixed.png: Boxplot comparing spending categories by gender.

