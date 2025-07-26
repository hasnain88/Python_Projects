import unittest
import demo2

class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calculate = demo2.Calculate()    
   
    def test_add(self):
        
        self.assertEqual(self.calculate.add(5,5),10)
        self.assertEqual(self.calculate.add(5,4),9)
    
    def test_sub(self):
        
        self.assertEqual(self.calculate.sub(5,5),0)

    def test_mul(self):
        calculate = demo2.Calculate()
        self.assertEqual(self.calculate.mul(5,5),25)
    
    def test_div(self):
        calculate = demo2.Calculate()
        self.assertEqual(self.calculate.div(5,5),1)


if __name__=="__main__":
    unittest.main()

        