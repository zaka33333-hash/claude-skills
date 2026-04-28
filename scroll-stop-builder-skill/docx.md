---
name: docx
description: >
  Creates, reads, edits, and manipulates Word documents (.docx files). Trigger when the user asks
  to create a Word document, edit a .docx file, extract content from a Word document, convert a
  document to PDF, add tracked changes, or any task where a .docx file is involved.
  Also triggers for "write a Word doc", "make a contract", "edit this document", "add comments to",
  or any professional document creation task.
keywords:
  - docx
  - word
  - document
  - microsoft word
  - contract
  - report
  - brief
---

# DOCX Skill

You create and manipulate Word documents professionally. Output is always clean, properly formatted, and cross-platform compatible.

---

## Tool Selection

| Task | Tool |
|------|------|
| Create from scratch | `docx-js` (JavaScript) |
| Edit existing document | Unpack XML → edit → repack |
| Extract text content | `pandoc` or XML unpack |
| Convert to PDF | LibreOffice CLI |
| Add tracked changes | XML editing |

---

## Creating Documents (docx-js)

```javascript
const { Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell } = require("docx");
const fs = require("fs");

const doc = new Document({
  sections: [{
    properties: {
      page: {
        size: {
          width: 12240,  // US Letter (DXA units) — NOT A4 default
          height: 15840,
        },
        margin: {
          top: 1440, bottom: 1440,
          left: 1440, right: 1440,
        }
      }
    },
    children: [
      new Paragraph({
        text: "Document Title",
        heading: HeadingLevel.HEADING_1,
      }),
      new Paragraph({
        children: [
          new TextRun("Body text here. "),
          new TextRun({ text: "Bold text.", bold: true }),
        ],
      }),
    ],
  }],
});

Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync("output.docx", buffer);
});
```

---

## Critical Technical Rules

### Page Size
- **docx-js defaults to A4** — always explicitly set US Letter (12,240 × 15,840 DXA) unless A4 is specified
- All measurements in DXA units: 1 inch = 1440 DXA

### Tables
```javascript
// Always specify BOTH columnWidths array AND individual cell widths
new Table({
  columnWidths: [3000, 5000, 2000],  // DXA — must match cell widths
  rows: [
    new TableRow({
      children: [
        new TableCell({
          width: { size: 3000, type: WidthType.DXA },
          children: [new Paragraph("Cell content")],
        }),
      ],
    }),
  ],
})
```
Never use percentage widths in tables — they cause rendering issues.

### Bullet Lists
```javascript
// NEVER use unicode bullet characters (•, -, ▪)
// Use the proper numbering configuration:
new Paragraph({
  text: "Bullet item",
  numbering: {
    reference: "bullet-list",
    level: 0,
  },
})
```

### Images
```javascript
// The 'type' parameter is MANDATORY — omitting it breaks the document
new ImageRun({
  data: fs.readFileSync("image.png"),
  transformation: { width: 400, height: 300 },
  type: "png",  // Required: "png", "jpg", "gif", "bmp", "svg"
})
```

### Page Breaks
```javascript
// Page breaks MUST be inside a Paragraph — never standalone
new Paragraph({
  children: [new PageBreak()],
})
```

---

## Editing Existing Documents

1. **Unpack** the .docx (it's a ZIP file):
```bash
unzip document.docx -d document_unpacked/
```

2. **Edit XML** in `document_unpacked/word/document.xml`
   - Use exact style IDs to override built-ins: "Heading1", "Normal", "TableGrid"
   - Never create new style names if built-in styles exist

3. **Repack**:
```bash
cd document_unpacked && zip -r ../document_edited.docx .
```

---

## Converting to PDF

```bash
# LibreOffice CLI — most reliable cross-platform conversion
libreoffice --headless --convert-to pdf --outdir /output/ document.docx
```

---

## Supported Features

- Headers and footers (different first page supported)
- Table of contents (auto-generated from heading styles)
- Tracked changes and comments
- Footnotes and endnotes
- Hyperlinks (internal bookmarks and external URLs)
- Multi-column layouts
- Custom styles

---

## Delivery

Always verify the output document:
- Opens in Microsoft Word without repair prompts
- All formatting renders correctly
- Images are embedded (not linked)
- No placeholder text remains
