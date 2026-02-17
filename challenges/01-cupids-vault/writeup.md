# Cupid's Vault

## Challenge Info
- **Platform**: TryHackMe
- **Difficulty**: Easy
- **Flag**: `THM{l0v3_is_in_th3_r0b0ts_txt}`

## Attack Path

1. **Recon** - nmap scan revealed port 80 (HTTP) open
2. **Enumeration** - Checked standard info disclosure files
3. **Discovery** - `robots.txt` contained a disallowed path: `/cupids_secret_vault/`
4. **Access** - Navigated to the vault page, found a login form
5. **Exploitation** - Password was hardcoded in page source: `cupid_arrow_2026!!!`
6. **Flag** - Logged in as admin, flag displayed on dashboard

## Techniques Used
- Information disclosure (robots.txt)
- Default/hardcoded credentials
- Source code inspection

## Developer Lesson
- `robots.txt` is publicly accessible -- it tells crawlers what NOT to index, but anyone can read it. Never use it to "hide" sensitive paths.
- Never hardcode passwords in client-side code (HTML, JavaScript). Use server-side authentication with hashed credentials.
- In enterprise applications, this is equivalent to leaving API keys in frontend JavaScript or checked-in config files.

## Enterprise Context
This maps directly to OWASP A01:2021 - Broken Access Control and A07:2021 - Security Misconfiguration. In Spring Boot applications, the equivalent would be exposing actuator endpoints without authentication or leaving default credentials in application.yml.
