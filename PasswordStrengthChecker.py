import string
import getpass
import math
import hashlib
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

MIN_LENGTH = 8
HIBP_API_KEY = None
USER_AGENT = "PasswordForge/1.0 (MumbaiHackMaster)"

session = requests.Session()
retry_strategy = Retry(total=3, backoff_factor=1)
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("http://", adapter)
session.mount("https://", adapter)


def check_pwned_password(password):

    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]

    try:
        headers = {'User-Agent': USER_AGENT, 'Add-Padding': 'true'}
        response = session.get(f'https://api.pwnedpasswords.com/range/{prefix}',
                               headers=headers, timeout=5)
        if response.status_code == 200:
            for line in response.text.splitlines():
                hash_suffix, count = line.split(':')
                if hash_suffix == suffix:
                    return int(count)
        return 0
    except Exception:
        return None


def calculate_entropy(password):
    charset_size = 0
    if any(c in string.ascii_lowercase for c in password):
        charset_size += 26
    if any(c in string.ascii_uppercase for c in password):
        charset_size += 26
    if any(c in string.digits for c in password):
        charset_size += 10
    if any(c in string.punctuation for c in password):
        charset_size += len(string.punctuation)
    if any(c.isspace() for c in password):
        charset_size += 1
    return len(password) * math.log2(charset_size) if charset_size else 0


def check_password_strength():

    password = getpass.getpass('Enter password: ')
    if len(password) < MIN_LENGTH:
        print(f"Too short! {MIN_LENGTH}+ chars.")
        return

    lower = sum(1 for c in password if c in string.ascii_lowercase)
    upper = sum(1 for c in password if c in string.ascii_uppercase)
    num = sum(1 for c in password if c in string.digits)
    special = sum(1 for c in password if c in string.punctuation)
    wspace = sum(1 for c in password if c.isspace())
    entropy = calculate_entropy(password)

    pwned_count = check_pwned_password(password)
    pwned_status = "PWNED!" if pwned_count and pwned_count > 0 else "Not pwned."

    if pwned_count and pwned_count > 0:
        remarks = f"BREACHED: Appears {pwned_count} times—scrap it bih!"
    elif entropy < 28:
        remarks = "Very Weak: Guessable."
    elif entropy < 36:
        remarks = "Weak: Cracks fast."
    elif entropy < 60:
        remarks = "Moderate: Harden up."
    elif entropy < 80:
        remarks = "Strong: Solid."
    else:
        remarks = "Fortress: Unbreakable."

    print("\n Analysis:")
    print(f"{lower} lowercase | {upper} uppercase | {num} digits | {special} specials | {wspace} spaces")
    print(f"Entropy: {entropy:.2f} bits")
    print(f"HIBP: {pwned_status}")
    if pwned_count:
        print(f"   → Seen {pwned_count} times in breaches.")
    print(f"{remarks}\n")


def check_another():
    while True:
        choice = input("Another? (y/n): ").strip().lower()
        return choice == 'y'


if __name__ == '__main__':
    print("HIBP Password Strength Checker")
    while True:
        check_password_strength()
        if not check_another():
            print("Stay fortified, bbbg")
            break
