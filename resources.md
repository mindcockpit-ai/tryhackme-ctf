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

## Password Cracking

| Resource | URL | Use Case |
|----------|-----|----------|
| Hashcat Example Hashes | https://hashcat.net/wiki/doku.php?id=example_hashes | Identify hash types by format |
| John the Ripper | https://www.openwall.com/john/ | CPU-based password cracker |
| SecLists (GitHub) | https://github.com/danielmiessler/SecLists | Wordlists for fuzzing, passwords, usernames, URLs |

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

## CTF Platforms

| Resource | URL | Use Case |
|----------|-----|----------|
| TryHackMe | https://tryhackme.com/dashboard | Guided CTF challenges and learning paths |

## Quick Reference: When to Use What

- **Found a hash?** → Check format at [Hashcat Examples](https://hashcat.net/wiki/doku.php?id=example_hashes), crack with hashcat or [John](https://www.openwall.com/john/)
- **Found a CVE?** → Look up details at [CVE.org](https://www.cve.org/) or [NVD](https://nvd.nist.gov/general), find exploit at [Exploit-DB](https://www.exploit-db.com/)
- **Need wordlists?** → [SecLists](https://github.com/danielmiessler/SecLists) has everything (passwords, directories, subdomains, fuzzing)
- **Suspicious file?** → Upload to [VirusTotal](https://www.virustotal.com/gui/home/upload)
- **Recon on a target?** → [Shodan](https://www.shodan.io/dashboard) for exposed services
- **Cron job privesc?** → Validate schedule at [Crontab Guru](https://crontab.guru/)
- **Windows forensics?** → Check [ADS](https://www.malwarebytes.com/blog/101/2015/07/introduction-to-alternate-data-streams) and [Task Manager](https://www.howtogeek.com/405806/windows-task-manager-the-complete-guide/) for hidden processes
