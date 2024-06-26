import os
from glob import glob
import pandas as pd

def calculate_seasonal_statistics(folderpath, folderpath_output):
    # Search for CSV files with "evaluation" in their names
    evaluation_data_files = glob(os.path.join(folderpath, '*output_rewards_evaluation*.csv'))

    # Ensure that at least one evaluation CSV file is found
    if len(evaluation_data_files) < 1:
        raise FileNotFoundError("No evaluation CSV files found in the folder.")

    # Group files by season
    evaluation_data_files.sort()

    # Extract seasons from filenames and group files by season
    evaluation_groups = {}

    for f in evaluation_data_files:
        season = f.split('_')[-2]
        if season not in evaluation_groups:
            evaluation_groups[season] = []
        evaluation_groups[season].append(f)

    # Calculate and output statistics for each season
    for season, files in evaluation_groups.items():
        evaluation_data_csv = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

        # Extract the second column (assuming it's the relevant data)
        evaluation_rewards = evaluation_data_csv.iloc[:, 1]

        # Calculate statistics for evaluation data
        mean_reward = evaluation_rewards.mean()
        variance_reward = evaluation_rewards.var()
        std_dev_reward = evaluation_rewards.std()

        # Output the statistics
        print(f"Season {season} - Mean Reward: {mean_reward}")
        print(f"Season {season} - Variance of Reward: {variance_reward}")
        print(f"Season {season} - Standard Deviation of Reward: {std_dev_reward}")

        # Optionally save statistics to a file
        output_stats_path = input(f"Enter the filename to save the statistics for season {season} (leave blank to skip saving): ")
        if output_stats_path:
            stats_output = os.path.join(folderpath_output, f"{output_stats_path}.txt")
            with open(stats_output, 'w') as f:
                f.write(f"Season {season} - Mean Reward: {mean_reward}\n")
                f.write(f"Season {season} - Variance of Reward: {variance_reward}\n")
                f.write(f"Season {season} - Standard Deviation of Reward: {std_dev_reward}\n")
            print(f"Statistics saved as {stats_output}")
        else:
            print(f"No output path provided for season {season}. Statistics not saved.")

# Define the folder paths
folderpath = r"C:\Users\tessel.kaal\OneDrive - Accenture\Thesis\Output training model\VERSION 5\VERSION 5.1\SCENARIO5\0612_400_200_SCENARIO5.5.2_LONGRUN"
folderpath_output = r"C:\Users\tessel.kaal\OneDrive - Accenture\Thesis\Output training model\Variability\Eval_only"

# Call the function
calculate_seasonal_statistics(folderpath, folderpath_output)
