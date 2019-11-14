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


if __name__ == '__main__':
    unittest.main()
