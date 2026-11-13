import unittest
#Application code
def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b

#Automated test cases
class TestCalculator(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(21,19),40)
  def test_subtract(self):
    self.assertEqual(subtract(20,1),19)
  def test_multiply(self):
    self.assertEqual(multiply(9,4),36)

#Main application
if __name__=="__main__":
  print("Student Calculator Application")
  print("Addition :",add(20,20))
  print("Subtraction:",subtract(20,10))
  print("Multiplication:",multiply(5,4))
  
  print("\n Executing Automated Tests...\n")
  unittest.main(argv=['first-arg-is-ignored'],exit=False)
