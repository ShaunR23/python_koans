#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrayAssignments in the Ruby Koans
#

from runner.koan import *

class AboutListAssignments(Koan):
    def test_non_parallel_assignment(self):
        #calling names returns the original array
        names = ["John", "Smith"]
        self.assertEqual(["John", "Smith"], names)

    def test_parallel_assignments(self):
        #first_name is assigned to index 0, last_name is assigned to index1
        first_name, last_name = ["John", "Smith"]
        self.assertEqual("John", first_name)
        self.assertEqual("Smith", last_name)

    def test_parallel_assignments_with_extra_values(self):
        title, *first_names, last_name = ["Sir", "Ricky", "Bobby", "Worthington"]
        self.assertEqual("Sir", title)
        self.assertEqual(["Ricky", "Bobby"], first_names)
        self.assertEqual("Worthington", last_name)
            #title takes 1st spot, last name takes last spot, first names takes anything else
    def test_parallel_assignments_with_fewer_values(self):
        title, *first_names, last_name = ["Mr", "Bond"]
        self.assertEqual("Mr", title)
        self.assertEqual([], first_names)#other variables were required, so nothing is entered here
        self.assertEqual("Bond", last_name)

    def test_parallel_assignments_with_sublists(self):
        #first_name is assigned to the array of Willy and Rae, last_name is index which is Johnson
        first_name, last_name = [["Willie", "Rae"], "Johnson"]
        self.assertEqual(["Willie", "Rae"], first_name)
        self.assertEqual("Johnson", last_name)

    def test_swapping_with_parallel_assignment(self):
        first_name = "Roy"
        last_name = "Rob"
        first_name, last_name = last_name, first_name
        self.assertEqual("Rob", first_name)
        self.assertEqual("Roy", last_name)

