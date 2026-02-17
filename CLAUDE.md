# Project Development Guide

## Quick Reference

| Item | Value |
|------|-------|
| **Project** | tryhackme-ctf |
| **Language** | python |
| **Architecture** | none |
| **Database** | none |
| **Main Branch** | main |
| **Test Command** | `pytest` |
| **Lint Command** | `ruff check $1` |

## Architecture

Pattern: **none**
Source root: `scripts`
Test root: `tests`

<!-- TODO: Document your architecture layers and patterns here -->

## Code Standards

- Follow python community best practices
- Run lint before every commit
- All new code must have tests
- Git commits: `type(scope): subject` (conventional format)
- NO AI/tool references in commit messages

## Key Rules

<!-- TODO: Add your project's critical rules here -->
<!-- These survive context compaction and are always visible -->

1. Follow the architecture pattern defined above
2. Use parameterized queries for all database operations
3. Run lint before every commit

## Agents

See `.claude/AGENTS_README.md` for the agent team documentation.

## Development Workflow

1. Check current branch and status
2. Implement changes following architecture pattern
3. Run tests: `pytest`
4. Run lint: `ruff check $1`
5. Commit with conventional format
