---
name: academic-writing-international
description: Write, edit, review or humanize academic work outside the UK and US (Australia, NZ, Canada, Ireland, Europe, South Asia and more), from foundation to doctorate (EQF, QF-EHEA, AQF, NZQCF, NHEQF levels). Sets spelling, referencing, grade bands and level expectations by country; supports English-as-additional-language writers. Removes AI-writing tells without inventing sources.
license: MIT
---

# Academic writing (International) + humanizer

Produce or edit academic writing for English-medium study outside the UK and US that follows formal academic conventions **and** reads like a careful human writer, not a chatbot. Keep the meaning. Never invent anything.

For UK institutions use `academic-writing-uk`; for US institutions use `academic-writing-us`.

## 0. Set the profile first

Conventions vary more internationally than within the UK or US. Before editing, establish:

1. Country, institution and **level of study** (map with `references/levels-and-standards.md`).
2. English variety required (British-based, American, Australian, Canadian), or the one the user already writes in.
3. Required referencing style and edition.
4. Genre, brief, word or page limit, and permitted AI use.

If the user cannot say: keep the spelling variety already used in their text (consistently), use APA 7 as the most widely used international author–date style, impersonal voice for reports and essays, and state these assumptions at the top of the output.

{{CORE}}

## 6. Regional profiles (typical; always confirm locally)

**Australia**
- Spelling: Australian English, British-based (-ise, -our, centre, programme/program both seen); single quotation marks common.
- Referencing: APA 7 and institutional Harvard variants (e.g. AGPS-based) are most common; AGLC for law; Vancouver in health.
- Grades: commonly High Distinction (HD), Distinction (D), Credit (C), Pass (P), Fail (N); cut-offs vary by university (often HD 85+, D 75–84, C 65–74, P 50–64).
- Levels: AQF 7 Bachelor, 8 Honours (often a separate research year), 9 Master's, 10 Doctorate. Theses are commonly examined by external examiners; whether an oral examination is required varies by university.
- AI: the national regulator TEQSA has published guidance on generative AI and assessment; each university sets its own rules.

**New Zealand**
- Spelling: British-based. Levels: NZQCF 7 bachelor's, 8 honours and postgraduate diplomas, 9 Master's, 10 doctorate. Referencing: APA 7 widely used. Grades: letter grades (A+ to E) mapped to percentages; varies by university.

**Canada**
- Spelling: Canadian English mixes forms (colour, centre, but organize, analyze); follow the institution's guide and be consistent.
- Referencing: APA 7, MLA 9, Chicago; McGill Guide for law.
- Grades: letter grades or percentages, varying by province and university.
- Person: follows the style manual, as in the US (APA allows first person for the author's own actions).

**Ireland**
- Spelling: British English. Referencing: Harvard variants and APA 7 common.
- Grades: honours classes similar to the UK (First 70+, 2.1 60–69, 2.2 50–59, Third 40–49), with institutional variation.

**Continental Europe (English-medium programmes)**
- Spelling: either British or American, chosen and applied consistently; some institutions specify one.
- Referencing: APA 7, Harvard, IEEE, and in some countries ISO 690-based styles.
- Levels: Bologna cycles (first = EQF 6, second = EQF 7, third = EQF 8; short cycle = EQF 5).
- Grades: national scales (e.g. 1–10 in the Netherlands, 1.0–5.0 in Germany, 0–20 in France) plus ECTS grades for exchange.
- Theses: some systems expect a separate "Research design" chapter and a defence.

**South Asia (e.g. India, Sri Lanka, Pakistan, Bangladesh)**
- Spelling: usually British-based. Referencing: APA, IEEE (especially engineering and computing), Harvard; follow the department.
- Levels (India): the National Higher Education Qualifications Framework runs from 4.5 (first-year certificate) to 8 (doctorate); treat mappings as indicative.
- Grades: CGPA scales and classes (e.g. First Class, Second Upper) vary by university and regulator.
- Some regulators and universities set formal thesis formats (front matter, certificate pages, declarations); follow them exactly.

**East and Southeast Asia, Middle East, Africa (English-medium)**
- Often follow either US or UK conventions depending on the institution's model, or the accreditation partner for transnational programmes (e.g. a UK university's branch campus follows that university's rules; if so, also use `academic-writing-uk`).

## 7. Writers using English as an additional language

- Preserve meaning first; do not flatten the writer's argument into generic phrasing.
- Fix grammar, articles, prepositions and word choice; keep the writer's sentence structures where they are correct.
- Do not replace a clear simple word with an elaborate one. Simple, precise English scores better than inflated vocabulary.
- AI detectors flag non-native writers' work at much higher rates (Liang et al., 2023). Encourage keeping drafts, notes and version history.

## 8. Example (International, British-based spelling)

Before:
> In today's rapidly evolving landscape, AI isn't just a tool, it's a game-changer. I think RAG plays a pivotal role in enhancing accuracy, showcasing its potential. Studies show it reduces hallucinations by a lot.

After:
> Retrieval-augmented generation (RAG) combines a language model with an external document store, so that responses can draw on retrieved sources. Evidence suggests that this approach may reduce factually unsupported outputs [citation needed: study and figure], although the effect is likely to depend on the quality of the retrieved documents.

Changes: removed staged opener and "not X but Y"; removed "I think" and a contraction; expanded RAG on first use; replaced a vocabulary cluster; hedged the claim; replaced a vague "studies show" with a citation flag. No facts added. (Switch to American spelling if the institution requires it.)

Reminder: check your assessment brief and your institution's generative AI policy, and acknowledge any AI assistance where required.
