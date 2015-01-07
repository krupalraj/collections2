from twisted.trial import unittest

from collections2 import FrozenOrderedSet


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.s = FrozenOrderedSet('abcdefg')

    def test_order(self):
        expected = list(enumerate('abcdefg'))
        self.assertEquals(list(enumerate(self.s)), expected)

    def test_index(self):
        self.assertEquals(self.s.key_index('c'), 2)


class TestEquality(unittest.TestCase):
    def setUp(self):
        self._test_vals = 'abc'
        self.s = FrozenOrderedSet('abc')

    def test_order_check(self):
        s = FrozenOrderedSet('abc')
        self.assertEqual(self.s, s)

    def test_bad_order_check(self):
        s = FrozenOrderedSet('bac')
        self.assertNotEqual(self.s, s)

    def test_builtin_set_inequality(self):
        s = set('abc')
        self.assertNotEqual(self.s, s)


class TestHashing(unittest.TestCase):
    def test_set_membership(self):
        a = FrozenOrderedSet('abc')
        b = FrozenOrderedSet('abc')

        test_set = set()
        test_set.add(a)

        self.assertIn(b, test_set)

    def test_dict_key(self):
        a = FrozenOrderedSet('abc')
        b = FrozenOrderedSet('abc')

        d = dict()
        d[a] = True
        self.assertIs(d[b], True)
