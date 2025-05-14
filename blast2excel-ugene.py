import re
import pandas as pd
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Input and output file paths in the same directory as the script
input_file = os.path.join(script_dir, "example.gb")  # Put your GenBank file here
excel_output = os.path.join(script_dir, "blast_hits.xlsx")   # Output will be in the same folder as this script

# List to store parsed BLAST hits
results_table = []

# Function to reset extracted variables for each BLAST hit
def reset_fields():
    return {
        "accession": None,
        "definition": None,
        "evalue": None,
        "bitscore": None,
        "identity": None
    }

# Initialize for first use
fields = reset_fields()
sequence_label = None

# Open and parse the input GenBank file line by line
with open(input_file, "r") as f:
    for line in f:
        line = line.strip()

        # New sequence block starts
        if line.startswith("LOCUS"):
            parts = line.split()
            sequence_label = parts[1] if len(parts) > 1 else "Unknown"
            fields = reset_fields()

        # Extract information from custom annotations
        elif "/accession=" in line:
            fields["accession"] = line.split('"')[1]
        elif "/def=" in line:
            fields["definition"] = line.split('"', 1)[1].strip()
        elif "/E-value=" in line:
            fields["evalue"] = line.split('"')[1]
        elif "/bit-score=" in line:
            fields["bitscore"] = line.split('"')[1]
        elif "/identities=" in line:
            # Extract numeric percentage value from identities string
            match = re.search(r"\(([\d\.]+)%\)", line)
            fields["identity"] = float(match.group(1)) if match else None

            # After identities, we assume the block is complete and ready to store
            if all(value is not None for value in fields.values()) and sequence_label is not None:
                results_table.append({
                    "Sequence Blasted": sequence_label,
                    "Accession": fields["accession"],
                    "Identity (%)": fields["identity"],
                    "E-value": fields["evalue"],
                    "Bit Score": fields["bitscore"],
                    "Definition": fields["definition"]
                })
                # Prepare for next hit
                fields = reset_fields()

# Convert the collected data into a DataFrame and write to Excel
df = pd.DataFrame(results_table)
df.to_excel(excel_output, index=False)

print(f"Spreadsheet saved to: {excel_output}")
