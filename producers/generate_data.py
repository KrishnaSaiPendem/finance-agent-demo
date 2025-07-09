import os
import random
import pandas as pd
from datetime import datetime, timedelta

os.makedirs("data", exist_ok=True)

user_ids = [f"u{i}" for i in range(1, 21)]
merchants = [
    "Starbucks","Whole Foods","Shell","Amazon","Apple","Walmart",
    "Uber","Lyft","McDonald's","Target","Costco","ExxonMobil",
    "Best Buy","Home Depot","Nike","Delta","Southwest","CVS","Walgreens","Trader Joe's"
]
categories = {
    "Starbucks":"dining","McDonald's":"dining",
    "Whole Foods":"groceries","Trader Joe's":"groceries","Walmart":"groceries",
    "Costco":"shopping","Target":"shopping","Amazon":"shopping","Best Buy":"tech","Apple":"tech",
    "Shell":"gas","ExxonMobil":"gas",
    "Uber":"transport","Lyft":"transport",
    "Home Depot":"home_improvement","Nike":"apparel",
    "Delta":"travel","Southwest":"travel",
    "CVS":"pharmacy","Walgreens":"pharmacy"
}

rows = []
start = datetime(2025,1,1)
for _ in range(1000):
    uid = random.choice(user_ids)
    date = (start + timedelta(days=random.randint(0,180))).strftime("%Y-%m-%d")
    m = random.choice(merchants)
    rows.append({
        "user_id": uid,
        "date": date,
        "amount": round(random.uniform(5,500),2),
        "merchant": m,
        "category": categories[m]
    })

pd.DataFrame(rows).to_csv("data/transactions.csv", index=False)
print("Generated data/transactions.csv with 1000 rows")
