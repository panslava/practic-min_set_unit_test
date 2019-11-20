import unittest


class TestSetProperties(unittest.TestCase):
    def test_unique(self):
        test_set = {1, 2, 3, 4, 4, 3, 1}
        self.assertEqual(test_set, {1, 2, 3, 4})

    def test_add_existing_element(self):
        test_set = {1, 2, 3}
        test_set.add(3)
        self.assertEqual(test_set, {1, 2, 3})

    def test_add_non_existing_element(self):
        test_set = {1, 2, 3}
        test_set.add(4)
        self.assertEqual(test_set, {1, 2, 3, 4})

    def test_same_sets_equal(self):
        first_set = {1, 2, 3}
        second_set = {2, 3, 1}
        self.assertEqual(first_set, second_set)

    def test_different_sets_differ(self):
        first_set = {1, 2, 3, 4}
        second_set = {1, 2, 3}
        self.assertNotEqual(first_set, second_set)

    def test_contains_element(self):
        test_set = {1, 2, 3}

        self.assertIn(1, test_set)

    def test_not_contains_element(self):
        test_set = {1, 2, 3}

        self.assertNotIn(4, test_set)

    def test_length(self):
        test_set = {1, 2, 3, 3}
        self.assertEqual(3, len(test_set))

        test_set.add(4)
        self.assertEqual(4, len(test_set))

        test_set.remove(3)
        self.assertEqual(3, len(test_set))

    def test_remove(self):
        test_set = {1, 2, 3, 3}
        test_set.remove(3)
        self.assertEqual(2, len(test_set))

    def test_clear(self):
        test_set = {1, 2, 3}
        test_set.clear()
        self.assertEqual(set(), test_set)

    def test_difference(self):
        first_set = {1, 2, 3, 4}
        second_set = {2, 3, 4, 5}
        self.assertEqual({1}, first_set.difference(second_set))
        self.assertEqual({5}, second_set.difference(first_set))

    def test_intersection(self):
        first_set = {1, 2, 3, 4}
        second_set = {2, 3, 4, 5}
        self.assertEqual({2, 3, 4}, first_set.intersection(second_set))
        self.assertEqual({2, 3, 4}, second_set.intersection(first_set))

    def test_symmetric_difference(self):
        first_set = {1, 2, 3, 4}
        second_set = {2, 3, 4, 5}
        self.assertEqual({1, 5}, first_set.symmetric_difference(second_set))
        self.assertEqual({1, 5}, second_set.symmetric_difference(first_set))

    def test_is_subset(self):
        first_set = {1, 2, 3}
        second_set = {1, 2, 3, 4}
        self.assertEqual(True, first_set.issubset(second_set))
        self.assertEqual(False, second_set.issubset(first_set))


if __name__ == '__main__':
    unittest.main()
