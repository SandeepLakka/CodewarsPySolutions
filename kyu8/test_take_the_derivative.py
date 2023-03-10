from kyu8.take_the_derivative import *
import codewars_test as test
from random import randint


@test.describe('Example Tests')
def example_tests():
    test.assert_equals(derive(7, 8), "56x^7", "derive(7, 8) -> 56x^7")
    test.assert_equals(derive(5, 9), "45x^8", "derive(5, 9) -> 45x^8")


@test.describe('Random Tests')
def random_tests():
    def generate_random_case(min_c=1, max_c=500, min_e=2, max_e=500):
        return randint(min_c, max_c), randint(min_e, max_e)

    def _derive_123(c, e):
        return f"{c * e}x^{e - 1}"

    def _do_one_test():
        c, e = generate_random_case()
        expected = _derive_123(c, e)
        actual = derive(c, e)
        test.assert_equals(actual, expected, f"derive({c}, {e}) -> {actual}")

    @test.it('Random Test Cases')
    def random_test_cases():
        for _ in range(100):
            _do_one_test()
