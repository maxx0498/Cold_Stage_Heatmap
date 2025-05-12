import os
import pandas as pd


def process_csv(file_path, master_file):
    # Read the CSV into a DataFrame
    df = pd.read_csv(file_path)

    # Calculate the median of the 'T' column
    median_T = df['T'].median()

    # Calculate the difference between the median and each 'T' value
    df['T_difference'] = df['T'] - median_T

    # Select relevant columns to save
    df_output = df[['T_difference', 'xpos', 'ypos']]

    # Append the result to the master CSV file
    df_output.to_csv(master_file, mode='a',
                     header=not os.path.exists(master_file), index=False)


def openfold(direc, master_file):
    for root, dirs, files in os.walk(direc):
        for file in files:
            if file == "dropdata.csv":
                # Log the folder being processed
                print(f"Processing file in folder: {root}")

                file_path = os.path.join(root, file)
                process_csv(file_path, master_file)


# Path for the combined output file
master_file = "O:/Nat_Chem-Aerosol-data/People/Max Fobian Skov/Master project/Heatmap folder/droplet_heatmap_redone.csv"

# Directory to search for dropdata.csv files
folder = "//uni.au.dk/dfs/Nat_Chem-Aerosol-data/Data/cold stage/Processing/level 2"
openfold(folder, master_file)
