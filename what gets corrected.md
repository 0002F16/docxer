Here’s a plain-language Markdown brief you can share with non-technical users.
It avoids regex and explains what the tool does and doesn’t check, with clear examples.

⸻

Proofreading Rules & Exemptions (Plain Guide)

This tool checks grammar and punctuation in Word documents.
But it skips certain text on purpose to avoid false corrections.

⸻

✅ What gets corrected
	•	Grammar mistakes
	•	Punctuation errors
	•	Typographic issues (e.g., double spaces, smart quotes)
	•	Some meaning-related issues (semantics)

⸻

🚫 What is skipped (never corrected)

1. Empty text
	•	Blank lines or paragraphs with only spaces
→ Skipped automatically

⸻

2. Legal citations
	•	Example:
	•	G.R. No. 123456
	•	G.R. Nos. 123456-78
	•	Reason: Legal references must remain untouched.

⸻

3. Quoted text
	•	Anything inside quotation marks is skipped:
	•	“This is quoted.”
	•	“This is quoted.”
	•	‘This is quoted.’
	•	‘This is quoted.’

⸻

4. Book references with page numbers
	•	Example:
	•	(Author, p. 123)
	•	(Author, p. 123-125)
	•	Reason: Citations are preserved as written.

⸻

5. ALL-CAPS headers
	•	Example:
	•	TAX EXEMPTION UNDER THE LOCAL GOVERNMENT CODE
	•	Reason: Likely headings, not prose.

⸻

6. Case titles (court cases)
	•	Example:
	•	CIR vs. Algue, Inc.
	•	People v. Sandiganbayan
	•	Reason: Names of parties should not be altered.

⸻

7. Lines full of proper nouns
	•	Example:
	•	Algue, Inc. and BayanTel Corporation
	•	If most words are names/companies, the whole line is skipped.

⸻

8. Sentences with common Tagalog words
	•	If text contains everyday Filipino words like:
	•	ang, mga, si, ni, kay, kina, sa, ng, na, nang
	•	hindi, wala, meron, dito, doon, iyan, iyon
	•	ako, ikaw, siya, kami, tayo, kayo, sila
	•	po, opo, ho, ba, daw, raw, lang, din, rin
	•	pala, yata, kasi, pero, kahit, habang, sapagkat, dahil
	•	Example:
	•	Ang mga bata ay nag-aral.
	•	Reason: Filipino lines are not grammar-checked.

⸻

⚠️ Protected words (not changed inside otherwise eligible text)

Even if a sentence is checked, some tokens are protected so they won’t be touched:
	•	Acronyms: VAT, CTA
	•	Company suffixes: Inc., Corp., Ltd.
	•	Short dotted words: Co., S.A.
	•	Numbers: 2025, Bldg. 3
	•	Words starting with non-: non-delegability
	•	Most Capitalized words: Bayantel, Government (unless it’s a common starter like “The” or “In”)

Example:
	•	Sentence: “Whether or not Bayantel’s real properties …”
	•	Bayantel’s is protected as a proper noun → no edits applied to it.

⸻

📝 Logging
	•	Grammar edits log → shows original vs corrected with rules applied
	•	No issues log → sentence checked, no corrections applied
	•	Skipped log → sentence ignored (reason is explained)

⸻

🎯 Key principle

The tool is very conservative:
It only changes text when it is confident, and skips anything that looks like a name, citation, or local language.

⸻

Do you want me to add a section with sample “before & after” corrections (e.g., common grammar fixes it will make), so users see what kinds of edits to expect?