# Public tests (students can view these)
def _expect_equal(a, b, msg=""):
    assert a == b, msg or f"expected {b!r}, got {a!r}"

_expect_equal(fizzbuzz(5), ["1","2","Fizz","4","Buzz"])
_expect_equal(fizzbuzz(3), ["1","2","Fizz"])
_expect_equal(fizzbuzz(15)[-1], "FizzBuzz")
