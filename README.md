# Kịrịkẹ-English Dictionary Parser

This project contains a Python script that parses a Kịrịkẹ-English dictionary PDF and converts it into structured formats (CSV, JSON, and Markdown).

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Output](#output)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/kirike-english-dictionary-parser.git
   cd kirike-english-dictionary-parser
   ```

2. (Optional) Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Place your Kịrịkẹ-English dictionary PDF file in the same directory as the script.

2. Open `process_dictionary.py` and update the `input_file` variable with your PDF filename:

   ```python
   input_file = "your-dictionary-file.pdf"
   ```

3. Run the script:
   ```
   python process_dictionary.py
   ```

4. The script will generate three output files in the same directory:
   - `kirike-english-dictionary.csv`: CSV version of the dictionary
   - `kirike-english-dictionary.json`: JSON version of the dictionary
   - `kirike-english-dictionary.md`: Markdown version of the dictionary

## Customization

To use this script with a different PDF dictionary:

1. Update the `input_file` variable in `process_dictionary.py` with your new PDF filename.

2. If your dictionary starts on a different page, modify the `read_pdf_file` function:

   ```python
   def read_pdf_file(file_path):
       # Change '15' to the page number where your dictionary starts (0-indexed)
       text = extract_text(file_path, page_numbers=range(15, 1000))
       text = unicodedata.normalize('NFKD', text)
       return text
   ```

3. If your dictionary has a different structure, update the regular expression in the `parse_dictionary` function:

   ```python
   match = re.match(r'^(\S+)\s+(\S+\.)\s+(\S+)\s+(.*)', line)
   ```

   Modify this pattern to match your dictionary's entry format.

## Output

- The CSV file can be opened with spreadsheet software like Microsoft Excel or Google Sheets.
- The JSON file can be used in various programming languages and web applications.
- The Markdown file can be viewed with any Markdown viewer or text editor.

## Troubleshooting

- If you encounter encoding issues, try different normalization methods in the `read_pdf_file` function:
  ```python
  text = unicodedata.normalize('NFKC', text)  # or 'NFC', or 'NFD'
  ```

- If the script is not correctly parsing entries, check the regular expression in the `parse_dictionary` function and adjust it to match your PDF's structure.

- For PDFs with complex layouts or scanned images, you might need to use OCR software to convert the PDF to text before processing.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This README provides a comprehensive guide for users to understand, install, use, and customize your script. It also includes sections on troubleshooting and contributing, which are helpful for open-source projects.

Remember to update the repository URL in the Installation section with your actual GitHub repository URL once you've created it.

To add these files to your GitHub repository:

1. Create a new repository on GitHub.
2. Initialize a Git repository in your local project folder (if you haven't already):
   ```
   git init
   ```
3. Add all the files:
   ```
   git add .
   ```
4. Commit the files:
   ```
   git commit -m "Initial commit"
   ```
5. Link your local repository to the GitHub repository:
   ```
   git remote add origin https://github.com/your-username/your-repo-name.git
   ```
6. Push the files to GitHub:
   ```
   git push -u origin master
   ```

This will set up your GitHub repository with the script, additional files, and a detailed README.md, making it easy for others to understand and use your Kịrịkẹ-English Dictionary Parser.