#!/usr/bin/env python3

from re_arrange import rearrange_name_regex
import unittest

# * Basic way of testing is trying with different inputs
print('Basic Test output -->', rearrange_name_regex('Lovelace, Ada'))
print('Basic Test output -->', rearrange_name_regex('Yaeger, Ereh'))

# * Now we will test using the  UNITTEST MODULE


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = 'Lovelace, Ada'
        expected = 'Ada Lovelace'
        self.assertAlmostEqual(rearrange_name_regex(testcase), expected)

    def test_empty(self):
        testcase = ''
        expected = ''
        self.assertEqual(rearrange_name_regex(testcase), expected)

    def test_double_name(self):
        testcase = 'Hopper, Grace M.'
        expected = 'Grace M. Hopper'
        self.assertEqual(rearrange_name_regex(testcase), expected)

    def test_one_name(self):
        testcase = 'Mikasa'
        expected = 'Mikasa'
        self.assertEqual(rearrange_name_regex(testcase), expected)


unittest.main()
