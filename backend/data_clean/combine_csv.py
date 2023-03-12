"""Recursively combine all csv files in a directory into one csv file.
"""
import os
import csv

CSV_DIR_PATH = '/backend/data/data_source/2023'
OUTPUT_FILE_PATH = '/backend/data/data_source/2023.csv'


def combine_csv(csv_dir_path: str, output_file_path: str):
    """Recursively combine all csv files in a directory into one csv file.
    The csv file in the directory inside the directory will also be combined.

    Args:
        csv_dir_path: path of directory containing csv files
        output_file_path: path of output csv file
    """
    # Initialize an empty list to store the data from all CSV files
    combined_data = []
    # Flag to indicate if the first row of the CSV file is being read
    first_row = True

    # Traverse through the directory and its subdirectories
    for root, dirs, files in os.walk(csv_dir_path):
        # Loop through each file in the directory
        for file in files:
            # Check if the file is a CSV file
            if file.endswith('.csv'):
                # time is the filename
                time = file.split('.')[0]
                # Open the file and read its contents
                with open(os.path.join(root, file), 'r') as f:
                    reader = csv.reader(f)
                    # Loop through each row in the CSV file and append it to the combined data list
                    for row in reader:
                        # Add the time to the row
                        if first_row:
                            row.append('Time')
                            first_row = False
                        else:
                            row.append(time)
                        combined_data.append(row)

    # Write the combined data to the output CSV file
    with open(output_file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(combined_data)


combine_csv(CSV_DIR_PATH, OUTPUT_FILE_PATH)
