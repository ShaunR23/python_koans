#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStrings(Koan):

    def test_double_quoted_strings_are_strings(self):
        #is double quoted properly
        string = "Hello, world."
        self.assertEqual(True, isinstance(string, str))

    def test_single_quoted_strings_are_also_strings(self):
        #single quotes works as a string
        string = 'Goodbye, world.'
        self.assertEqual(True, isinstance(string, str))

    def test_triple_quote_strings_are_also_strings(self):
        #triple quotes are strings
        string = """Howdy, world!"""
        self.assertEqual(True, isinstance(string, str))

    def test_triple_single_quotes_work_too(self):
       #triple single quotes works as string
        string = '''Bonjour tout le monde!'''
        self.assertEqual(True, isinstance(string, str))

    def test_raw_strings_are_also_strings(self):
        #raw strings count as strings
        string = r"Konnichi wa, world!"
        self.assertEqual(True, isinstance(string, str))

    def test_use_single_quotes_to_create_string_with_double_quotes(self):
        #single quotes on both ends and double quotations inside the single quotes counts as a string
        string = 'He said, "Go Away."'
        self.assertEqual('He said, "Go Away."', string)

    def test_use_double_quotes_to_create_strings_with_single_quotes(self):
        #double quotes on both ends of string and single quote in the string works
        string = "Don't"
        self.assertEqual("Don't", string)

    def test_use_backslash_for_escaping_quotes_in_strings(self):
        #backslash escapes the quote so the strings are equal
        a = "He said, \"Don't\""
        b = 'He said, "Don\'t"'
        self.assertEqual(True, (a == b))

    def test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line(self):
        #backslash continues to next line, length of the string is 52 characters
        string = "It was the best of times,\n\
It was the worst of times."
        self.assertEqual(52, len(string))

    def test_triple_quoted_strings_can_span_lines(self):
        #Triple quotes strings can bu used to span multiple lines, length of string is 15
        string = """
Howdy,
world!
"""
        self.assertEqual(15, len(string))

    def test_triple_quoted_strings_need_less_escaping(self):
        #triple quoted lines do not need to use backslash escaping as much, string a and b match
        a = "Hello \"world\"."
        b = """Hello "world"."""
        self.assertEqual(True, (a == b))

    def test_escaping_quotes_at_the_end_of_triple_quoted_string(self):
        #used single quotes on outside and double quotes inside for a valid string
        string = """Hello "world\""""
        self.assertEqual('Hello "world"', string)

    def test_plus_concatenates_strings(self):
        #concatenating two strings
        string = "Hello, " + "world"
        self.assertEqual("Hello, world", string)

    def test_adjacent_strings_are_concatenated_automatically(self):
        #automatically concatenated
        string = "Hello" ", " "world"
        self.assertEqual("Hello, world", string)

    def test_plus_will_not_modify_original_strings(self):
        #Concatenates both variables as strings
        hi = "Hello, "
        there = "world"
        string = hi + there
        self.assertEqual("Hello, ", hi)
        self.assertEqual("world", there)

    def test_plus_equals_will_append_to_end_of_string(self):
        # += appends to end of the string
        hi = "Hello, "
        there = "world"
        hi += there
        self.assertEqual("Hello, world", hi)

    def test_plus_equals_also_leaves_original_string_unmodified(self):
        # += does not modify the original string
        original = "Hello, "
        hi = original
        there = "world"
        hi += there
        self.assertEqual("Hello, ", original)

    def test_most_strings_interpret_escape_characters(self):
        #strings interpret escape characters, so length is equal to 1
        string = "\n"
        self.assertEqual('\n', string)
        self.assertEqual("""\n""", string)
        self.assertEqual(1, len(string))
