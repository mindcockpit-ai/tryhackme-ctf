# Security Resources & Bookmarks

Curated reference links organized by category for CTF challenges and security learning.

## Vulnerability Databases & Research

| Resource | URL | Use Case |
|----------|-----|----------|
| Exploit-DB | https://www.exploit-db.com/ | Public exploit database, searchsploit companion |
| CVE.org | https://www.cve.org/ | Official CVE identifier registry |
| NVD (NIST) | https://nvd.nist.gov/general | Vulnerability scoring (CVSS), detailed analysis |
| VirusTotal | https://www.virustotal.com/gui/home/upload | File/URL/hash scanning with 70+ AV engines |

## Reconnaissance & OSINT

| Resource | URL | Use Case |
|----------|-----|----------|
| Shodan | https://www.shodan.io/dashboard | Internet-connected device search engine |

## Web Exploitation Tools

| Resource | URL | Use Case |
|----------|-----|----------|
| OWASP ZAP | https://www.zaproxy.org/ | Free web app scanner and intercepting proxy (Burp Suite alternative) |
| Webhook.site | https://webhook.site | Capture and inspect HTTP requests (SSRF, XSS callbacks, OOB) |
| RequestBin | https://requestbin.net/ | Capture incoming HTTP requests in real time |

## Reverse Shells

| Resource | URL | Use Case |
|----------|-----|----------|
| RevShells | https://www.revshells.com/ | Interactive reverse shell generator for all languages, with encoding |

## CTF Tools (Encoding, Steganography, Forensics)

| Resource | URL | Use Case |
|----------|-----|----------|
| CyberChef | https://gchq.github.io/CyberChef/ | Browser-based encoding, decoding, encryption, hashing swiss army knife |
| dCode.fr | https://www.dcode.fr/en | Cipher identifier and solver for 200+ ciphers |
| Aperi'Solve | https://www.aperisolve.com/ | Online stego analysis (runs zsteg, binwalk, foremost, strings in one pass) |

## Password Cracking

| Resource | URL | Use Case |
|----------|-----|----------|
| Hashcat Example Hashes | https://hashcat.net/wiki/doku.php?id=example_hashes | Identify hash types by format |
| John the Ripper | https://www.openwall.com/john/ | CPU-based password cracker |
| SecLists (GitHub) | https://github.com/danielmiessler/SecLists | Wordlists for fuzzing, passwords, usernames, URLs |

## Cheat Sheets & Reference

| Resource | URL | Use Case |
|----------|-----|----------|
| OWASP Cheat Sheet Series | https://cheatsheetseries.owasp.org/ | Authoritative references for SQLi, XSS, auth, CSRF, and more |
| Wireshark Cheat Sheet | https://hackertarget.com/wireshark-tutorial-and-cheat-sheet/ | Practical Wireshark filters and PCAP analysis reference |

## Network Tools

| Resource | URL | Use Case |
|----------|-----|----------|
| Wireshark | https://www.wireshark.org/ | Packet analyzer for network forensics and PCAP challenges |

## Binary Exploitation / Reverse Engineering

| Resource | URL | Use Case |
|----------|-----|----------|
| Ghidra | https://github.com/NationalSecurityAgency/ghidra | NSA's free RE framework (decompiler, disassembler) |
| pwntools Docs | https://docs.pwntools.com/en/stable/ | Python library for CTF exploits (ROP chains, payload crafting) |
| Nightmare | https://guyinatuxedo.github.io/ | CTF-based intro to binary exploitation with 90+ walkthroughs |

## Linux & System Administration

| Resource | URL | Use Case |
|----------|-----|----------|
| Linux Man Pages | https://linux.die.net/man/ | Command reference and documentation |
| Crontab Guru | https://crontab.guru/ | Cron schedule expression editor |
| Crontab Generator | https://crontab-generator.org/ | Generate crontab entries interactively |
| Vim Cheat Sheet | https://vim.rtorr.com/ | Quick vim command reference |

## Windows

| Resource | URL | Use Case |
|----------|-----|----------|
| Windows Task Manager Guide | https://www.howtogeek.com/405806/windows-task-manager-the-complete-guide/ | Process analysis, performance monitoring |
| Alternate Data Streams | https://www.malwarebytes.com/blog/101/2015/07/introduction-to-alternate-data-streams | NTFS ADS for hiding data, forensics |
| Microsoft Learn | https://learn.microsoft.com/en-us/ | Official Microsoft documentation |
| Windows Taskbar Customization | https://support.microsoft.com/en-us/windows/customize-the-taskbar-in-windows-0657a50f-0cc7-dbfd-ae6b-05020b195b07 | Windows 10 taskbar settings |

## CTF Platforms & Practice

| Resource | URL | Use Case |
|----------|-----|----------|
| TryHackMe | https://tryhackme.com/dashboard | Guided CTF challenges and learning paths |
| Hack The Box | https://www.hackthebox.com/ | Active machines, retired walkthroughs, CTF events |
| PortSwigger Web Security Academy | https://portswigger.net/web-security | Free lab-based web hacking curriculum (from Burp Suite makers) |
| OverTheWire | https://overthewire.org/wargames/ | SSH wargames starting with Bandit (Linux fundamentals) |
| PicoCTF | https://picoctf.org/ | Beginner-friendly CTF with permanent practice gym |
| VulnHub | https://www.vulnhub.com/ | Downloadable vulnerable VMs for offline practice |
| Root-Me | https://www.root-me.org/ | 470+ challenges across web, forensics, network, reversing |
| pwn.college | https://pwn.college/ | University-level binary exploitation course with dojos |
| CTFtime | https://ctftime.org/ | Global CTF competition calendar, team rankings, writeups |

## Quick Reference: When to Use What

- **Got a foothold?** → [RevShells](https://www.revshells.com/) to generate the right reverse shell command
- **Encoded data?** → [CyberChef](https://gchq.github.io/CyberChef/) for any encoding/decoding/crypto operation
- **Found a hash?** → Check format at [Hashcat Examples](https://hashcat.net/wiki/doku.php?id=example_hashes), crack with hashcat or [John](https://www.openwall.com/john/)
- **Found a CVE?** → Look up at [CVE.org](https://www.cve.org/) or [NVD](https://nvd.nist.gov/general), find exploit at [Exploit-DB](https://www.exploit-db.com/)
- **Need wordlists?** → [SecLists](https://github.com/danielmiessler/SecLists) has everything (passwords, directories, subdomains, fuzzing)
- **Testing SSRF/XSS?** → [Webhook.site](https://webhook.site) to catch callbacks
- **Suspicious file?** → Upload to [VirusTotal](https://www.virustotal.com/gui/home/upload)
- **Recon on a target?** → [Shodan](https://www.shodan.io/dashboard) for exposed services
- **Web app testing?** → [ZAP](https://www.zaproxy.org/) as intercepting proxy
- **PCAP file?** → [Wireshark](https://www.wireshark.org/) with [cheat sheet](https://hackertarget.com/wireshark-tutorial-and-cheat-sheet/)
- **Unknown cipher?** → [dCode.fr](https://www.dcode.fr/en) to identify and solve
- **Stego challenge?** → [Aperi'Solve](https://www.aperisolve.com/) runs all tools in one pass
- **Cron job privesc?** → Validate schedule at [Crontab Guru](https://crontab.guru/)
- **Binary RE?** → [Ghidra](https://github.com/NationalSecurityAgency/ghidra) for decompilation
- **Learn web hacking?** → [PortSwigger Academy](https://portswigger.net/web-security) (free, hands-on)
- **Learn binary exploitation?** → [Nightmare](https://guyinatuxedo.github.io/) (CTF-based, 90+ challenges)
- **Windows forensics?** → Check [ADS](https://www.malwarebytes.com/blog/101/2015/07/introduction-to-alternate-data-streams) and [Task Manager](https://www.howtogeek.com/405806/windows-task-manager-the-complete-guide/)
