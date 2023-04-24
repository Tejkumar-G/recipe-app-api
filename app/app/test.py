"""
Sample tests
"""
from django.test import SimpleTestCase
from app import cal


class CalsTests(SimpleTestCase):
    """Tests the cals function"""

    def test_add_numbers(self):
        """Tests adding numbers"""
        res = cal.sum(3, 4)

        self.assertEqual(res, 7)
