from unittest import TestCase
from flask_apidoc.utils import cached


class TestUtils(TestCase):
    def test_cache(self):
        @cached
        def f(a, b):
            return object()

        self.assertEqual(f(1, 2), f(1, 2))
        self.assertNotEqual(f(1, 2), f(1, 3))
