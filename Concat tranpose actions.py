import os
from glob import glob
import matplotlib.pyplot as plt
import pandas as pd

# Define the folder path
folderpath = r"C:\Users\tessel.kaal\OneDrive - Accenture\Thesis\Output training model\VERSION 5\VERSION 5.1\SCENARIO5\trial_26"

# Search for CSV files with "training" and "evaluation" in their names
action_data_files = glob(os.path.join(folderpath, '*actions*.csv'))

# Ensure that at least one training and one evaluation CSV file are found
if len(action_data_files) < 1:
    raise FileNotFoundError("Not enough CSV files found in the folder.")

# Read the training and evaluation data
action_data_csv = pd.concat([pd.read_csv(f) for f in action_data_files], ignore_index=True)


# Extract the second column (assuming it's the relevant data)
action_rewards = action_data_csv.iloc[:, 1]

# Concatenate the training and evaluation data
concatenated_rewards = pd.concat([action_rewards], ignore_index=True)


print(concatenated_rewards)

# Plot the concatenated graph using matplotlib
plt.figure(figsize=(12, 6))
plt.plot(concatenated_rewards, label='Action Data', color='blue')
plt.xlabel('Steps')
plt.ylabel('Action')
plt.title('Concatenated Evaluation Rewards Over 3840 steps, being 40 episodes')
plt.legend()
plt.grid(True)