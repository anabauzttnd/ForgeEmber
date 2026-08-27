# test_forgeember.py
"""
Tests for ForgeEmber module.
"""

import unittest
from forgeember import ForgeEmber

class TestForgeEmber(unittest.TestCase):
    """Test cases for ForgeEmber class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ForgeEmber()
        self.assertIsInstance(instance, ForgeEmber)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ForgeEmber()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
