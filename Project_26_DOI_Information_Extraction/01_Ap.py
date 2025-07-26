import pandas as pd
import requests
import time

def fetch_metadata(doi):
    url = f"https://api.crossref.org/works/{doi}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()['message']
            return {
                'DOI': doi,
                'Title': data.get('title', [''])[0],
                'Authors': ', '.join([f"{a.get('given', '')} {a.get('family', '')}" for a in data.get('author', [])]),
                'Journal': data.get('container-title', [''])[0],
                'Publisher': data.get('publisher', ''),
                'Published Year': data.get('published-print', {}).get('date-parts', [[None]])[0][0] or data.get('published-online', {}).get('date-parts', [[None]])[0][0],
                'Abstract': data.get('abstract', 'N/A')
            }
        else:
            return {'DOI': doi, 'Error': f"Status code: {response.status_code}"}
    except Exception as e:
        return {'DOI': doi, 'Error': str(e)}

# Step 1: Load Excel file
input_file = 'DOI_Info.xlsx'  # Excel file must have a column 'DOI'
df = pd.read_excel(input_file)

# Step 2: Process each DOI
results = []
for doi in df['DOI']:
    metadata = fetch_metadata(doi)
    results.append(metadata)
    time.sleep(1)  # To avoid rate limits

# Step 3: Save to Excel
output_df = pd.DataFrame(results)
output_df.to_excel('doi_metadata_output.xlsx', index=False)
