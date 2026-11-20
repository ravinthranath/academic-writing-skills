# Genres and section-by-section requirements

Identify the genre first. The genre changes the rules for person, structure, headings and summary type. The assessment brief always overrides this file.

## 1. Genre selector

| Genre | Purpose | Typical structure | Person / voice | Key rule |
|---|---|---|---|---|
| Essay | Argue a position | Introduction (thesis), body paragraphs, conclusion; usually no headings | Impersonal, third person (region rules apply) | One continuous argument; no executive summary |
| Research report | Report an investigation | Abstract, Introduction, Literature review, Method, Results, Discussion, Conclusion, References, Appendices | Impersonal; passive common in Method | Results describe; Discussion interprets |
| Technical / lab report | Record procedure and outcome | Abstract, Introduction/Theory, Method/Apparatus, Results, Discussion, Conclusion | Past tense; passive in Method | Enough detail for someone else to replicate |
| Business report | Support a decision | Executive summary, Introduction / terms of reference, Findings, Conclusions, Recommendations, Appendices | Direct, concise; numbered headings; bullets allowed | Executive summary includes recommendations |
| Literature review | Synthesise a field | Thematic sections, not source by source | Impersonal, evaluative | Synthesis and critique, ending in the gap |
| Reflective writing | Learn from experience | Structured by a model (Gibbs, Kolb, Driscoll) | **First person expected** | Description is the smallest part; analysis and action plan carry the marks |
| Dissertation / thesis | Independent research | As research report, plus ethics, limitations, future work | Impersonal; "I" allowed in positionality or reflection if permitted | Aim → objectives → research questions must align with conclusions |
| Project / research proposal | Justify planned work | Title, background, aims/objectives/RQs, method, timeline (Gantt), ethics, risks, references | Future tense | Feasibility and scope are assessed |
| Computing / AI / data science report | Report experiments reproducibly | Introduction, Related work, Data, Method/Model, Experimental setup, Results, Discussion, Limitations, Ethics, Conclusion, Appendices | Impersonal, or "we" if the brief or venue allows | Reproducibility details are mandatory (section 4) |
| Case study | Apply theory to a case | Introduction, case background, analysis using theory, recommendations | Impersonal | Theory must be applied, not just described |

Different universities structure reports differently. Literature-based reports may use themed chapters instead of Method/Results.

## 2. Reflective models (first person allowed)

- **Gibbs (1988):** Description → Feelings → Evaluation → Analysis → Conclusion → Action plan. Best for longer reflections.
- **Kolb (1984):** Concrete experience → Reflective observation → Abstract conceptualisation → Active experimentation.
- **Driscoll (2007):** What? → So what? → Now what? Best for short reflections.

Reflect on a specific experience and draw specific lessons. The analysis stage should still cite theory. Keep the tone professional; avoid emotional language without analysis.

## 3. Section requirements

**Title / cover page.** Title; student name or ID (per anonymous-marking rules); module code and title; module leader; word count; submission date; AI-use declaration if required.

**Abstract (research / technical).** Written last. A stand-alone summary: context, aim, method, key results (with figures), conclusion. Usually 150–300 words, one paragraph (computing and AI abstracts are normally unstructured). Structured abstracts (Background, Methods, Results, Conclusions) are standard in health sciences. No citations or undefined acronyms in most styles.

**Executive summary (business).** A mini version of the report for decision-makers: purpose, key findings, conclusions **and recommendations**. Can be one to several pages for long reports; headings and bullets may be allowed.

**Contents, lists of figures and tables, abbreviations/glossary.** Generate automatically (Word heading styles; LaTeX `\tableofcontents`, `\listoffigures`). A glossary suits non-specialist readers. Still expand acronyms at first use in the text.

**Introduction.** Context → problem → aim (one sentence) → numbered objectives (SMART) → research questions or hypotheses → scope and delimitations → report structure.

**Literature review.** Organise by theme or debate, not by source. Compare, contrast and evaluate methods and evidence. Identify the gap and link it to the research questions. See language-bank.md section 6.

**Methodology.** Research design and rationale; data or participants; materials and tools (with versions); procedure; analysis or evaluation metrics; ethics approval; justification against alternatives. Past tense.

**Results / Findings.** What was found: figures, tables, statistics, no interpretation. Every visual is numbered, captioned and discussed in the text.

**Discussion.** Interpret results against the research questions and the literature; explain unexpected findings with hedged language; state implications. This is where most hedging belongs.

**Limitations.** State the limitation, its likely effect, and any mitigation. Write it as analysis, not apology.

**Conclusion.** Answer each objective or research question in turn. No new data or citations. Do not simply restate the abstract.

**Recommendations.** Actionable, prioritised, justified by the findings. (Business and practice-based reports.)

**Future work.** Research-facing next steps tied to specific limitations.

**References.** One consistent style; every in-text citation listed and vice versa.

**Appendices.** Raw data, extra tables, code listings, questionnaires, consent forms, AI prompt logs if required. Each appendix is referred to in the main text ("see Appendix B"). Never place essential argument in appendices to avoid the word limit.

## 4. Computing / AI / data science: reproducibility block

Adapted from the NeurIPS Paper Checklist. For every experimental report, state:

- Dataset name, version, source, licence; size; train / validation / test splits; preprocessing; data-leakage controls.
- Model architecture and baselines compared against.
- Hyperparameters and how they were chosen (grid search, defaults, prior work).
- Random seeds and number of runs.
- Metrics, with justification for each (why F1 rather than accuracy on imbalanced data).
- Variability: error bars, confidence intervals or significance tests for the main claims, and how they were calculated (e.g. "±1 standard deviation over 5 seeds"). Do not show symmetric error bars that imply impossible values such as negative error rates.
- Compute: hardware (CPU/GPU type, memory), time per run, total compute.
- Code: repository link and commit, or appendix listing; library versions.
- Existing assets: credit creators and state licences.
- Limitations: a dedicated section, honest about scope and failure cases.
- Ethics: personal data, consent, bias and fairness, potential misuse.

## 5. Alignment check (dissertations and research reports)

Build a simple map and confirm every row is complete:

| Objective / RQ | Method used | Result section | Conclusion paragraph |
|---|---|---|---|
| RQ1 | ... | 4.1 | 6, para 1 |

Any objective with no result, or conclusion with no objective, must be fixed before submission.
