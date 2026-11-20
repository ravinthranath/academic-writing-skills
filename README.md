# Academic Writing Skills for Claude (UK · US · International)

Three skills that help anyone write, edit and review academic work, from pre-university coursework to a PhD thesis. They also act as a **humanizer**: they remove AI-sounding writing without inventing sources. Each skill is set to your **level of study** and your **university's standards**.

| Skill | For | Defaults |
|---|---|---|
| [`academic-writing-uk`](plugins/academic-writing/skills/academic-writing-uk/SKILL.md) | UK universities and colleges | British English, Harvard (Cite Them Right), FHEQ levels 3–8 and SCQF 7–12, First / 2:1 / Merit / Distinction |
| [`academic-writing-us`](plugins/academic-writing/skills/academic-writing-us/SKILL.md) | US colleges and universities | American English, APA 7 / MLA 9 / Chicago / IEEE, first-year composition to dissertation, letter grades |
| [`academic-writing-international`](plugins/academic-writing/skills/academic-writing-international/SKILL.md) | Everywhere else: Australia, NZ, Canada, Ireland, Europe, South Asia and more | Asks your country first; EQF, AQF, NZQCF and NHEQF levels; support for writers using English as an additional language |

---

## ⚡ Quick start (2 minutes)

### Claude app (web, desktop or mobile): no coding needed

1. **Download** the zip for your country from the [latest release](https://github.com/ravinthranath/academic-writing-skills/releases/latest):
   - [academic-writing-uk.zip](https://github.com/ravinthranath/academic-writing-skills/releases/latest/download/academic-writing-uk.zip)
   - [academic-writing-us.zip](https://github.com/ravinthranath/academic-writing-skills/releases/latest/download/academic-writing-us.zip)
   - [academic-writing-international.zip](https://github.com/ravinthranath/academic-writing-skills/releases/latest/download/academic-writing-international.zip)
2. In Claude, open **Customize → Skills**, click **+**, choose **Upload a skill**, and select the zip. Don't unzip it first.
3. Make sure the skill is **switched on**.
4. Paste your work and ask, for example:
   > *Review my 2,500-word second-year sociology essay against UK Level 5 standards. Don't rewrite it.*

If you can't see Skills, turn on code execution (called **Create and edit files** or **Code execution and file creation**) under **Settings → Capabilities**. On Team and Enterprise plans an admin may need to enable Skills first. Menu names change from time to time, so see Anthropic's [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) guide.

### Claude Code: one command

```
/plugin install academic-writing --marketplace ravinthranath/academic-writing-skills
```

On older versions, use two steps instead:

```
/plugin marketplace add ravinthranath/academic-writing-skills
/plugin install academic-writing@academic-writing-skills
```

All three skills are then available. Claude picks one automatically, or you can call one by name: `/academic-writing:academic-writing-uk`.

More options (copying folders, API and Agent SDK, troubleshooting) are in **[INSTALL.md](INSTALL.md)**.

---

## How to use it

Just ask in plain language. The more context you give (**level, country, task, word limit, referencing style, the assessment brief**), the better the result.

| You want to… | Try asking |
|---|---|
| Polish a draft | "Edit this for academic tone. Final-year UK dissertation, Harvard, 10,000 words." |
| Get feedback only | "Review this Master's literature review. What band does it read at, and how do I reach Distinction?" |
| Remove AI-sounding phrasing | "Humanize this paragraph but keep it formal and keep all my citations." |
| Understand the question | "What does 'critically evaluate' mean for a Level 6 essay?" |
| Plan the structure | "Plan a 3,000-word business report with an executive summary." |
| Write a reflection | "Turn my notes into a Gibbs reflective account. First person is fine." |
| Check references | "Check my in-text citations against my reference list (APA 7)." |
| Declare AI use | "Write an AI-use acknowledgement: I used Claude to check grammar only." |

**Tip:** attach or paste your **assessment brief and marking rubric**. The skill always puts them first.

## What's inside

**Levels of study and university standards**
- A six-step level selector: pre-university (L3), first year, intermediate, final year / honours, Master's, doctoral. It maps to UK FHEQ and SCQF, Europe's EQF and Dublin descriptors, Australia's AQF, New Zealand's NZQCF, India's NHEQF and US stages (WPA, AAC&U VALUE, DQP).
- What each level expects for criticality, sources, method and originality, with checklists and common weaknesses.
- Grade bands and what separates them (First, 2:1, 2:2; Distinction, Merit, Pass; HD, D, C, P; US rubrics), plus doctoral examination expectations.
- Bloom and SOLO taxonomies, the meaning of command words, and **the same paragraph written at four levels**.
- Order of authority: **your brief → your university → national descriptors → generic rules**.

**Academic conventions**
- Formal register: no contractions or informal words, precise language, hedging matched to the evidence, acronyms expanded at first use, consistent terminology.
- Ten genres: essay, research, technical/lab, business, literature review, reflective, dissertation, proposal, computing/AI, case study.
- Numbered, captioned figures and tables that the text discusses, with caption placement set by referencing style.
- Referencing styles (Harvard, APA, IEEE, ACM, MLA, Chicago, Vancouver, OSCOLA and more), including how to cite AI tools.
- A reproducibility checklist for computing, AI and data-science reports, adapted from the NeurIPS checklist.

**Humanizer**
- Removes AI-writing patterns such as "not just X but Y", inflated significance, vague "studies show" claims, participle tails, forced triads, chatbot leftovers and citation artefacts.
- Includes a list of vocabulary that corpus studies flag as overused by AI (Kobak et al., 2025; Liang et al., 2024; Juzek & Ward, 2025; Geng & Trotta, 2024), with plain replacements.

## Integrity rules (always on)

1. **No invention.** The skills never add facts, figures, quotes, studies or references you didn't provide. Gaps are marked `[citation needed]`. Chatbots often fabricate references (Walters & Wilder, 2023; Linardon et al., 2025), so verify every one.
2. **Your brief and your university come first.**
3. **Not a detector-evasion tool.** AI detectors are unreliable and biased against non-native English writers (Liang et al., 2023; Jisc). These skills aim for clear work that you can explain and defend. Every output reminds you to follow your institution's generative-AI policy.
4. **No fake level-ups.** Higher bands come from your own reading and analysis. The skill shows you where more is needed but doesn't fake it.

## Repository layout

```
.claude-plugin/marketplace.json      ← makes this repo a Claude Code plugin marketplace
plugins/academic-writing/
  .claude-plugin/plugin.json
  skills/                            ← the three installable skills (generated)
    academic-writing-uk/
    academic-writing-us/
    academic-writing-international/
shared/core.md                       ← workflow shared by all three skills
shared/references/                   ← reference files copied into every skill
regions/*.md                         ← country-specific rules and frontmatter
build.py                             ← rebuilds the skills from shared/ and regions/
```

To change something, edit `shared/` or `regions/`, run `python3 build.py`, and commit both the sources and the generated skills. Check with `claude plugin validate .`.

## Contributing

Corrections and improvements are welcome. Please cite an official source (a qualification framework, university regulation, library guide or style manual) in your pull request. Policies change every academic year, so date-stamp any policy facts.

## Sources and credits

- **Level frameworks:** [QAA Frameworks for HE Qualifications (2024)](https://www.qaa.ac.uk/docs/qaa/quality-code/the-frameworks-for-higher-education-qualifications-of-uk-degree-awarding-bodies-2024.pdf); [QAA Doctoral Degree Characteristics Statement (2020)](https://www.qaa.ac.uk/docs/qaa/quality-code/doctoral-degree-characteristics-statement-2020.pdf); [EQF level descriptions (Europass)](https://europass.europa.eu/en/description-eight-eqf-levels); the Dublin descriptors (QF-EHEA); Australian Qualifications Framework; [University of Toronto degree level expectations](https://www.vpacademic.utoronto.ca/academic-programs-change/program-types/degree-diploma-certificate-programs/degree-level-expectations/); [Lumina Degree Qualifications Profile](https://www.luminafoundation.org/files/resources/dqp.pdf); the WPA Outcomes Statement for First-Year Composition; AAC&U VALUE rubrics; UGC (India) curriculum frameworks.
- **Grade descriptors:** QAA 2024 classification descriptors; published university regulations (e.g. Swansea, Bristol, Nottingham, Warwick, Edinburgh).
- **Humanizer:** patterns adapted for academic register from the open-source [blader/humanizer](https://github.com/blader/humanizer) skill and Wikipedia's *Signs of AI writing* (WikiProject AI Cleanup).
- **Language:** categories follow the [Manchester Academic Phrasebank](https://www.phrasebank.manchester.ac.uk/).
- **Reproducibility:** adapted from the [NeurIPS Paper Checklist](https://neurips.cc/public/guides/PaperChecklist).
- **Style guides:** APA Style blog ([first-person myth](https://apastyle.apa.org/blog/first-person-myth)), [IEEE Reference Guide](https://journals.ieeeauthorcenter.ieee.org/wp-content/uploads/IEEE-Reference-Guide.pdf), [ACM reference formatting](https://www.acm.org/publications/authors/reference-formatting), Cite Them Right (Pears & Shields).
- **Research:** Kobak et al. (2025) *Science Advances*; Liang et al. (2024) arXiv:2404.01268; Liang et al. (2023) *Patterns*; Juzek & Ward (2025) COLING; Geng & Trotta (2024); Walters & Wilder (2023) *Scientific Reports*; Linardon et al. (2025) *JMIR Mental Health*; Jisc guidance on AI detection.

Conventions were checked against public sources in November 2026 and may change. Descriptors are reference points, not marking schemes, so always confirm with your assessment brief and institution.

## Licence

MIT. See [LICENSE](LICENSE).

Created by [Ravinthranath Anton Arul Jeevan](https://www.linkedin.com/in/ravinthranath/).
