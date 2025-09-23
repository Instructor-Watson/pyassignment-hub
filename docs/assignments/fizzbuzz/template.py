"""
TODO:
- Implement fizzbuzz(n) as described in the instructions.
- Write clean conditionals (consider order).
- Keep your function pure: do NOT print; return a list.
"""

def fizzbuzz(n: int):
    """
    Return a list from 1..n with Fizz/Buzz/FizzBuzz substitutions.
    """
    # Your code here
    result = []
    for i in range(1, n+1):
        label = ""
        # TODO: set label based on i
        # if multiple of 3 and 5 -> "FizzBuzz"
        # elif multiple of 3 -> "Fizz"
        # elif multiple of 5 -> "Buzz"
        # else -> str(i)

        result.append(str(i) if not label else label)
    return result


if __name__ == "__main__":
    # quick manual check
    print(fizzbuzz(16))
