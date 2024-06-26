import os
from glob import glob
import matplotlib.pyplot as plt
import pandas as pd

def concatenate_and_plot_rewards(folderpath, output_folder):
    # Search for CSV files with "training" and "evaluation" in their names
    training_data_files = glob(os.path.join(folderpath, '*training_rewards*.csv'))
    evaluation_data_files = glob(os.path.join(folderpath, '*output_rewards_evaluation*.csv'))

    # Ensure that at least one training and one evaluation CSV file are found
    if len(training_data_files) < 1 or len(evaluation_data_files) < 1:
        raise FileNotFoundError("Not enough training or evaluation CSV files found in the folder.")

    # Group files by season
    training_data_files.sort()
    evaluation_data_files.sort()

    # Extract seasons from filenames and group files by season
    training_groups = {}
    evaluation_groups = {}

    for f in training_data_files:
        season = f.split('_')[-2]
        if season not in training_groups:
            training_groups[season] = []
        training_groups[season].append(f)

    for f in evaluation_data_files:
        season = f.split('_')[-2]
        if season not in evaluation_groups:
            evaluation_groups[season] = []
        evaluation_groups[season].append(f)

    concatenated_training_rewards = []
    concatenated_evaluation_rewards = []

    # Concatenate and collect rewards for each season
    for season in training_groups.keys():
        if season in evaluation_groups:
            training_data_csv = pd.concat([pd.read_csv(f) for f in training_groups[season]], ignore_index=True)
            evaluation_data_csv = pd.concat([pd.read_csv(f) for f in evaluation_groups[season]], ignore_index=True)

            # Extract the second column (assuming it's the relevant data)
            training_rewards = training_data_csv.iloc[:, 1]
            evaluation_rewards = evaluation_data_csv.iloc[:, 1]

            # Concatenate the training and evaluation data
            concatenated_training_rewards.extend(training_rewards)
            concatenated_evaluation_rewards.extend(evaluation_rewards)

    concatenated_training_rewards = pd.Series(concatenated_training_rewards)
    concatenated_evaluation_rewards = pd.Series(concatenated_evaluation_rewards)

    # Plot the concatenated graph using matplotlib
    plt.figure(figsize=(12, 6))
    total_steps = len(concatenated_training_rewards) + len(concatenated_evaluation_rewards)
    plt.plot(range(len(concatenated_training_rewards)), concatenated_training_rewards, label='Training Data', color='blue')
    plt.plot(range(len(concatenated_training_rewards), total_steps), concatenated_evaluation_rewards, label='Evaluation Data', color='red')
    plt.xlabel('Steps')
    plt.ylabel('Rewards')
    plt.title('Concatenated Training and Evaluation Rewards Across All Seasons')
    plt.legend()
    plt.grid(True)

    # Save plot if an output path is provided
    output_path = input("Enter the filename to save the plot (leave blank to skip saving): ")
    if output_path:
        output = os.path.join(output_folder, f"{output_path}.png")
        plt.savefig(output, bbox_inches='tight')
        print(f"Plot saved as {output}")
    else:
        print("No output path provided. Plot not saved.")

    # Display the plot
    plt.show()

# Define the folder paths
folderpath = r"C:\Users\tessel.kaal\OneDrive - Accenture\Thesis\Output training model\VERSION 5\VERSION 5.1\SCENARIO5\0625_400_200_Scenario5.5_Allmethods_2"
output_folder = r"C:\Users\tessel.kaal\OneDrive - Accenture\Thesis\Output training model\VERSION 5\VERSION 5.1\Concatenatedgraphs"

# Call the function
concatenate_and_plot_rewards(folderpath, output_folder)
