import pandas as pd

def excel_to_bib(excel_file, bib_file, entry_type="article", key_column="ID"):
    df = pd.read_excel(excel_file)
    
    with open(bib_file, 'w', encoding='utf-8') as f:
        for _, row in df.iterrows():
            entry_key = row.get(key_column, f"entry{_}")
            f.write(f"@{entry_type}{{{entry_key},\n")
            for col, val in row.items():
                if pd.notna(val) and col != key_column:
                    f.write(f"  {col} = {{{val}}},\n")
            f.write("}\n\n")
    print(f"Converted {len(df)} entries to {bib_file}")

# Example usage:
excel_file = "new_data.xlsx"    # Your Excel file
bib_file = "output_data.bib"      # Output .bib file
entry_type = "article"            # Can be "book", "inproceedings", etc.
key_column = "ID"                 # Column to be used as citation key (optional)

excel_to_bib(excel_file, bib_file, entry_type, key_column)
