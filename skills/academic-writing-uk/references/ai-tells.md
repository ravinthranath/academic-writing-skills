# AI-writing tells in academic text

Use this file in pass 2 (humanize). It adapts general humanizer rules to the academic register. Academic rules win over general humanizer advice. Do not add "I", contractions, jokes, asides or personal opinions to make text "sound human". Make it specific, evidenced and plainly worded instead.

## How to judge a tell

- **S (fix on sight):** one instance is enough.
- **M (fix when repeated or clustered):** act when it appears 2+ times in a passage or sits next to other tells.
- **W (weak alone):** act only when other tells are present.
- Corpus markers show patterns across thousands of papers. They cannot prove one text is AI-written. Many are ordinary words (potential, findings, within). Look for **density and clustering**, not single words.
- Introductions and Discussions show the most AI-style vocabulary in published research, so check them first. One 2026 preprint found it in 68% of Discussion paragraphs and 32% of Methods paragraphs.

## A. Staging instead of stating (strongest)

1. **Not X but Y (S).** "This is not merely a tool but a paradigm shift." "It is not about X; it is about Y." "Not A. Not B. Just C." Keep only when the negative half corrects a view the literature actually holds, and cite that view.
   - Before: "RAG is not just an add-on; it is a fundamental rethinking of retrieval."
   - After: "RAG adds a retrieval step before generation, so responses can draw on documents outside the model's training data (Lewis et al., 2020)." (Keep a citation only if the user supplied or verified it.)
2. **Dramatic closers (S).** "This distinction matters." "And that changes everything." A sentence that restates what the paragraph just showed. Cut, or replace with the implication for the research question.
3. **Pseudo-profound framing (S).** "At its core", "the real question is", "at the end of the day", "X is the currency of Y". Replace with the actual claim.
4. **Staged openers (S).** "In today's rapidly evolving world", "In an era of", "Since the dawn of time", "Let us delve into", "It is worth noting that", "It is important to note that", "When it comes to". Start with the topic and its context.
5. **Arguing with nobody (S).** "Some might argue...", "One might think..." with no source. Cite the actual opposing position or delete.
6. **Importance flags (S).** "This matters because", "why this matters", "just as importantly". Delete the flag and state the consequence with evidence.

## B. Inflation and borrowed authority

7. **Inflated significance (S).** "plays a pivotal/vital/crucial role", "stands as a testament", "marks a paradigm shift", "has revolutionised", "a key turning point", "the evolving landscape of", "paving the way for", "the future looks promising". Keep the fact; drop the significance claim unless a source supports it.
   - Before: "Transformers have revolutionised NLP, marking a pivotal moment in AI history."
   - After: "Transformer models replaced recurrent architectures as the dominant approach in many NLP benchmarks after 2018 [citation needed]."
8. **Vague attribution (S in academic text).** "Studies show", "research suggests", "experts argue", "it is widely accepted", "scholars have noted", "many researchers". Name author and year, or flag [citation needed].
9. **Vague association (M).** "is associated with", "is linked to", "is tied to" where the source states a specific relationship (causes, predicts, correlates at r = ...). Use the precise relationship, or keep "associated with" when that is exactly what the evidence shows.
10. **Participle tails (M).** ", highlighting the importance of...", ", underscoring...", ", showcasing...", ", ensuring...", ", contributing to...", ", fostering...", ", reflecting...". Delete, or turn into a separate evidenced sentence.
11. **Copula avoidance (M).** "serves as", "stands as", "functions as", "represents", "boasts", "offers". Use "is" or "has" where that is what is meant.
12. **Evaluative padding (M).** remarkable, notable, noteworthy, commendable, valuable, meaningful, robust (non-technical), comprehensive, significant (when not statistical). Describe the property or give the figure. Reserve "significant" for statistical significance with the test and p-value.

## C. Rhythm and structure by rule

13. **Forced triads (M).** Three adjectives, three examples, three benefits, every time. Use as many items as the evidence supports.
14. **Uniform sentence length (M).** Every sentence 15 to 25 words, only commas and full stops. Mix longer analytical sentences with short claims. Use semicolons and colons where the logic calls for them.
15. **Repeated openers (M).** "This... This... This..." or "Additionally... Furthermore... Moreover..." in sequence. Vary, merge, or drop the connector.
16. **Stacked hedges (M).** "could potentially possibly suggest". Use one hedge per claim, matched to the evidence (see language-bank.md).
17. **Elegant variation (M).** Calling the same thing "the model", "the system", "the framework", "the architecture" in turn. Academic writing needs consistent terms: define once, then repeat the same noun.
18. **Paragraph-end summaries (M).** A final sentence that restates the paragraph. Replace with a link to the next point or to the research question, or cut.
19. **Document narration (M).** "This section will explore...", "The following paragraphs discuss...", "In conclusion, this report has shown..." in every section. Keep one structure statement in the introduction. Elsewhere, make the point.
20. **Formulaic endings (M).** "Despite these challenges, the future is bright", generic "Challenges and Future Directions" with no specifics. Replace with specific limitations and specific future work tied to the findings.

## D. Formatting and residue

21. **Chatbot residue (S).** "Certainly!", "Great question", "I hope this helps", "Let me know if you would like...", "Here is a revised version". Delete.
22. **Citation artefacts (S).** `oaicite`, `contentReference`, `turn0search0`, `[cite: 1]`, `【12†L3-L9】`, `[web:1]`, `utm_source=chatgpt.com`. Delete. **Never** replace with an invented citation. Flag [citation needed].
23. **Markdown leakage (S).** `**bold**`, `##`, `---`, emoji, arrow bullets in a Word or PDF submission. Convert to the document's heading styles and prose.
24. **Bold inline headers in lists (M).** "**Scalability:** The system scales..." Turn into prose unless the brief allows bullet points (business reports often do).
25. **Placeholders (S).** [Your Name], [Insert data], 20XX, {module code}. Fill from the user's information or flag. Never guess.
26. **Knowledge-cutoff hedges (S).** "As of my last update", "based on available information", "while specific details are limited". Delete; verify the fact or flag it.

## E. Vocabulary watch-list (academic corpora)

Treat as M: act when two or more appear in one paragraph, or one appears in an inflated pattern above.

**Strongest corpus markers (Kobak et al., 2025; Liang et al., 2024; Juzek & Ward, 2025; Geng & Trotta, 2024):**
delve(s), underscore(s), showcasing, pivotal, intricate(ly), realm, meticulous(ly), garner(ed), grappling, notably, additionally, comprehensive, crucial, enhance/enhancing, insights, valuable, nuanced, surpass(es), align(ing) with, excel(s), interplay, landscape, tapestry, potential, findings, within, across, particularly, exhibited, highlights, offering.

**Other frequent ones:** multifaceted, noteworthy, commendable, groundbreaking, pioneering, poised, paving the way, propelling, pressing, pronounced, remarkable, renowned, necessitate, pinpoint, leverage, harness, foster, bolster, navigate, embark, unlock, unveil, seamless, robust (non-technical), ever-evolving, cutting-edge, game-changer, testament, beacon, journey (for a process), deep dive.

**Plain replacements**

| AI-style | Plainer academic choice |
|---|---|
| delve into, explore (as filler) | examine, investigate, analyse |
| underscore, highlight, showcase | show, demonstrate, indicate |
| leverage, harness, utilise | use, apply |
| foster, cultivate | encourage, support, develop |
| enhance, bolster, elevate | improve, increase, strengthen (state by how much) |
| garner | receive, attract, obtain |
| align with | match, be consistent with |
| navigate | manage, address, deal with |
| pivotal, crucial, vital, key | important, central (or cut) |
| intricate | complex |
| meticulous | careful, systematic, detailed |
| comprehensive | full, detailed, extensive (or say what it covers) |
| multifaceted | has several dimensions (then name them) |
| landscape, realm | field, area, sector |
| interplay | interaction, relationship |
| insights | findings, results, evidence (or state the insight) |
| notably, additionally, furthermore, moreover | also, in addition, however (or cut; vary) |
| a testament to | evidence of (with citation) |
| serves as, stands as | is |

**Abstract-verb rewrite rule.** Replace a sentence built on abstract verbs with a concrete claim.
- Before: "This study delves into the intricate interplay between data quality and model performance."
- After: "This study measures how label noise in the training set affects F1 score on the [dataset] test split."

## F. What to leave alone

- Passive voice in Methods and to keep focus on the research.
- Calibrated hedging, discipline terms, defined technical vocabulary.
- Formal connectors used in moderation: however, therefore, in contrast, consequently.
- Quoted text, titles, proper nouns, code, equations.
- A user's established voice in their own earlier writing (within academic rules).

Removing these markers improves clarity. It does not and should not aim to "beat" AI detectors. See integrity-and-ai-use.md.
