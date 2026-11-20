# Install guide

Pick the option that matches how you use Claude. Menu names and version numbers are correct as of November 2026; if something has moved, check Anthropic's official guides linked at the end.

## 1. Claude app (claude.ai on web, desktop or mobile)

**Before you start**
- Skills need code execution. Under **Settings → Capabilities**, turn on **Create and edit files** (also called **Code execution and file creation**).
- Team and Enterprise: an organisation Owner may need to enable **Code execution** and **Skills** in the organisation settings first.
- Anthropic's help centre lists skills on Free, Pro, Max, Team and Enterprise plans. If you can't see the option, check your plan's Customize page.

**Install**
1. Download one zip from the [latest release](https://github.com/ravinthranath/academic-writing-skills/releases/latest): `academic-writing-uk.zip`, `academic-writing-us.zip` or `academic-writing-international.zip`. You can install more than one.
2. Open **Customize → Skills**, click **+**, choose **Upload a skill**, and select the zip. Upload it as it is; don't unzip it.
3. Check that the skill is toggled **on**.

**Use**
- Ask normally, e.g. "Edit this final-year essay for academic tone (UK, Harvard)". Claude chooses the skill from its description.
- To force it: "Use the academic-writing-uk skill to review this."
- Uploaded skills are private to you unless you share them (sharing is available on Team and Enterprise).

**Troubleshooting**
- **Upload rejected:** use the zip from the release. It contains one folder (e.g. `academic-writing-uk/`) with `SKILL.md` inside. If you build your own zip, zip the folder rather than its contents, and keep the folder name the same as the `name:` in `SKILL.md`.
- **Skills greyed out:** code execution is off (see above).
- **Skill not used:** mention your country and level, or name the skill.

## 2. Claude Code

**Option A: plugin from GitHub (recommended, gets updates)**

```
/plugin install academic-writing --marketplace ravinthranath/academic-writing-skills
```

On older Claude Code versions:

```
/plugin marketplace add ravinthranath/academic-writing-skills
/plugin install academic-writing@academic-writing-skills
```

From a terminal, the same commands work as `claude plugin marketplace add …` and `claude plugin install …`. Check the install with `/plugin` or `claude plugin list`. Skills are namespaced, e.g. `/academic-writing:academic-writing-uk`. To update later, run `/plugin marketplace update academic-writing-skills`.

**Option B: copy a folder**

```bash
git clone https://github.com/ravinthranath/academic-writing-skills.git
cp -r academic-writing-skills/plugins/academic-writing/skills/academic-writing-uk ~/.claude/skills/
```

Use `~/.claude/skills/` for all your projects, or `.claude/skills/` inside a project to share it with collaborators through git. Run `/skills` to list skills, or call one with `/academic-writing-uk`.

**Option C: sync from claude.ai.** Recent Claude Code versions load skills that are enabled on your claude.ai account when you sign in with that account. This does not apply to API-key sessions.

## 3. Claude API and Agent SDK

- **API:** upload a skill folder through the Skills endpoints (`/v1/skills`) and use it in Messages requests with the code execution tool. Check the current beta headers in the [Agent Skills docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview). Skills uploaded on claude.ai do not sync to the API; upload them separately.
- **Agent SDK:** place the skill folder in `.claude/skills/` (project) or `~/.claude/skills/` (user) and enable skills in the SDK options.

## 4. Which skill should I install?

| You study or teach in… | Install |
|---|---|
| England, Wales, Scotland, Northern Ireland | `academic-writing-uk` |
| United States | `academic-writing-us` |
| Australia, New Zealand, Canada, Ireland, Europe, South Asia, elsewhere | `academic-writing-international` |
| A UK university's overseas campus | `academic-writing-uk` |

## Official guides

- [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) (Anthropic help centre)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [Agent Skills overview (API)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
