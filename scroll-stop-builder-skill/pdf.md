---
name: pdf
description: >
  Does anything with PDF files — reading, extracting text and tables, merging, splitting, rotating,
  watermarking, creating from scratch, filling forms, encrypting, extracting images, and OCR.
  Trigger when the user says "read this PDF", "extract data from PDF", "merge PDFs", "create a PDF",
  "fill out this form", "add a watermark", "protect this PDF", or any task where a PDF file is involved.
keywords:
  - pdf
  - extract
  - merge
  - split
  - watermark
  - OCR
  - form
  - encrypt
  - read pdf
  - table extraction
---

# PDF Skill

You handle all PDF operations using Python libraries and command-line tools. You always choose the right tool for the job.

---

## Tool Selection Guide

| Task | Best Tool |
|------|-----------|
| Extract text (layout-preserved) | `pdfplumber` |
| Extract tables from PDF | `pdfplumber` |
| Merge multiple PDFs | `pypdf` or `qpdf` |
| Split PDF pages | `pypdf` or `qpdf` |
| Rotate pages | `pypdf` |
| Extract metadata | `pypdf` |
| Create PDF from scratch | `reportlab` |
| Watermark pages | `pypdf` + `reportlab` |
| Password protect / encrypt | `pypdf` or `qpdf` |
| Extract images from PDF | `pypdfium2` or `pdfplumber` |
| OCR scanned documents | `pytesseract` + `pdf2image` |
| Fill PDF forms | See FORMS.md |
| Convert PDF → images | `poppler-utils` (pdftoppm) |

---

## Key Libraries

### pdfplumber (Text & Table Extraction)
Best for extracting text with spatial layout awareness and pulling tables as structured data.

```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    for page in pdf.pages:
        # Extract all text
        text = page.extract_text()
        
        # Extract tables as list of lists
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                print(row)
```

### pypdf (Merge / Split / Rotate)
```python
from pypdf import PdfWriter, PdfReader

# Merge
writer = PdfWriter()
for filename in ["file1.pdf", "file2.pdf"]:
    reader = PdfReader(filename)
    for page in reader.pages:
        writer.add_page(page)
with open("merged.pdf", "wb") as f:
    writer.write(f)

# Split — extract pages 2-5
reader = PdfReader("input.pdf")
writer = PdfWriter()
for page_num in range(1, 5):  # 0-indexed
    writer.add_page(reader.pages[page_num])
with open("extracted.pdf", "wb") as f:
    writer.write(f)
```

### reportlab (Create PDF from Scratch)
```python
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("output.pdf", pagesize=A4)
styles = getSampleStyleSheet()
story = []
story.append(Paragraph("Title Here", styles['Title']))
story.append(Spacer(1, 12))
story.append(Paragraph("Body text here.", styles['Normal']))
doc.build(story)
```

**Critical reportlab rule:** Never use Unicode subscript/superscript characters (₁, ², ™, etc.). Use ReportLab's XML markup tags in Paragraph objects instead: `<super>2</super>`, `<sub>1</sub>`.

### OCR for Scanned Documents
```python
from pdf2image import convert_from_path
import pytesseract

pages = convert_from_path("scanned.pdf", dpi=300)
full_text = ""
for page_image in pages:
    text = pytesseract.image_to_string(page_image, lang='spa')  # 'spa' for Spanish
    full_text += text + "\n"
```

---

## Command-Line Tools

```bash
# Extract text (fast, no Python)
pdftotext input.pdf output.txt

# Merge with qpdf
qpdf --empty --pages file1.pdf file2.pdf -- merged.pdf

# Encrypt / password protect
qpdf --encrypt user-password owner-password 256 -- input.pdf protected.pdf

# Convert PDF pages to images
pdftoppm -r 300 -png input.pdf output_prefix
```

---

## Audit PDF Processing (Semrush / Analytics Reports)

When processing SEO audit PDFs or analytics reports:
1. Use `pdfplumber` to extract tables with layout preservation
2. Parse extracted tables into pandas DataFrames for analysis
3. Export cleaned data to .xlsx or .csv for further use
4. Highlight critical findings with color formatting in the export

---

## Delivery

Always verify the output PDF:
- Opens without error
- Pages are in correct order
- Text is readable (not garbled encoding)
- File size is reasonable (flag if unexpectedly large)

For created PDFs: embed fonts to ensure cross-platform rendering.
For encrypted PDFs: confirm the password works before delivering.
