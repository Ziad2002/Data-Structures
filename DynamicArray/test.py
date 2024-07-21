import unittest
from DynamicArray import DynamicArray

class Test_Dynamix_Array(unittest.TestCase):
    
    def test_one(self):
        array = DynamicArray(1)
        array.pushback(1)
        self.assertEqual(array.getCapacity(), 1)
        array.pushback(1)
        self.assertEqual(array.getCapacity(), 2)
        
    def test_two(self):
        array = DynamicArray(1)
        self.assertEqual(array.getSize(), 0)
        self.assertEqual(array.getCapacity(), 1)
        
    def test_three(self):
        array = DynamicArray(1)
        self.assertEqual(array.getSize(), 0)
        self.assertEqual(array.getCapacity(), 1)
        array.pushback(1)
        self.assertEqual(array.getSize(), 1)
        self.assertEqual(array.getCapacity(), 1)
        array.pushback(2)
        self.assertEqual(array.getSize(), 2)
        self.assertEqual(array.getCapacity(), 2)
        self.assertEqual(array.get(1), 2)
        array.set(1, 3)
        self.assertEqual(array.get(1), 3)
        array.popback()
        self.assertEqual(array.getSize(), 1)
        self.assertEqual(array.getCapacity(), 2)
        
        
        
        
        

if __name__ == '__main__':
    unittest.main()