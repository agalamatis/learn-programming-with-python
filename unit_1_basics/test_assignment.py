import unittest

from unit_1_basics import assignment


class TestAssignment(unittest.TestCase):

    def test_operation_precedence(self):
        """
        result = (1 - 3) ** 2 / - 2
        """
        result = assignment.operation_precedence()
        self.assertEqual(
            -2.0, 
            result,
            msg=(
                'You have to try again, '
                f'the result of your expression was {result}, '
                'not the float -2.0.'
            )
        )
