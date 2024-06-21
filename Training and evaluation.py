import os
from glob import glob
import matplotlib.pyplot as plt
import pandas as pd

# Define the folder path
folderpath = r"C:\Users\tessel.kaal\OneDrive - Accenture\Thesis\Output training model\VERSION 5\VERSION 5.1\SCENARIO5\0620_100_40_Scenario5.3_new"

# Search for CSV files with "training" and "evaluation" in their names
training_data_files = glob(os.path.join(folderpath, '*training_rewards*.csv'))
evaluation_data_files = glob(os.path.join(folderpath, '*output_rewards_evaluation*.csv'))

# Ensure that at least one training and one evaluation CSV file are found
if len(training_data_files) < 1 or len(evaluation_data_files) < 1:
    raise FileNotFoundError("Not enough training or evaluation CSV files found in the folder.")

# Read the training and evaluation data
training_data_csv = pd.concat([pd.read_csv(f) for f in training_data_files], ignore_index=True)
evaluation_data_csv = pd.concat([pd.read_csv(f) for f in evaluation_data_files], ignore_index=True)

# Extract the second column (assuming it's the relevant data)
training_rewards = training_data_csv.iloc[:, 1]
evaluation_rewards = evaluation_data_csv.iloc[:, 1]

# Concatenate the training and evaluation data
concatenated_rewards = pd.concat([training_rewards, evaluation_rewards], ignore_index=True)

# Plot the concatenated graph using matplotlib
plt.figure(figsize=(12, 6))
plt.plot(concatenated_rewards[:100], label='Training Data', color='blue')
plt.plot(range(100, 140), concatenated_rewards[100:140], label='Evaluation Data', color='red')
plt.xlabel('Episodes')
plt.ylabel('Rewards')
plt.title('Concatenated Training and Evaluation Rewards Over 140 Episodes')
plt.legend()
plt.grid(True)

# Save plot if an output path is provided
output_path = input("Enter the filename to save the plot (leave blank to skip saving): ")
if output_path:
    output = os.path.join(r"C:\Users\tessel.kaal\OneDrive - Accenture\Thesis\Output training model\VERSION 5\VERSION 5.1\Concatenatedgraphs\\", f"{output_path}.png")
    plt.savefig(output, bbox_inches='tight')
    print(f"Plot saved as {output}")
else:
    print("No output path provided. Plot not saved.")

# Display the plot
plt.show()
