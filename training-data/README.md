# Training Data for tryhackme-ctf - Mistral Fine-tuning

## Purpose

Training data extracted from tryhackme-ctf development sessions for fine-tuning Mistral LLM models on cybersecurity, CTF methodology, and penetration testing domains.

## Project Context

**tryhackme-ctf** is a repository of TryHackMe CTF (Capture The Flag) challenge writeups and security learning materials. It uses the cognitive-core `ctf-pentesting` skill pack and `security-analyst` agent for structured CTF methodology. Contains challenge writeups, Python exploit scripts (JWT attacks, enumeration tools), a progress tracker, and curated security resource bookmarks.

## Directory Structure

```
training-data/
├── raw/                    # Raw conversation exports (markdown)
├── alpaca/                 # Alpaca instruction format (JSONL)
├── sharegpt/               # ShareGPT conversation format (JSONL)
├── qa_pairs/               # Simple Q&A pairs (JSONL)
├── metadata/               # Statistics and indexes
└── README.md               # This file
```

## Domain Categories

| Domain | Description | Tags |
|--------|-------------|------|
| CTF Methodology | Structured approach to Capture The Flag challenges | `ctf`, `methodology`, `hacking` |
| Web Exploitation | Information disclosure, default credentials, authentication bypass | `web-exploit`, `auth-bypass`, `recon` |
| JWT Attacks | JWT none algorithm bypass and token manipulation | `jwt`, `token`, `authentication` |
| Reconnaissance | Information gathering, enumeration, OSINT | `recon`, `enumeration`, `osint` |
| Python Exploits | Security tooling and exploit scripts in Python | `python`, `exploit`, `scripting` |
| Network Security | Network analysis, port scanning, service enumeration | `network`, `scanning`, `services` |
| Forensics | Breach investigation and digital forensics | `forensics`, `investigation`, `breach` |

## Formats

### Alpaca (Instruction Format)
```json
{"instruction": "...", "input": "...", "output": "..."}
```
One entry per line in JSONL files. Best for single-turn instruction following.

### ShareGPT (Conversation Format)
```json
{"conversations": [{"from": "human", "value": "..."}, {"from": "gpt", "value": "..."}]}
```
One conversation per line. Best for multi-turn dialogue fine-tuning.

### Q&A Pairs
```json
{"question": "...", "answer": "...", "domain": "...", "tags": [...]}
```
Simple question-answer pairs with domain metadata for filtering.

## Usage

```bash
# Count entries per format
wc -l alpaca/*.jsonl
wc -l sharegpt/*.jsonl
wc -l qa_pairs/*.jsonl

# Validate JSONL format
python3 -c "import json; [json.loads(l) for l in open('alpaca/data.jsonl')]"

# Filter by domain tag
python3 -c "
import json
with open('qa_pairs/data.jsonl') as f:
    for line in f:
        entry = json.loads(line)
        if 'ctf' in entry.get('tags', []):
            print(entry['question'])
"
```

## Quality Guidelines

- Technical accuracy required
- No PII or credentials
- Complete context in each entry
- Proper code formatting
- Domain tags for filtering

## Sensitive Data Exclusions

| Type | Reason |
|------|--------|
| TryHackMe credentials | Platform authentication |
| VPN configuration files | Network access credentials |
| Target IP addresses | Challenge infrastructure |
| Flag values | CTF answers (educational integrity) |
| SSH keys and passwords | Challenge-specific secrets |
| API keys for security tools | Third-party service access |

## Supervised by

Training Data Curator Agent
