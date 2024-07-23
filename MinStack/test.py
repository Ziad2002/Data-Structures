import unittest
from MinStack import MinStack


class Test_MinStack(unittest.TestCase):
    def test(self):
        minStack = MinStack()
        minStack.push(1)
        minStack.push(2)
        minStack.push(0)
        self.assertEqual(minStack.getMin(), 0)
        minStack.pop()
        self.assertEqual(minStack.top(), 2)
        self.assertEqual(minStack.getMin(), 1)


if __name__ == '__main__':
    unittest.main()