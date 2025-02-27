#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutIteration(Koan):

    def test_iterators_are_a_type(self):
        it = iter(range(1,6))

        total = 0

        for num in it:
            total += num
    #loops through numbers 1 through 5 adding num to previous total each time
        self.assertEqual(15, total)

    def test_iterating_with_next(self):
        stages = iter(['alpha','beta','gamma'])

        try:
            self.assertEqual('alpha', next(stages))
            next(stages)#moves to beta
            self.assertEqual('gamma', next(stages))
            #gamma is after beta
            next(stages)
            #empty
        except StopIteration as ex:
            err_msg = 'Ran out of iterations'

        self.assertRegex(err_msg, 'Ran out of iterations')

    # ------------------------------------------------------------------

    def add_ten(self, item):
        return item + 10

    def test_map_transforms_elements_of_a_list(self):
        seq = [1, 2, 3]
        mapped_seq = list()

        mapping = map(self.add_ten, seq)

        self.assertNotEqual(list, mapping.__class__)
        self.assertEqual(map, mapping.__class__)
        # In Python 3 built in iterator funcs return iterable view objects
        # instead of lists

        for item in mapping:
            mapped_seq.append(item)

        self.assertEqual([11,12,13], mapped_seq)

        # Note, iterator methods actually return objects of iter type in
        # python 3. In python 2 map() would give you a list.

    def test_filter_selects_certain_items_from_a_list(self):
        def is_even(item):
            return (item % 2) == 0

        seq = [1, 2, 3, 4, 5, 6]
        even_numbers = list()

        for item in filter(is_even, seq):
            even_numbers.append(item)

        self.assertEqual([2,4,6], even_numbers)
        #even numbers returned through filter because items divided by 2 have no remainder
    def test_filter_returns_all_items_matching_criterion(self):
        def is_big_name(item):
             return len(item) > 4

        names = ["Jim", "Bill", "Clarence", "Doug", "Eli", "Elizabeth"]
        iterator = filter(is_big_name, names)

        self.assertEqual('Clarence', next(iterator))
        self.assertEqual('Elizabeth', next(iterator))
        #Clarence and Elizabeth were filtered out by being greater than 4 characters
        try:
            next(iterator)
            pass
        except StopIteration:
            msg = 'Ran out of big names'

        self.assertEquals('Ran out of big names', msg)

    # ------------------------------------------------------------------

    def add(self,accum,item):
        return accum + item

    def multiply(self,accum,item):
        return accum * item

    def test_reduce_will_blow_your_mind(self):
        import functools
        # As of Python 3 reduce() has been demoted from a builtin function
        # to the functools module.

        result = functools.reduce(self.add, [2, 3, 4])
        self.assertEqual(int, result.__class__)
        # Reduce() syntax is same as Python 2
        #adding together 2+3, and took that result 5 and added the next item 4. 5+4 =9
        self.assertEqual(9, result)

        result2 = functools.reduce(self.multiply, [2, 3, 4], 1)
        self.assertEqual(24, result2)
        #multiplied 2*3=6, 6 is multiplied by 4 =24 and then 24*1 leaves the result at 24
        # Extra Credit:
        # Describe in your own words what reduce does.

    # ------------------------------------------------------------------

    def test_use_pass_for_iterations_with_no_body(self):
        for num in range(1,5):
            pass

        self.assertEqual(4, num)

    # ------------------------------------------------------------------

    def test_all_iteration_methods_work_on_any_sequence_not_just_lists(self):
        # Ranges are an iterable sequence
        result = map(self.add_ten, range(1,4))
        self.assertEqual([11,12,13], list(result))
        #mapped through numbers 1,2,3 and added 10

    def test_lines_in_a_file_are_iterable_sequences_too(self):
        def make_upcase(line):
            return line.strip().title()

        file = open("example_file.txt")
        upcase_lines = map(make_upcase, file.readlines())
        self.assertEqual(['This', 'Is', 'A', 'Test'], list(upcase_lines))
        file.close()
