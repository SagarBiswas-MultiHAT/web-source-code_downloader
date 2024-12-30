#!/usr/bin/python3

import pyfiglet  # pyfiglet use for printing text in ASCII Art.
from termcolor import colored  # colored use for printing text in color.
import urllib.request as urllib2  # urllib2 use for opening URL.

print(colored("\n******************** Web Source Code Downloader ********************", "cyan"))
print(colored("********************* Created By Sagar Biswas *********************", "red"))

banner = colored(pyfiglet.figlet_format("Web Source Code"), "green")
print(banner)

website_name = input("\n..:: Enter the website name (including http:// or https://): ")

# Open the URL and retrieve the source code
source_code = urllib2.urlopen(website_name)

# Read the HTML content
html_content = source_code.read()

# Define the output file name
output_file = "web_source_code.html"

# Write the source code into the HTML file
with open(output_file, "wb") as file: # "wb" stands for write binary mode.
# w: This mode is for writing to a file. If the file already exists, it will be overwritten.
# b: This mode indicates binary file handling. It’s used for files that contain non-text data, such as images, videos, or any file with special characters (including HTML, which might have non-ASCII characters).
    file.write(html_content)

print(f"\n--> The source code has been saved to: {output_file}")


'''
Use a Virtual Environment
This is the recommended approach for managing Python packages without affecting the system environment.

1. Create a virtual environment:
    python3 -m venv venv

2. Activate the virtual environment:
    source venv/bin/activate

3. Install pyautogui inside the virtual environment:
    pip install pyfiglet 
    pip install termcolor

4. Deactivate the virtual environment: 
    deactivate
'''