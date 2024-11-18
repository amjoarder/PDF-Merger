import PyPDF2
import os

# Create a PdfMerger object
merger = PyPDF2.PdfMerger()

# Loop through all files in the current directory
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        # Append each PDF file to the merger
        merger.append(file)

# Write the combined PDF to a new file
merger.write("combinedDocs.pdf")

# Close the PdfMerger object
merger.close()
