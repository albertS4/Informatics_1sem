import unittest
def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[(len(array) - 1)//2]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)
    else:
        return array


class OrderTest(unittest.TestCase):
    def test_numbers(self):
        self.assertListEqual(sort([1, 2, 3]), [1, 2, 3])
        self.assertListEqual(sort([2, 1, 3]), [1, 2, 3])
        self.assertListEqual(sort([10, 2, 3]), [2, 3, 10])
        self.assertListEqual(sort([-1, -2, -3]), [-3, -2, -1])
        self.assertListEqual(sort([1.0, 1.1, 1.2]), [1.0, 1.1, 1.2])
        self.assertListEqual(sort([1, 1, 1]), [1, 1, 1])
        self.assertListEqual(sort([float("-inf"), 2, float("inf")]), [float("-inf"), 2, float("inf")])
    def test_strings(self):
        self.assertListEqual(sort(["a", "b", "c"]), ["a", "b", "c"])
        self.assertListEqual(sort(["кот", "кит"]), ["кит", "кот"])
        self.assertListEqual(sort(["А", "О", "В"]), ["А", "В", "О"])
    def test_lists(self):
        self.assertListEqual(sort([[1, 2, 3], [1, 2], [1]]), [[1], [1, 2], [1, 2, 3]])
        self.assertListEqual(sort([[], [1, 2], [1]]), [[], [1], [1, 2]])
    
if __name__ == "__main__":
    unittest.main()