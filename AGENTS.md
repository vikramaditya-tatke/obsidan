# AGENTS.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This is an **Obsidian knowledge vault** containing technical learning notes, primarily focused on:
- AWS Data Engineering (83 notes in Zettelkasten-style structure)
- ClickHouse databases
- Data Engineering concepts
- Airflow orchestration
- Interview preparation
- Programming fundamentals and algorithms

The vault is synced with OneDrive and managed using Git for version control.

## Key Characteristics

**Vault Structure:**
- **Content Organization**: Topic-based directories (AWS Data Engineer Zettelkasten Lite style, ClickHouse, Data Engineering, Airflow, Interview Preps)
- **Template System**: Standardized note templates in `templates/` directory for consistent structure
- **Rich Linking**: Notes use Obsidian's wiki-link syntax `[[Note Name]]` to create knowledge graphs
- **Frontmatter Metadata**: All structured notes include YAML frontmatter with tags, services, status, domain, and timestamps
- **Total Notes**: 205+ markdown files across the vault

**Obsidian Configuration:**
- Configuration stored in `.obsidian/` directory (excluded from most operations)
- Active plugins include: Copilot, Excalidraw, Omnisearch, Dataview, Calendar, Obsidian Git, PDF Plus, and MCP Tools
- Templates folder configured at `templates/` with time format `HH:mm:ss`

## Working with Vault Content

### Note Templates

Two primary note templates exist for structured content creation:

**AWS Zettelkasten Template** (`templates/AWS-Zettelkasten-Note-Template.md`):
```yaml
---
services: []
tags: [aws]
status: atomic
topic:
domain:
created_at: "YYYY-MM-DD"
---
## {{title}}
### Active Recall
### Key Characteristics
### Implementation & Features
### Use Cases
```

**DEA-C01 Template** (`templates/DEA-C01-Note-Template.md`):
```yaml
---
tags: [aws, v-tag]
status: atomic
topic: Technical Function
domain: DEA-C01 Domain
big_data_v: [V-Category]
flashcard_question: "Question?"
confidence: 1
created_at: {{date}}
questions: []
---
```

### Frontmatter Standards

When creating or modifying notes:
- **services**: List of AWS/tech services discussed
- **tags**: Keywords for categorization
- **status**: Typically "atomic" for complete, focused notes
- **topic**: High-level subject area
- **domain**: Knowledge domain (e.g., "Exam Prep", "DEA-C01 Domain")
- **created_at**: ISO date format (YYYY-MM-DD)

### Content Linking

- Use `[[Note Name]]` syntax for internal links
- Preserve link structure when editing—these power Obsidian's graph view
- Common link patterns: `[[Amazon S3]]`, `[[Public vs Private AWS Services]]`

## Git Workflow

**Current Branch**: `updated-notes` (ahead of `main`)

**Typical Commit Pattern**:
```bash
git add .
git commit -m "docs: Updated notes"
git push origin updated-notes
```

The vault uses descriptive commit messages prefixed with `docs:` or `vault backup:` timestamps.

## Search and Discovery

**Semantic Search**: This codebase is indexed for semantic search via `codebase_semantic_search` tool.

**Grep Search**: Use `grep` for exact matches on:
- Frontmatter fields (e.g., `tags:`, `services:`)
- Service names (e.g., "Amazon S3", "ClickHouse")
- Technical terms and concepts

**File Organization**:
- AWS notes: `AWS Data Engineer Zettelkasten Lite style/`
- ClickHouse notes: `ClickHouse/`
- General DE concepts: `Data Engineering/`
- Root-level notes for cross-cutting topics

## Agent Interaction Guidelines

**When Reading Notes**:
- Respect the Zettelkasten structure—notes are atomic, interconnected knowledge units
- Parse YAML frontmatter to understand context and relationships
- Follow wiki-links to discover related concepts
- Note images are embedded using `![[image_name]]` syntax

**When Creating Notes**:
- Use appropriate template from `templates/` directory
- Generate globally unique titles (Obsidian convention)
- Include comprehensive frontmatter metadata
- Add Active Recall questions where applicable
- Link to related concepts using `[[]]` syntax
- Place in appropriate directory based on topic

**When Modifying Notes**:
- Preserve existing frontmatter structure
- Maintain wiki-link integrity
- Keep Zettelkasten principles: atomic, connected, concept-focused
- Update `created_at` only for new notes; use version control for edit history

**What to Avoid**:
- Don't modify `.obsidian/` configuration files unless explicitly requested
- Don't break existing wiki-links when renaming notes
- Don't remove frontmatter fields—they may be used by plugins
- Don't treat this as a code repository—it's a knowledge management system

## Copilot Custom Prompts

The vault includes custom text transformation prompts in `copilot-custom-prompts/`:
- Emojify, Explain like I am 5, Fix grammar and spelling
- Generate glossary, Generate table of contents
- Make longer/shorter, Remove URLs
- Rewrite as press release/tweet/tweet thread
- Simplify, Summarize, Translate to Chinese

These can be referenced when the user requests similar transformations.

## Platform Considerations

**Windows Environment**:
- Vault path uses Windows-style separators: `C:\Users\vikra\OneDrive\Obsidian Vaults\Vikram's Learning Vault`
- PowerShell is the active shell (version 5.1)
- OneDrive sync may cause temporary file locks

**Path Handling**:
- Always use full paths when referencing vault files
- Be aware of spaces in directory names ("Vikram's Learning Vault")
- Escape paths properly in PowerShell commands

## Special Files

- `.gitignore`: Excludes Obsidian plugin state and remotely-save plugin
- `README.md`: Minimal vault description
- `Application Q&A.md`: Job application preparation content
- `qradar_ingestion_pattern.md`: Technical documentation for QRadar integration
- `Untitled.canvas`: Obsidian Canvas file (visual note arrangement)
