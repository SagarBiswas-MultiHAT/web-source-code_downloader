![I am a Coder | Web Devoloper | Web Penetration Tester. ]([https://scontent.fdac138-1.fna.fbcdn.net/v/t39.30808-6/471196948_581277394508345_1068491655999856687_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=cc71e4&_nc_eui2=AeHZ4ksf_IPOhLH3TEgzPcUe7K2RK83azQTsrZErzdrNBOPx0JJlD7r26-6RQOCfrTMOSQMy1TdBTTkY522XPM4Y&_nc_ohc=PUcdaJUHzOoQ7kNvgHSDs97&_nc_zt=23&_nc_ht=scontent.fdac138-1.fna&_nc_gid=AnQ0Pl1JI2FUThknlXiUPn7&oh=00_AYAZbBfDXe36-n1_A3WTORsW3Q1d96zECPiSEUkrSMQU4Q&oe=676CFB3D](https://www.facebook.com/photo/?fbid=122132259038552158&set=a.122095037252552158&__cft__[0]=AZVoZK9m6COGLegTuFNnSCUzyDvNTr9aAv3c6JjCuoMDnX0E3mAsEQ4Y6Pyk5QRb6sYdtKvlXdQFXNCkZ08nyny1XS307-4FKW9wpivfkkokjg&__tn__=EH-R))

# Web Source Code Downloader

This Python script allows you to easily download the HTML source code of any website. Just input the website URL, and the script will fetch the source code and save it as an `HTML` file on your computer. It's simple, lightweight, and perfect for saving or analyzing web pages locally.

## Features

- Fetches the HTML source code of any website.
- Saves the content as a `.html` file in the local directory.
- Displays an ASCII art banner and colorful terminal output.
- Easy-to-use interface that only requires the website URL.

## Requirements

Before running the script, you'll need to install the following Python libraries:

- `pyfiglet` – Used for generating ASCII art banners.
- `termcolor` – Adds color to terminal output.

You can install these using `pip`:

```bash
pip install pyfiglet termcolor
```

## How to Use

1. Clone or download this repository to your computer.
2. Install the necessary dependencies (as mentioned above).
3. Run the script with:

   ```bash
   python3 web_source_code_downloader.py
   ```

4. Enter the website URL when prompted (make sure to include `http://` or `https://`).
5. The source code will be saved as `web_source_code.html` in the same directory.

## Example

```bash
$ python3 web_source_code_downloader.py
..:: Enter the website name (including http:// or https://): https://example.com
--> The source code has been saved to: web_source_code.html
```

## Optional: Using a Virtual Environment

For better package management, it’s recommended to run the script inside a virtual environment. Here's how to set it up:

1. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install pyfiglet termcolor
   ```

4. After use, deactivate the environment:

   ```bash
   deactivate
   ```

## Author

- **Sagar Biswas**

---
