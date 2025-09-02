import unittest
import demo2

class TestCalculate(unittest.TestCase):
    
   
    def test_add(self):
        calculate = demo2.Calculate()
        self.assertEqual(calculate.add(5,5),10)
        self.assertEqual(calculate.add(5,4),9)
    
    def test_sub(self):
        calculate = demo2.Calculate()
        self.assertEqual(calculate.sub(5,5),0)

    def test_mul(self):
        calculate = demo2.Calculate()
        self.assertEqual(calculate.mul(5,5),25)
    
    def test_div(self):
        calculate = demo2.Calculate()
        self.assertEqual(calculate.div(5,5),1)


if __name__=="__main__":
    unittest.main()

        