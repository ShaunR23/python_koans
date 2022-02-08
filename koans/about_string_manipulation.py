#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStringManipulation(Koan):

    def test_use_format_to_interpolate_variables(self):
        #the values of one and 2 are plugged in place of {0} and {1}
        value1 = 'one'
        value2 = 2
        string = "The values are {0} and {1}".format(value1, value2)
        self.assertEqual("The values are one and 2", string)

    def test_formatted_values_can_be_shown_in_any_order_or_be_repeated(self):
        #value DOH is passed in place of {1} and value doh is passed in place of {0}
        value1 = 'doh'
        value2 = 'DOH'
        string = "The values are {1}, {0}, {0} and {1}!".format(value1, value2)
        self.assertEqual("The values are DOH, doh, doh and DOH!", string)

    def test_any_python_expression_may_be_interpolated(self):
        import math # import a standard python module with math functions
        #the square root of 5 calculated after .format is used in place of {0:.{1}f}
        decimal_places = 4
        string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5),
            decimal_places)
        self.assertEqual('The square root of 5 is 2.2361', string)

    def test_you_can_get_a_substring_from_a_string(self):
        #returns index of 7 to index of 10
        string = "Bacon, lettuce and tomato"
        self.assertEqual('let', string[7:10])

    def test_you_can_get_a_single_character_from_a_string(self):
        #returns a since its the index of 1
        string = "Bacon, lettuce and tomato"
        self.assertEqual('a', string[1])

    def test_single_characters_can_be_represented_by_integers(self):
        #ord returns the ASCII value of the character
        self.assertEqual(97, ord('a'))
        self.assertEqual(True, ord('b') == (ord('a') + 1))

    def test_strings_can_be_split(self):
        #by default split seperator is any whitespace
        string = "Sausage Egg Cheese"
        words = string.split()
        self.assertListEqual(['Sausage', 'Egg', 'Cheese'], words)

    def test_strings_can_be_split_with_different_patterns(self):
        import re #import python regular expression library
        #string is being seperated by any special characters defined in pattern
        string = "the,rain;in,spain"
        pattern = re.compile(',|;')

        words = pattern.split(string)

        self.assertListEqual(['the', 'rain', 'in', 'spain'], words)

        # Pattern is a Python regular expression pattern which matches ',' or ';'

    def test_raw_strings_do_not_interpret_escape_characters(self):
        #raw strings take an escape character such as \ as an literal character
        string = r'\n'
        self.assertNotEqual('\n', string)
        self.assertEqual('\\n', string)
        self.assertEqual(2, len(string))

        # Useful in regular expressions, file paths, URLs, etc.

    def test_strings_can_be_joined(self):
        words = ["Now", "is", "the", "time"]
        self.assertEqual('Now is the time', ' '.join(words))

    def test_strings_can_change_case(self):
        self.assertEqual('Guido', 'guido'.capitalize()) #capitalizes the string
        self.assertEqual('GUIDO', 'guido'.upper()) #converts to all uppercase
        self.assertEqual('timbot', 'TimBot'.lower()) #converts to all lowercase
        self.assertEqual('Guido Van Rossum', 'guido van rossum'.title()) #capitalizes first character of each word
        self.assertEqual('tOtAlLy AwEsOmE', 'ToTaLlY aWeSoMe'.swapcase())#swaps lowercase to uppercase and vice versa
