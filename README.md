# Blast2Excel for Ugene blast

This Python script extracts embedded BLAST results from a GenBank (.gb) file exported from UGENE and organizes them into a structured Excel spreadsheet.

## ✅ Features

- Reads `.gb` files with BLAST annotations from UGENE.
- Automatically extracts the following fields per hit:
  - `Sequence Blasted`
  - `Accession`
  - `Identity (%)`
  - `E-value`
  - `Bit Score`
  - `Definition`
- Saves the data into an Excel file (`blast_hits.xlsx`) in the same directory as the script.

## 📂 Expected Input

A GenBank file named `orig_with_blast.gb` placed in the same folder as the script, containing BLAST annotations in the following format:

```text
/accession="..."
/def="..."
/E-value="..."
/bit-score="..."
/identities="... (%)"
```

## 📤 Output

- A file named `blast_hits.xlsx` will be generated in the same folder as the script.

## 🛠 Requirements

- Python 3.x
- Libraries: `pandas`, `openpyxl`

To install the requirements:

```bash
pip install -r requirements.txt
```

## 🚀 How to Use

1. Place your `orig_with_blast.gb` file in the same folder as the script `ugene_blast_to_excel.py`.
2. Run the script:

```bash
python ugene_blast_to_excel.py
```

3. Check the generated Excel file named `blast_hits.xlsx`.

## 📎 Notes

- Make sure the BLAST annotations follow the expected format exported by UGENE.
- The script automatically detects its own location and writes the Excel output to the same directory.

Created by João Paulo Romualdo A. Bernardes
