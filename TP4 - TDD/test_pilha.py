import unittest 
from pilha import Pilha


class TestPilha(unittest.TestCase):
    def test_enqueue(self):
        stack = Pilha()
        stack.enqueue(0)
        stack.enqueue(1)
        stack.enqueue(2)
        self.assertEqual(3, stack.length())



    def test_dequeue(self):
        stack = Pilha()
        stack.enqueue(0)
        stack.enqueue(1)
        stack.dequeue()
        self.assertEqual(1, stack.length())



    def test_is_empty(self):
        stack = Pilha()
        self.assertTrue(stack.is_empty())
    

if __name__ == '__main__':
    unittest.main()