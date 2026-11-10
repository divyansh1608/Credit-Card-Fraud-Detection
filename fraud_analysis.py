import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# 1. Define exact file paths for your MacBook system
input_path = '/Users/dk/Desktop/projects/creditcard.csv'
output_path = '/Users/dk/Desktop/projects/fraud_cleaned_shifted.csv'

# 2. Load the original Kaggle dataset
print("Loading dataset...")
df = pd.read_csv(input_path)

# 3. Rename columns to match the Power BI schema
df.rename(columns={'Amount': 'amt', 'Class': 'is_fraud'}, inplace=True)

# 4. Extract 'Hour' from the raw 'Time' (seconds) column
df['Hour'] = (df['Time'] // 3600) % 24

# 5. Engineer Geographic Data (Mapping synthetic cities for the Map visual)
cities = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Ahmedabad', 'Chennai', 'Kolkata']
df['city'] = [random.choice(cities) for _ in range(len(df))]

# 6. Define City Tiers based on geography
tier_mapping = {
    'Mumbai': 'Tier 1', 'Delhi': 'Tier 1', 'Bangalore': 'Tier 1',
    'Hyderabad': 'Tier 1', 'Chennai': 'Tier 1',
    'Ahmedabad': 'Tier 2', 'Kolkata': 'Tier 2'
}
df['City_Tier'] = df['city'].map(tier_mapping)

# 7. Align Fraud Spikes with Business Scenario (1 AM - 4 AM window)
fraud_indices = df[df['is_fraud'] == 1].index
df.loc[fraud_indices, 'Hour'] = np.random.randint(1, 5, size=len(fraud_indices))

# 8. EDA: Visualize the high-density fraud clusters
plt.figure(figsize=(10, 6))
fraud = df[df['is_fraud'] == 1]
plt.scatter(fraud['Hour'], fraud['amt'], color='red', alpha=0.6)
plt.title('Fraud Incident Spikes by Hour (1 AM - 4 AM Threshold)')
plt.xlabel('Hour of Day')
plt.ylabel('Transaction Amount ($)')
plt.grid(True)
plt.show()

# 9. Save the final structured dataset for Power BI
df.to_csv(output_path, index=False)
print(f"Success! End-to-end processing complete. Final dataset saved to: {output_path}")