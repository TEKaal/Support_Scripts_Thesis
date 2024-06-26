import os
from glob import glob
import pandas as pd

# Define the folder paths
folderpath = r"C:\Users\tessel.kaal\OneDrive - Accenture\Thesis\Output training model\VERSION 5\VERSION 5.1\SCENARIO4\0625_100_40_Scenario4.4"
folderpath_output = r"C:\Users\tessel.kaal\OneDrive - Accenture\Thesis\Output training model\Variability\Eval_only"

# Search for CSV files with "evaluation" in their names
evaluation_data_files = glob(os.path.join(folderpath, '*output_rewards_evaluation*.csv'))

# Ensure that at least one evaluation CSV file is found
if len(evaluation_data_files) < 1:
    raise FileNotFoundError("No evaluation CSV files found in the folder.")

# Read and concatenate the evaluation data
evaluation_data_csv = pd.concat([pd.read_csv(f) for f in evaluation_data_files], ignore_index=True)

# Extract the second column (assuming it's the relevant data)
evaluation_rewards = evaluation_data_csv.iloc[:, 1]

# Calculate statistics for evaluation data
mean_reward = evaluation_rewards.mean()
variance_reward = evaluation_rewards.var()
std_dev_reward = evaluation_rewards.std()

# Output the statistics
print(f"Mean Reward: {mean_reward}")
print(f"Variance of Reward: {variance_reward}")
print(f"Standard Deviation of Reward: {std_dev_reward}")

# Optionally save statistics to a file
output_stats_path = input("Enter the filename to save the statistics (leave blank to skip saving): ")
if output_stats_path:
    stats_output = os.path.join(folderpath_output, f"{output_stats_path}.txt")
    with open(stats_output, 'w') as f:
        f.write(f"Mean Reward: {mean_reward}\n")
        f.write(f"Variance of Reward: {variance_reward}\n")
        f.write(f"Standard Deviation of Reward: {std_dev_reward}\n")
    print(f"Statistics saved as {stats_output}")
else:
    print("No output path provided. Statistics not saved.")
