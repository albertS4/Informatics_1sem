import unittest
def least_squares(x,y):
    #y = b + kx
    N = len(x)
    avxy = sum([x[i]*y[i] for i in range(len(x))])/N 
    avx = sum(x)/N
    avy = sum(y)/N
    av2x = sum([x[i]*x[i] for i in range(len(x))])/N
    av2y = sum([y[i]*y[i] for i in range(len(x))])/N
    k=(avxy - avx*avy)/(av2x - avx**2)
    b=avy - k*avx
    return k, b


class ApproxTest(unittest.TestCase):
    def test_k(self):
        self.assertEqual(least_squares([0, 1], [0, 1])[0], 1.0, "(0, 0) -> (1, 1) should be k = 1, b = 0")
        self.assertEqual(least_squares([0, 5], [0, 5])[0], 1.0, "(0, 0) -> (5, 5) should be k = 1, b = 0")
        self.assertEqual(least_squares([0, 1], [1, 2])[0], 1.0, "(0, 1) -> (1, 2) should be k = 1, b = 1")
        self.assertEqual(least_squares([0, 1], [0, -1])[0], -1.0, "(0, 0) -> (1, -1) should be k = -1, b = 0")
        self.assertEqual(least_squares([0, 1], [1, 0])[0], -1.0, "(0, 1) -> (1, 0) should be k = -1, b = 1")
        self.assertEqual(least_squares([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])[0], 1.0, "(0, 0) -> (1, 1) -> (2, 2) -....> (9, 9) should be k = 1, b = 0")
    def test_b(self):
        self.assertEqual(least_squares([0, 1], [0, 1])[1], 0.0, "(0, 0) -> (1, 1) should be k = 1, b = 0")
        self.assertEqual(least_squares([0, 5], [0, 5])[1], 0.0, "(0, 0) -> (5, 5) should be k = 1, b = 0")
        self.assertEqual(least_squares([0, 1], [1, 2])[1], 1.0, "(0, 1) -> (1, 2) should be k = 1, b = 1")
        self.assertEqual(least_squares([0, 1], [0, -1])[1], 0.0, "(0, 0) -> (1, -1) should be k = -1, b = 0")
        self.assertEqual(least_squares([0, 1], [1, 0])[1], 1.0, "(0, 1) -> (1, 0) should be k = -1, b = 1")
        self.assertEqual(least_squares([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])[1], 0.0, "(0, 0) -> (1, 1) -> (2, 2) -....> (9, 9) should be k = 1, b = 0")
    def test_complex(self):
        self.assertTrue(least_squares([0, 1, 2, 3, 4], [0, 1*0.3, 2*0.6, 3*0.9, 4*0.4])[0] < 0.9)
        self.assertTrue(least_squares([0, 1, 2, 3, 4], [0, 1*0.3, 2*0.6, 3*0.9, 4*0.4])[0] > 0.3)
if __name__ == "__main__":
    unittest.main()
