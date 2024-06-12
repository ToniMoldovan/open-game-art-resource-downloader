import os
import requests

# Define the base URL and the range of file numbers
base_url = "https://opengameart.org/sites/default/files/"
file_prefix = "effort_grunt_male.wav"
start_index = 1
end_index = 41

# Specify the directory where you want to save the downloaded files
download_directory = "E:/GameDev/Assets/Male_Voice_SFX"

# Create the directory if it doesn't exist
os.makedirs(download_directory, exist_ok=True)

# Function to download a file
def download_file(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded: {save_path}")

# Loop to download each file
for i in range(start_index, end_index + 1):
    file_number = str(i).zfill(2)  # Ensure the file number is two digits
    file_name = f"{file_number}._{file_prefix}"
    file_url = base_url + file_name
    save_path = os.path.join(download_directory, file_name)
    download_file(file_url, save_path)

print("All files have been downloaded.")
