from kyu8.enum_magic_does_my_list_include_this import include as include
import codewars_test as test

list_to_test = [0, 1, 2, 3, 5, 8, 13, 2, 2, 2, 11]
test.assert_equals(include(list_to_test, 100), False, "list does not include 100")
test.assert_equals(include(list_to_test, 2), True, "list includes 2 multiple times")
test.assert_equals(include(list_to_test, 11), True, "list includes 11")
test.assert_equals(include(list_to_test, "2"), False, "list includes 2 (integer), not ''2'' (string)")
test.assert_equals(include([], 0), False, "empty list doesn't include anything")
test.assert_equals(include(list_to_test, 0), True, "list includes 0")
