from twisted.trial import unittest

from collections2 import FrozenOrderedDict


class TestOrder(unittest.TestCase):
    def setUp(self):
        self._test_keys = ['a', 'b', 'c']
        self._test_vals = [-2, 0, 1]
        self.d = FrozenOrderedDict(zip(self._test_keys, self._test_vals))

    def test_order(self):
        self.assertEquals(self.d.keys(), [key for key in self._test_keys])

    def test_index(self):
        self.assertEquals(self.d.key_index('c'), 2)


class TestEquality(unittest.TestCase):
    def setUp(self):
        self._test_keys = ['a', 'b', 'c']
        self._test_vals = [-2, 0, 1]
        self.d = FrozenOrderedDict(zip(self._test_keys, self._test_vals))

    def test_order_check(self):
        od = FrozenOrderedDict([('c', 1), ('b', 0), ('a', -2)])
        self.assertNotEquals(self.d, od)

    def test_value_check(self):
        od = FrozenOrderedDict([('a', -2), ('b', 0), ('c', 3)])
        self.assertNotEquals(self.d, od)

    def test_builtin_dict_inequality(self):
        d = {'a': -2, 'b': 0, 'c': 3}
        self.assertNotEquals(self.d, d)


class TestHashing(unittest.TestCase):
    def test_set_membership(self):
        a = FrozenOrderedDict(enumerate('abc'))
        b = FrozenOrderedDict(enumerate('abc'))

        test_set = set()
        test_set.add(a)

        self.assertIn(b, test_set)

    def test_dict_key(self):
        a = FrozenOrderedDict(enumerate('abc'))
        b = FrozenOrderedDict(enumerate('abc'))

        d = dict()
        d[a] = True
        self.assertIs(d[b], True)
