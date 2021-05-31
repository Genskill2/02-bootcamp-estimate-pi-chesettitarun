import math
import unittest
import random

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
def wallis(num_iterations):
	ans=2
	for i in range(1,num_iterations+1):
	    ans=ans*((4*i*i)/((4*i*i)-1))
	return ans
class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
def monte_carlo(num_darts):
	ans=4
	num_darts_inside_circle=0
	total_num_darts=0
	for i in range(1,num_darts+1):
		x=random.random()
		y=random.random()
		a=x
		b=y
		y=((b)*b)
		x=(a*(a))
		result= ((x+y)**0.5)
		if (result <= 1):
			num_darts_inside_circle=num_darts_inside_circle+1
		total_num_darts=total_num_darts+1
	return ans*(num_darts_inside_circle/total_num_darts)
        
    
if __name__ == "__main__":
    unittest.main()
