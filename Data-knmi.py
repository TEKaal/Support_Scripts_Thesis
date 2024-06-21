import requests
import os

# Your API key and headers
api_key = 'eyJvcmciOiI1ZTU1NGUxOTI3NGE5NjAwMDEyYTNlYjEiLCJpZCI6IjMzOTAyNTJhZTc2NzRlZGZiY2Q5NjA4Y2ZlOTY4YTRhIiwiaCI6Im11cm11cjEyOCJ9'  # Replace with your actual API key
headers = {'Authorization': f'Bearer {api_key}'}

# Variables for dataset, version
dataset_name = 'zonneschijnduur_en_straling'  # Example dataset name
version_id = '1.0'  # Example version ID

# Base URL for file download
base_url = 'https://api.dataplatform.knmi.nl/open-data/v1/datasets/'

# Local directory to save the files (change this to your local directory if necessary)
local_directory = r'C:\Users\tessel.kaal\OneDrive - Accenture\Thesis\Thesis P4\Data\Solar\Solar dowloads'

# Ensure the directory exists
os.makedirs(local_directory, exist_ok=True)

for month in range(12,13):  # Loop through months 1 to 12
    formatted_month = f'{month:02d}'
    filename = f'kis_tos_2022{formatted_month}.gz'
    url_file_download = f'{base_url}{dataset_name}/versions/{version_id}/files/{filename}/url'

    # Making the API call to get the download URL
    response_download = requests.get(url_file_download, headers=headers)

    if response_download.status_code == 200:
        download_url_info = response_download.json()
        download_url = download_url_info.get('temporaryDownloadUrl')
        print('Downloading:', filename)

        # Download the file
        if download_url:
            file_response = requests.get(download_url)
            if file_response.status_code == 200:
                file_path = os.path.join(local_directory, filename)
                with open(file_path, 'wb') as file:
                    file.write(file_response.content)
                print(f'Successfully downloaded {filename} to {file_path}')
            else:
                print(f'Error downloading {filename}')
        else:
            print(f'Download URL not found for {filename}')
    else:
        print(f'Error getting download URL for {filename}:', response_download.status_code, response_download.text)


