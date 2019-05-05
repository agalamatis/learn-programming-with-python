import unittest

from unit_1_basics import assignment


class TestAssignment(unittest.TestCase):

    def test_a_test(self):
        self.assertEqual(1, assignment.a_test())
