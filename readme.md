
# Proofreader Script Documentation

## Overview
The **Proofreader Script** is a Python-based utility that leverages **LanguageTool** to automatically detect and correct grammar mistakes in text documents. It is designed for conservative proofreading where proper nouns, case titles, and Tagalog words are preserved, avoiding false corrections.

This script is ideal for processing legal case digests, academic papers, and mixed English-Tagalog documents, ensuring grammatical accuracy without distorting domain-specific terminology.

---

## Features
- **Grammar-only corrections**  
  - Filters LanguageTool matches to apply only grammar-related fixes.  
  - Ignores stylistic and spelling suggestions to avoid false positives.

- **Protects sensitive tokens**  
  - Case titles (e.g., *CIR vs. Algue, Inc.*) are skipped.  
  - Tagalog words and particles prevent corrections in affected lines.  
  - Proper nouns and acronyms are preserved.

- **Two separate logs**  
  1. `grammar_edits.log` – Records all grammar edits applied, including the rules triggered.  
  2. `skipped_items.log` – Records skipped lines with reasons (`case_title`, `tagalog_detected`, `protected_token`).  

- **Summary report**  
  - `Proofreading_Changes_Log.txt` is generated with counts of total grammar edits and skipped items.

---

## Workflow
1. **Input**: Provide a text file to the script.  
2. **Processing**:  
   - Each line is scanned by LanguageTool with grammar-only filtering.  
   - Sensitive lines (case titles, Tagalog) are skipped.  
   - Allowed grammar corrections are applied.  
3. **Logging**:  
   - Applied edits → stored in `grammar_edits.log`.  
   - Skipped content → stored in `skipped_items.log`.  
   - Summary report is generated.  
4. **Output**:  
   - A corrected version of the file (if enabled).  
   - Logs for transparency and audit.

---

## Example

### Input:
```
Republic vs. Mambulao Lumber  
The President have extended incentives to John Hay SEZ.  
```
### Output:
```
Republic vs. Mambulao Lumber   (Skipped – case title)  
The President has extended incentives to John Hay SEZ.  
```

### Logs:
**grammar_edits.log**
```
Original: The President have extended incentives to John Hay SEZ.  
Corrected: The President has extended incentives to John Hay SEZ.  
Rules applied: [SUBJECT_VERB_AGREEMENT] – Use "has" instead of "have" when subject is singular.
```

**skipped_items.log**
```
Skipped: Republic vs. Mambulao Lumber  
Reason: case_title  
```

**Proofreading_Changes_Log.txt**
```
Summary of Proofreading:
- Grammar edits applied: 1  
- Skipped items: 1  
See grammar_edits.log and skipped_items.log for details.  
```

---

## Usage
Activate your virtual environment and run the script:
```bash
source /Users/macbookm1/Documents/Projects/.venv/bin/activate
python /Users/macbookm1/Documents/Projects/docxer/proofreader.py
```

---

## Future Improvements
- CLI flags for custom log file names (`--grammar-log`, `--skipped-log`).  
- Token-level Tagalog filtering for mixed-language sentences.  
- Export to Markdown/HTML with highlights of changes.  

---

## Author
Developed by John for processing legal case digests and academic documents in mixed English-Tagalog settings.
