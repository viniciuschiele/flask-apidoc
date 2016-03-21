from unittest import TestCase
from flask_apidoc.utils import cached


class TestUtils(TestCase):
    def test_cached_function(self):
        @cached
        def f(a, b):
            return object()

        self.assertEqual(f(1, 2), f(1, 2))
        self.assertNotEqual(f(1, 2), f(1, 3))

    def test_cached_method(self):
        class C(object):
            @cached
            def f(self, a, b):
                return object()

        c = C()
        self.assertEqual(c.f(1, 2), c.f(1, 2))
        self.assertNotEqual(c.f(1, 2), c.f(1, 3))
