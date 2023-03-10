def assert_equals(actual, expected, message=None):
    try:
        assert actual == expected
    except AssertionError as ae:
        print(
            (message if message is not None else "Test Exception"),
            " :: Expected =", expected,
            "Actual =", actual)


# Return True for values which are not singular
def plural(n):
    return n != 1


# Make a function that returns the value multiplied by 50 and increased by 6.
# If the value entered is a string it should return "Error".
def problem(a):
    return "Error" if type(a) == str else a * 50 + 6


# https://www.codewars.com/kata/574b3b1599d8f897470018f6/train/python
def get_real_floor(n):
    return n if n < 1 else (n-1 if n <13 else n-2)


if __name__ == '__main__':
    assert_equals(plural(0), True, "Should be True for 0")
    assert_equals(plural(1), False)
    assert_equals(plural(100), True)

    assert_equals(problem("1"), "Error")
    assert_equals(problem(100), 5006)
    assert_equals(problem(20), 1006)

    assert_equals(get_real_floor(1), 0)
    assert_equals(get_real_floor(5), 4)
    assert_equals(get_real_floor(15), 13)

    print("Tests OK")
