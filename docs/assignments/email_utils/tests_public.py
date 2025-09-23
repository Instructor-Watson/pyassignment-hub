# Public tests
def _t(v, msg=""): 
    assert v, msg or "expected True"

def _f(v, msg=""): 
    assert not v, msg or "expected False"

_t(is_valid_email("a.b_c1@example.com"))
_t(is_valid_email("x@x.io"))
_f(is_valid_email("nospaces please@example.com"))
_f(is_valid_email("bad@domain"))
assert extract_user_domain("a.b@example.com") == ("a.b", "example.com")
