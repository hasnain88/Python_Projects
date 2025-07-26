import unittest
import demo2


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calculate = demo2.Calculate()   

    def tearDown(self):
        # return super().tearDown()
        print("this a tear down method, execute after each test") 
   
    def test_add(self):
        
        self.assertEqual(self.calculate.add(5,5),10)
        self.assertEqual(self.calculate.add(5,4),9)
    

    def test_sub(self):
        
        self.assertEqual(self.calculate.sub(5,5),0)

    @unittest.skipIf(True,"Skipping beacuse the condition is True")
    def test_mul(self):
        self.assertEqual(self.calculate.mul(5,5),25)
    
    @unittest.skipIf(True,"Skipping beacuse the condition is True")
    def test_div(self):
        self.assertEqual(self.calculate.div(5,5),1)
        with self.assertRaises(ValueError):
            self.calculate.div(10,0)



if __name__=="__main__":
    unittest.main()

        