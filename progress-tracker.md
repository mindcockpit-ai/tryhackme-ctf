# Security Learning Progress

## TryHackMe Profile
- **Username**: wolaschka
- **League**: Gold League #2
- **Points**: 976

## Skill Matrix

| Skill Area | Level | Notes |
|---|---|---|
| Port Scanning (nmap) | ✅ | Quick + full scans, version detection |
| Directory Enumeration (gobuster) | ✅ | Common wordlists, extension filtering |
| Information Disclosure | ✅ | robots.txt, .env, .git, source code |
| JWT Analysis & Attacks | ✅ | None algorithm bypass, cookie tampering |
| Web Source Code Analysis | 🔄 | JS chunk analysis, RSC payloads |
| Next.js Attacks | 🔄 | CVE-2025-29927 tested, Server Actions |
| Forensics / Log Analysis | 🔄 | Breach investigation in progress |
| SQL Injection | ⬜ | |
| SSTI | ⬜ | |
| Command Injection | ⬜ | |
| LFI/RFI | ⬜ | |
| XSS | ⬜ | |
| SSRF | ⬜ | |
| File Upload Attacks | ⬜ | |
| Privilege Escalation (Linux) | ⬜ | |
| Privilege Escalation (Windows) | ⬜ | |
| Password Cracking | ⬜ | |
| Reverse Shells | ⬜ | |
| Buffer Overflow | ⬜ | |
| Active Directory | ⬜ | |

Legend: ⬜ Not yet | 🔄 Learning | ✅ Practiced | 🏆 Mastered

## Completed Challenges

### 01 - Cupid's Vault
- **Platform**: TryHackMe
- **Flag**: `THM{l0v3_is_in_th3_r0b0ts_txt}`
- **Attack Path**: nmap → robots.txt → /cupids_secret_vault/ → hardcoded password → admin login → flag
- **Techniques**: Information disclosure, default credentials
- **Developer Lesson**: robots.txt is public; never hardcode passwords
- **Difficulty**: Easy

### 02 - ValenFind
- **Platform**: TryHackMe
- **Flag**: `THM{v4l3nt1n3_jwt_c00k13_t4mp3r_4dm1n_sh0p}`
- **Attack Path**: Register → tryheartme_jwt cookie → decode JWT → none algorithm bypass → forge admin token → buy ValenFlag
- **Techniques**: JWT analysis, base64, algorithm confusion
- **Developer Lesson**: Enforce JWT algorithm server-side, never trust client alg header
- **Difficulty**: Easy-Medium

### 03 - Romance Co (In Progress)
- **Platform**: TryHackMe
- **Target**: Port 3000 (Next.js), Port 22 (SSH)
- **Objective**: Breach investigation - find user flag and root flag
- **Status**: Enumeration phase, searching for attacker backdoor

## Statistics
- Total challenges completed: 2
- Challenges in progress: 1
- Techniques practiced: 4 (port scanning, dir enum, info disclosure, JWT)
- Current streak: Active
