# Romance Co - Breach Investigation

## Challenge Info
- **Platform**: TryHackMe
- **Difficulty**: Medium
- **Status**: In Progress
- **Objective**: Investigate a breach, find user flag and root flag

## Reconnaissance

### Port Scan
```
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.9p1
3000/tcp open  http    Next.js (Node.js)
```

### Technology Stack
- Next.js application on port 3000
- SSH on port 22
- No other services detected on full port scan

## Enumeration Attempts

### Completed
- [x] nmap full port scan (-p-)
- [x] gobuster with common.txt wordlist
- [x] Info disclosure checks (.env, .git, package.json, robots.txt)
- [x] JavaScript chunk analysis (/_next/static/chunks/)
- [x] RSC Flight data check (RSC: 1 header)
- [x] API route enumeration
- [x] CVE-2025-29927 middleware bypass attempt (not vulnerable)
- [x] CGI-bin directory check

### Findings So Far
- Next.js application, appears to be a company website
- No obvious info disclosure
- CVE-2025-29927 headers returned 403 (patched or not applicable)
- No interesting API routes found with common wordlist

## Next Steps
- [ ] Run gobuster with larger wordlist (directory-list-2.3-medium.txt)
- [ ] Focus on finding attacker's backdoor (breach investigation context)
- [ ] Check for hidden Next.js Server Actions
- [ ] Look for unusual files/endpoints the attacker may have left
- [ ] Try vhost enumeration

## Notes
This is a breach investigation scenario -- the attacker has already compromised the system. The approach should focus on finding artifacts the attacker left behind (backdoors, webshells, modified files) rather than finding a new vulnerability to exploit.
