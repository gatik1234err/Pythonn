HIBP-Integrated Password Strength Checker CLI

Abstract:

This project is a Python-based command-line tool that evaluates password strength locally and checks whether a password has appeared in known data breaches using the Have I Been Pwned (HIBP) Pwned Passwords API. It combines entropy-style checks (length, character diversity) with breach detection via HIBP’s k‑anonymity model, ensuring the full password is never sent over. The goal is to provide a practical, privacy-preserving security utility for personal use, pentesting workflows, and integration into custom authentication systems.

Work documentation

The project is an interactive CLI where the user enters a password, receives an immediate strength assessment, and then learns whether that password is known to be compromised in public breach datasets. Input is captured securely using hidden terminal input, and the process repeats in a loop until the user chooses to exit.

The workflow:
1. Accept password via `getpass` to avoid echoing it on screen.  
2. Run basic checks: minimum length, presence of lowercase, uppercase, digits, and symbols, plus a rough entropy-style score.  
3. Hash the password using SHA‑1 and convert it to an uppercase hex string.  
4. Send only the first 5 characters of the hash to HIBP’s Pwned Passwords API (`/range` endpoint) using the k‑anonymity model.  
5. Compare the remaining 35 characters of the hash against the returned list to determine if the password has been seen in breaches and how many times.  
6. Report:  
   - Qualitative strength (weak / moderate / strong) based on rules and score.  
   - Whether the password is compromised and an approximate breach count.  

Network requests use a `requests` session with retry logic to handle transient failures gracefully. The tool is also structured to later add HIBP API-key-based features for email or full breach lookup, though the core password-checking path does not require an API key.
Tools/technologies used:

- Python 3 for the core CLI implementation and logic.
- `getpass` for secure, non-echoed password input.   
- `hashlib` for SHA‑1 hashing of passwords before remote lookup.
- `requests` plus `HTTPAdapter` and `Retry` for robust HTTP communication with HIBP.
- HIBP Pwned Passwords API using the `range` endpoint and k‑anonymity pattern.
- Basic entropy estimation using logarithms from Python’s math capabilities.

Conclusion

This project delivers a practical, security-focused utility that combines local strength checks with real-world breach data while preserving user privacy via k‑anonymity. It fits neatly into a security-conscious workflow for developers, students, and pentesters who want fast feedback on password quality without trusting a third-party website with raw credentials.

Future work:

Planned and possible extensions include:
- Packaging as an installable CLI tool (`setuptools`/`pipx`) with proper versioning and documentation.  
- Adding configuration for policies (e.g., minimum entropy, corporate rules) and exporting JSON/CSV reports for audits.  
- Integrating HIBP’s authenticated endpoints (with an API key) for email or breach notifications, beyond just passwords.  
- Building a thin GUI/TUI or web frontend for non-technical users or for demos at college/hackathons.  
- Embedding this logic into custom authentication flows (e.g., NFC ring auth, Supabase-backed apps, or IoT devices) as a pre-check gate.  
 