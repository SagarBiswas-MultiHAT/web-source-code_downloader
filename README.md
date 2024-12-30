![web-source-code_downloader](https://scontent.fdac138-2.fna.fbcdn.net/v/t39.30808-6/471830853_122132259044552158_3565479281626046296_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=106&ccb=1-7&_nc_sid=127cfc&_nc_ohc=AejDNtbRnX0Q7kNvgEZc5r2&_nc_zt=23&_nc_ht=scontent.fdac138-2.fna&_nc_gid=AIJFI8o8g89A7N9Fv0OfCCA&oh=00_AYCmxd-6b43GdRnGunI4zEWRsUVMefAOcg4VFWbwz2BybQ&oe=6778C996)

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
