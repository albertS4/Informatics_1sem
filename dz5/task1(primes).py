import math

def to_primes(n):
    primes = []

    while n % 2 == 0:
        primes.append(2)
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            primes.append(i)
            n //= i

    if n > 2:
        primes.append(n)
    return primes

import unittest

class BasicTest(unittest.TestCase):
    def test_subprimes(self):
        self.assertListEqual(to_primes(2), [2])
        self.assertListEqual(to_primes(3), [3])
    def test_primes(self):
        self.assertListEqual(to_primes(7), [7])
        self.assertListEqual(to_primes(11), [11])
        self.assertListEqual(to_primes(977), [977])
    def test_simple_compounds(self):
        self.assertListEqual(to_primes(6), [2, 3])
        self.assertListEqual(to_primes(8), [2, 2, 2])
        self.assertListEqual(to_primes(121), [11, 11])
        self.assertListEqual(to_primes(2), [2])
    def test_complex_compounds(self):
        self.assertListEqual(to_primes(120120), [2, 2, 2, 3, 5, 7, 11, 13])
        self.assertListEqual(to_primes(622349), [7, 7, 13, 977])

if __name__ == "__main__":
    unittest.main()