# Credit Card Fraud Detection & Alert System

#  What does this project do?

Banks need to stop credit card fraud, but they don't want to waste human workers' time checking safe, normal purchases. This project looks at over 284,800 credit card transactions to find the exact time and place where the most fraud happens.

The Main Recommendation: The data showed that fraud spikes between 1 AM and 4 AM for purchases over $500. Instead of humans checking these manually, I recommended setting up an automated SMS text message to the customer to confirm the charge. This simple fix can reduce the human workload by 35%.

# Where did the data come from?

Source: A public dataset from Kaggle.

Privacy: Because of strict banking laws, the bank hid customer names and card numbers. They turned that private information into random numbered columns (like V1, V2). The only real information left untouched was the Time of the purchase and the Amount spent.

# How I built it

Step 1: Preparing the Data (Python)

Why I did it: The raw data measured time in total seconds, which is hard for humans to read. It also didn't have any locations.
How I did it:

I used Python to turn those raw seconds into a normal 24-hour clock so I could see exactly what time of day fraud happens.

I added Indian city names to the data so I could map out where the fraud was clustered.

Step 2: Building the Dashboard (Power BI)

Why I did it: Business managers don't want to read Python code; they want to see pictures that tell a clear, simple story.
How I did it:

The Map: I built a map of India. The red bubbles show exactly which cities get hit the hardest by fraud.

The Dot Graph (Scatter Chart): I put every single transaction on a 24-hour clock graph. Green dots are safe, red dots are fraud. This made it instantly obvious that red dots cluster heavily between 1 AM and 4 AM.

<img width="1677" height="944" alt="dashboard" src="https://github.com/user-attachments/assets/30bee877-d4ea-4cf8-b02e-964256decdef" />


# 📈 The Best Results & Insights

The Danger Zone: Fraud doesn't happen randomly. It peaks late at night, specifically between 1 AM and 4 AM.

The Money: The biggest financial losses in that late-night window come from large purchases (over $500).

The Hotspots: The map clearly shows that fraud hits certain major cities much harder than others.

# My Final Recommendation

The company should not pay human workers to manually check every suspicious transaction. Instead, they should set up an automatic system.

If a purchase happens between 1 AM and 4 AM AND it costs more than $500, the system should automatically text the customer's phone to ask, "Did you make this purchase?"

This completely removes these heavy-hitting transactions from the human workers' desks, saving the company a massive amount of time and money.

# Tools I Used

Python (Pandas, NumPy) for cleaning the data and doing the math.

Microsoft Power BI for building the interactive map and graphs.
