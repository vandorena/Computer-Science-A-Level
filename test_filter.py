import unittest
from profanity_filter import censor

class TestFilterResult(unittest.TestCase):

    def test1(self):
        self.assertEqual(censor("You are a dunderhead spoon muncher."), "You are a d********d spoon muncher.")
    
    def test2(self):
        self.assertEqual(censor("Oh lordy this is a load of poppycock poo"), "Oh l***y this is a load of p*******k p*o")

# class TestFilterMore(unittest.TestCase):
#     def test_return_type(self):
#         self.assertIsInstance(censor("blah"), str)
        
#     def test_exception(self):
#         self.assertRaises(TypeError, censor)
#         self.assertRaises(AttributeError, censor, 123)


if __name__ == '__main__':
    unittest.main()
