---
name: xlsx
description: >
  Opens, reads, edits, creates, and analyzes spreadsheet files including .xlsx, .xlsm, .csv, and .tsv.
  Trigger when the user wants to create a spreadsheet, edit an Excel file, work with CSV data, build
  a financial model, clean tabular data, or any task where a spreadsheet is the primary deliverable.
  Also triggers for "make a spreadsheet", "export to Excel", "update the CSV", "bulk data update",
  or any request involving structured tabular data manipulation.
keywords:
  - excel
  - spreadsheet
  - xlsx
  - csv
  - tsv
  - data
  - table
  - financial model
  - bulk update
---

# XLSX / Spreadsheet Skill

You handle all spreadsheet operations with professional-grade output. Every file you deliver is clean, functional, and free of formula errors.

---

## Core Libraries & Tools

- **openpyxl** — Primary library for .xlsx creation and editing (formulas, formatting, charts)
- **pandas** — Data manipulation, cleaning, CSV/TSV reading, analysis
- **scripts/recalc.py** — Run after creating formulas to recalculate and verify zero errors
- **LibreOffice** (CLI) — Formula recalculation when openpyxl alone is insufficient

---

## Phase 1 — Understand the Task

Before writing any code:
1. What format is needed? (.xlsx / .csv / .tsv)
2. Is this creation from scratch, editing an existing file, or format conversion?
3. Are there formulas needed, or is this pure data?
4. What is the audience? (Internal data → clean. External deliverable → professional formatting.)

---

## Phase 2 — Professional Formatting Standards

### Typography & Fonts
- Use **Arial** or **Times New Roman** consistently throughout — never mix fonts in one file
- Headers: bold, slightly larger (12–14pt), background fill to distinguish from data rows

### Financial Model Color Coding (required for any financial data)
- **Blue text** — hardcoded inputs that users will modify
- **Black text** — formulas and calculated values
- **Green text** — links to other cells within the same worksheet
- **Red text** — links to cells in external files
- **Yellow background** — key assumption cells

### Number Formatting Rules
- Years displayed as **text** ("2024", not 2024)
- Currency: units in column header ("Revenue ($mm)"), not in each cell
- Zeros displayed as **"-"** not 0
- Percentages at **0.0%** format
- Negative numbers in **parentheses** (1,234) — never minus sign -1,234

---

## Phase 3 — Formula Rules (Critical)

**Always use Excel formulas instead of calculating values in Python and hardcoding them.**

Every calculation — totals, percentages, ratios, growth rates — must use Excel formulas so the spreadsheet remains dynamic and editable by the user.

Examples:
- ✅ `=SUM(B2:B12)` in cell B13
- ❌ Calculating the sum in Python and writing `1,234,567` to cell B13

**After creating any formula-heavy file:**
1. Run `scripts/recalc.py` to recalculate all formulas
2. Verify zero formula errors: no `#REF!`, `#DIV/0!`, `#VALUE!`, `#N/A`, `#NAME?`
3. Never deliver a file with formula errors

### Hardcoded Value Documentation
When hardcoding a value is unavoidable, add a comment cell citing:
- Source (e.g., "SEC Filing Q3 2024")
- Date retrieved
- Reference location (URL or document name)

---

## Phase 4 — Data Cleaning Standards

When working with messy input data:
1. Strip leading/trailing whitespace from all text fields
2. Standardize date formats to ISO 8601 (YYYY-MM-DD) unless specified otherwise
3. Remove duplicate rows — flag them for review rather than silently deleting
4. Normalize categorical values (e.g., "españa", "España", "ESPAÑA" → "España")
5. Document every transformation made in a "Changes" tab or comment block

---

## Phase 5 — Delivery

Deliver the complete file. When working with CSVs for Shopify or e-commerce bulk updates:
- Preserve the exact column headers from the original template
- Use UTF-8 encoding (not UTF-8 BOM)
- Quote fields that contain commas
- Never truncate product descriptions or meta fields

For multi-sheet workbooks:
- Sheet 1: Main data or summary
- Sheet 2+: Supporting data, raw inputs, or documentation
- Color-code sheet tabs to indicate their role
