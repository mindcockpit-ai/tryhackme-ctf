# tryhackme-ctf

TryHackMe CTF challenge writeups and security learning, powered by [Cognitive Core](https://github.com/mindcockpit-ai/cognitive-core) with the `ctf-pentesting` skill pack.

## Setup

```bash
git clone https://github.com/mindcockpit-ai/tryhackme-ctf.git
cd tryhackme-ctf
claude
```

The Cognitive Core `ctf-pentesting` skill and `security-analyst` agent load automatically, providing structured methodology for CTF challenges.

## Challenges

| # | Name | Difficulty | Status | Techniques |
|---|------|------------|--------|------------|
| 01 | [Cupid's Vault](challenges/01-cupids-vault/writeup.md) | Easy | Completed | Info disclosure, default creds |
| 02 | [ValenFind](challenges/02-valenfind/writeup.md) | Easy-Medium | Completed | JWT none algorithm bypass |
| 03 | [Romance Co](challenges/03-romance-co/writeup.md) | Medium | In Progress | Next.js, breach investigation |

## Progress

See [progress-tracker.md](progress-tracker.md) for skill matrix and statistics.

## Scripts

- `scripts/jwt-none-attack.py` - JWT none algorithm attack tool

## License

MIT
