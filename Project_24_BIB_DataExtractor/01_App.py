import bibtexparser
import pandas as pd

# Step 1: Load and parse the .bib file
def load_bib_file(file_path):
    
    with open(file_path, encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    return bib_database.entries

# Step 2: Convert to DataFrame and export to Excel
def export_to_excel(entries, output_excel):
    df = pd.DataFrame(entries)
    df.to_excel(output_excel, index=False)
    print(f"Exported {len(df)} entries to {output_excel}")

# Example usage
bib_file = "library.bib"  # Replace with your .bib file name
output_excel = "output_bib_data.xlsx"
entries = load_bib_file(bib_file)
export_to_excel(entries, output_excel)

