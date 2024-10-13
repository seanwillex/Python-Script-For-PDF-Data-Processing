import re
import pandas as pd
from pdfminer.high_level import extract_text
import unicodedata
import json

def read_pdf_file(file_path):
    # Extract text from page 16 onwards
    text = extract_text(file_path, page_numbers=range(15, 1000))  # Assuming max 1000 pages
    # Normalize the Unicode characters
    text = unicodedata.normalize('NFKD', text)
    return text

def clean_text(text):
    # Remove any remaining non-printable characters
    return ''.join(char for char in text if char.isprintable() or char.isspace())

def parse_dictionary(content):
    entries = []
    lines = content.split('\n')
    current_entry = {}
    
    for line in lines:
        line = clean_text(line.strip())
        if not line:
            continue
        
        # Check if this line starts a new entry
        match = re.match(r'^(\S+)\s+(\S+\.)\s+(\S+)\s+(.*)', line)
        if match:
            if current_entry:
                entries.append(current_entry)
            kirike, pos, sf, english = match.groups()
            current_entry = {
                'Kịrịkẹ': kirike,
                'Part of Speech': pos,
                'Semantic Field': sf,
                'English Gloss': english
            }
        elif current_entry:
            # If not a new entry, append to the current English gloss
            current_entry['English Gloss'] += ' ' + line
    
    # Add the last entry
    if current_entry:
        entries.append(current_entry)
    
    return entries

def save_to_csv(entries, output_file):
    df = pd.DataFrame(entries)
    df.to_csv(output_file, index=False, encoding='utf-8-sig')

def save_to_json(entries, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

def save_to_markdown(entries, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Kịrịkẹ-English Dictionary\n\n")
        for entry in entries:
            f.write(f"## {entry['Kịrịkẹ']}\n\n")
            f.write(f"**Part of Speech:** {entry['Part of Speech']}\n\n")
            f.write(f"**Semantic Field:** {entry['Semantic Field']}\n\n")
            f.write(f"**English Gloss:** {entry['English Gloss']}\n\n")
            f.write("---\n\n")

if __name__ == "__main__":
    input_file = "kirike-english-dictionary.pdf"  # Replace with your PDF file name
    output_csv = "kirike-english-dictionary.csv"
    output_json = "kirike-english-dictionary.json"
    output_md = "kirike-english-dictionary.md"

    print("Reading PDF file...")
    content = read_pdf_file(input_file)
    
    print("Parsing dictionary entries...")
    entries = parse_dictionary(content)

    print("Saving to CSV...")
    save_to_csv(entries, output_csv)
    
    print("Saving to JSON...")
    save_to_json(entries, output_json)

    print("Saving to Markdown...")
    save_to_markdown(entries, output_md)

    print(f"Processed {len(entries)} entries.")
    print(f"CSV file saved: {output_csv}")
    print(f"JSON file saved: {output_json}")
    print(f"Markdown file saved: {output_md}")