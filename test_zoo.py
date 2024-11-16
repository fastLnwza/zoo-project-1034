import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
     # Add your additional test cases here.
        self.assertEqual(self.zoo.get_ticket_price(-1),0)
        self.assertEqual(self.zoo.get_ticket_price(0),50)
        self.assertEqual(self.zoo.get_ticket_price(20),100)
        self.assertEqual(self.zoo.get_ticket_price(21),150)
        self.assertEqual(self.zoo.get_ticket_price(60),150)
       
   

if __name__ == '__main__':
    unittest.main()