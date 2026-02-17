# Agent Team Architecture

## Hub-and-Spoke Model

The agent team follows a hub-and-spoke pattern where the **project-coordinator**
acts as the central orchestrator, delegating to specialist agents based on task type.

```
                    +---------------------+
                    | project-coordinator |
                    |     (Hub / Opus)    |
                    +----------+----------+
                               |
         +----------+----------+----------+----------+
         |          |          |          |          |
    +----+----+ +---+---+ +---+---+ +---+----+ +---+----+
    |solution | | code  | | test  | |research| |database|
    |architect| |reviewer| |  spec | |analyst | |  spec  |
    +---------+ +-------+ +-------+ +--------+ +--------+
```

## Agent Catalog

| Agent | File | Model | Role |
|-------|------|-------|------|
| project-coordinator | `project-coordinator.md` | opus | Smart orchestrator, delegates to specialists |
| solution-architect | `solution-architect.md` | opus | Business workflows, architecture, requirements |
| code-standards-reviewer | `code-standards-reviewer.md` | sonnet | Code review, standards compliance |
| test-specialist | `test-specialist.md` | sonnet | Unit/integration tests, coverage, QA |
| research-analyst | `research-analyst.md` | opus | External research, library evaluation |
| database-specialist | `database-specialist.md` | opus | Query optimization, bulk operations |

## Quick Selection Guide

| Need | Agent |
|------|-------|
| New feature or workflow | solution-architect |
| Code review | code-standards-reviewer |
| Tests needed or failing | test-specialist |
| Unknown error or library | research-analyst |
| Slow query or DB design | database-specialist |
| Multi-step coordination | project-coordinator |

## Delegation Flow

1. Request arrives at **project-coordinator**
2. Coordinator analyzes and identifies required expertise
3. Delegates to appropriate specialist(s)
4. Specialist completes work and reports back
5. Coordinator synthesizes results
6. **code-standards-reviewer** performs final quality gate (mandatory)
