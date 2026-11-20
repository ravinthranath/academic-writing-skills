# Academic Writing Skills (UK · US · International)

Three Agent Skills for Claude that help anyone write, edit and review academic work: essays, reports, literature reviews, reflective pieces, proposals, dissertations and theses. Each skill combines **academic writing conventions** with a **humanizer** that removes AI-writing tells, so the result is formal, precise and evidence-based, and does not read like a chatbot.

| Skill | For | Defaults |
|---|---|---|
| [`academic-writing-uk`](skills/academic-writing-uk/SKILL.md) | UK universities | British English, Cite Them Right Harvard, UK marking bands (First / 2:1 / Distinction / Merit) |
| [`academic-writing-us`](skills/academic-writing-us/SKILL.md) | US colleges and universities | American English, APA 7 / MLA 9 / Chicago / IEEE, letter grades, APA first-person rules |
| [`academic-writing-international`](skills/academic-writing-international/SKILL.md) | Everywhere else: Australia, NZ, Canada, Ireland, Europe, South Asia and more | Asks for country and style first; regional profiles; support for writers using English as an additional language |

## What every skill does

- **Edit:** rewrites your draft in academic register and gives a short report of the changes, the gaps to fill, and the word count before and after.
- **Review:** lists the problems (quoted phrase, rule broken, suggested fix) without rewriting.
- **Draft:** writes only from your notes and sources, and flags every gap.
- **Structure:** plans the sections, the word allocation for each, and the evidence each one needs.
- **Reference check:** matches in-text citations against the reference list and flags anything it cannot verify.
- **Declaration:** drafts an AI-use acknowledgement from what you tell it you did.

Rules built in:

- Formal register: no contractions, informal words, rhetorical questions or "you"; precise language; hedging matched to the evidence; acronyms expanded on first use.
- Genre switching (essay, research, technical, business, literature review, reflective, dissertation, proposal, computing/AI, case study). For example, first person is expected in reflective writing.
- Numbered, captioned figures and tables, each discussed in the text. Caption placement follows the referencing style.
- A reproducibility checklist for computing, AI and data-science reports, adapted from the NeurIPS checklist.
- An AI-tell list grounded in corpus research (Kobak et al., 2025; Liang et al., 2024; Juzek & Ward, 2025; Geng & Trotta, 2024), with plain replacements.

## Integrity rules (non-negotiable)

1. **No invention.** The skills never add facts, figures, quotes, studies or references you did not provide. Gaps are flagged as `[citation needed]`. Research shows chatbots fabricate a large share of the references they generate (Walters & Wilder, 2023; Linardon et al., 2025), so every reference must be verified.
2. **Your assessment brief wins** over every default.
3. **Not a detector-evasion tool.** AI detectors are unreliable and biased against non-native English writers (Liang et al., 2023; Jisc). These skills aim for clear writing you can explain and defend. Every output ends with a reminder to follow your institution's generative AI policy and to acknowledge AI use where required.

## Install

**Claude (claude.ai / desktop):** download the skill folder you need (for example `skills/academic-writing-uk`), zip it, and upload it under Settings → Capabilities → Skills. The exact menu location may change; check Anthropic's help centre if it has moved.

**Claude Code:** copy the folder into `~/.claude/skills/` (personal) or `.claude/skills/` (project):

```bash
git clone https://github.com/ravinthranath/academic-writing-skills.git
cp -r academic-writing-skills/skills/academic-writing-uk ~/.claude/skills/
```

Each skill folder is self-contained (`SKILL.md` plus `references/`).

## Example prompts

- "Edit this literature review for my UK Master's report. Cite Them Right Harvard, 2,500 words max."
- "Review my APA 7 paper for informal language and AI-sounding phrases. Don't rewrite."
- "Plan the structure of a business report on remote-work policy, 3,000 words, with an executive summary."
- "Turn my notes into a Gibbs reflective account. First person is fine."
- "Check my reference list against my in-text citations (IEEE)."

## Repository layout

```
skills/                 ← installable skills (generated)
  academic-writing-uk/
  academic-writing-us/
  academic-writing-international/
shared/core.md          ← workflow and rules shared by all three
shared/references/      ← reference files copied into every skill
regions/*.md            ← region-specific frontmatter and conventions
build.py                ← rebuilds skills/ from shared/ and regions/
```

To change something, edit `shared/` or `regions/`, run `python3 build.py`, and commit both the sources and the generated `skills/` folders.

## Contributing

Corrections and improvements are welcome. Please cite an official source (university library guide, regulation or style manual) in the pull request. Policies change every academic year, so date-stamp any policy facts.

## Sources and credits

- The humanizer patterns are adapted for academic register from the open-source [blader/humanizer](https://github.com/blader/humanizer) skill and Wikipedia's *Signs of AI writing* (WikiProject AI Cleanup).
- Phrase categories follow the [Manchester Academic Phrasebank](https://www.phrasebank.manchester.ac.uk/).
- The reproducibility block is adapted from the [NeurIPS Paper Checklist](https://neurips.cc/public/guides/PaperChecklist).
- Style guidance: APA Style blog ([first-person myth](https://apastyle.apa.org/blog/first-person-myth)), [IEEE Reference Guide](https://journals.ieeeauthorcenter.ieee.org/wp-content/uploads/IEEE-Reference-Guide.pdf), [ACM reference formatting](https://www.acm.org/publications/authors/reference-formatting), and Cite Them Right (Pears & Shields).
- Research: Kobak et al. (2025) *Science Advances* 11(27); Liang et al. (2024) arXiv:2404.01268; Liang et al. (2023) *Patterns*; Juzek & Ward (2025) COLING; Geng & Trotta (2024); Walters & Wilder (2023) *Scientific Reports*; Linardon et al. (2025) *JMIR Mental Health*; Jisc National Centre for AI guidance on AI detection.

Conventions were checked against public sources in November 2026 and may change. Always confirm with your assessment brief and institution.

## Licence

MIT. See [LICENSE](LICENSE).

Created by [Ravinthranath Anton Arul Jeevan](https://www.linkedin.com/in/ravinthranath/).
