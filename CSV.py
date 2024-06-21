import os
from glob import glob
import pandas as pd

# Define the folder path
folderpath = r"C:\Users\tessel.kaal\OneDrive - Accenture\Thesis\Output training model\Variability\Eval_only"

# Search for all CSV files in the directory
csv_files = glob(os.path.join(folderpath, '*.txt'))

# Ensure that at least one CSV file is found
if len(csv_files) < 1:
    raise FileNotFoundError("No CSV files found in the folder.")

# Create an empty DataFrame to hold all data
all_data = pd.DataFrame()

# Read each CSV file and extract its content
data_dict = {"File": [], "Mean Reward": [], "Variance of Reward": [], "Standard Deviation of Reward": []}

for file in csv_files:
    file_name = os.path.splitext(os.path.basename(file))[0]  # Get the file name without extension
    with open(file, 'r') as f:
        lines = f.readlines()
        mean_reward = float(lines[0].split(":")[1].strip())
        variance_reward = float(lines[1].split(":")[1].strip())
        std_dev_reward = float(lines[2].split(":")[1].strip())
        data_dict["File"].append(file_name)
        data_dict["Mean Reward"].append(mean_reward)
        data_dict["Variance of Reward"].append(variance_reward)
        data_dict["Standard Deviation of Reward"].append(std_dev_reward)

# Convert the dictionary to a DataFrame
all_data = pd.DataFrame(data_dict)

# Define the output path for the combined CSV file
output_csv = os.path.join(folderpath, 'combined_data.csv')

# Save the concatenated data to the output CSV file
all_data.to_csv(output_csv, index=False)

print(f"All CSV data has been combined and saved to {output_csv}")
