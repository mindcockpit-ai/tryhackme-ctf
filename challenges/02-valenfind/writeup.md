# ValenFind

## Challenge Info
- **Platform**: TryHackMe
- **Difficulty**: Easy-Medium
- **Flag**: `THM{v4l3nt1n3_jwt_c00k13_t4mp3r_4dm1n_sh0p}`

## Attack Path

1. **Recon** - nmap scan revealed port 80 (HTTP) with a web shop application
2. **Enumeration** - Registered an account, explored functionality
3. **Discovery** - Found a `tryheartme_jwt` cookie set after login
4. **JWT Analysis** - Decoded the JWT:
   - Header: `{"alg":"HS256","typ":"JWT"}`
   - Payload: `{"username":"testuser","role":"user"}`
5. **Exploitation** - Applied the "none" algorithm attack:
   - Changed header alg to `"none"`
   - Changed payload role to `"admin"`
   - Removed the signature (empty third segment)
   - Base64url-encoded and set as cookie
6. **Flag** - With forged admin JWT, accessed the admin shop and purchased the "ValenFlag" item

## Techniques Used
- JWT analysis and decoding
- Base64url encoding/decoding
- JWT "none" algorithm bypass
- Cookie tampering

## Key Script

Used `scripts/jwt-none-attack.py` to forge the admin token:
```bash
python3 scripts/jwt-none-attack.py <original-jwt>
```

## Developer Lesson
- Always enforce the JWT algorithm on the server side. Never trust the `alg` header from the client.
- Use an allowlist of accepted algorithms (e.g., only `HS256` or `RS256`).
- In Java/Spring: configure `JwtDecoder` with explicit algorithm constraints.
- This is equivalent to accepting unsigned API requests in your backend.

## Enterprise Context
Maps to OWASP A02:2021 - Cryptographic Failures. In enterprise applications using Spring Security with JWT, always use `NimbusJwtDecoder.withSecretKeyValue()` with explicit algorithm, never parse tokens with arbitrary algorithms. Libraries like `java-jwt` and `jose4j` support algorithm allowlists.
