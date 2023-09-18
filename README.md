Converts the copy-pasted values from [The Refinitiv Business Classification](https://www.refinitiv.com/content/dam/marketing/en_us/documents/quick-reference-guides/trbc-business-classification-quick-guide.pdf) PDF to a JSON structure.

note:
- you'll need to remove the column headers and deal with line breaks.
- copy-pasting the whole pdf at once fails because of page break issues. Do it page by page.

To run: `python parse-text.py`

a `trbc.json` file will be created in the directory
