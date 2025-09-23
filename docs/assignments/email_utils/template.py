import re

# TODO: design a simple, readable pattern.
# Requirements (approximate):
# - username: letters/digits, dot/underscore allowed (not first/last), e.g. alice_1
# - domain: letters/digits and dots, at least one dot, e.g. example.com

EMAIL_RE = re.compile(r"", re.IGNORECASE)

def is_valid_email(s: str) -> bool:
    """Return True if s matches EMAIL_RE exactly."""
    # your code here
    return False

def extract_user_domain(s: str):
    """Return (user, domain) if valid, else None."""
    # your code here
    return None


if __name__ == "__main__":
    # quick manual checks
    tests = ["test@example.com", "bad@", "first.last@sub.domain.org", "UPPER_case@Example.Com"]
    for t in tests:
        print(t, is_valid_email(t), extract_user_domain(t))
