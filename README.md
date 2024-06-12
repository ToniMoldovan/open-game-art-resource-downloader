# OpenGameArt Resource/Assets Downloader

This script allows you to download resources/assets from the OpenGameArt website (or any similar site) efficiently by specifying a file name prefix and a range of indices. It is especially useful for downloading series of files with similar names.

## Features
- Downloads a range of files with a common prefix from a specified URL.
- Saves the files to a specified directory on your local machine.
- Easily configurable for different websites and file ranges.

## Requirements
- Python 3.x
- `requests` library

## Installation
First, ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

Next, install the `requests` library using pip:

```sh
pip install requests
```

## Usage

1. **Clone the repository:**

   ```sh
   git clone https://github.com/ToniMoldovan/open-game-art-resource-downloader.git
   ```

2. **Modify the script if necessary:**
   - Update the `base_url`, `file_prefix`, `start_index`, `end_index`, and `download_directory` variables in the script to match your needs.

3. **Run the script:**

   ```sh
   python downloader.py
   ```

## Example

If you want to download files named `effort_grunt_male01.wav`, `effort_grunt_male02.wav`, ..., `effort_grunt_male41.wav` from the `https://opengameart.org/sites/default/files/` URL and save them to `E:/GameDev/Assets/Male_Voice_SFX`, the script provided will do exactly that.

## Customization
- **Change the URL and Prefix:**
  To download files from a different website or with a different naming pattern, modify the `base_url` and `file_prefix` variables.

- **Adjust the Range:**
  Set the `start_index` and `end_index` variables to match the range of files you want to download.

- **Download Directory:**
  Change the `download_directory` to the path where you want to save the downloaded files.

## Contributing

Feel free to submit pull requests if you have suggestions for improvements or new features. 

**For major changes**, please open an issue first to discuss what you would like to change.

## License

This project is open-source and available under the MIT License.

## Contact

If you have any questions or need further assistance, please open an issue or contact me at [antonio.moldovan82@yahoo.com].
