# test_typescripthub.py
"""
Tests for TypeScriptHub module.
"""

import unittest
from typescripthub import TypeScriptHub

class TestTypeScriptHub(unittest.TestCase):
    """Test cases for TypeScriptHub class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TypeScriptHub()
        self.assertIsInstance(instance, TypeScriptHub)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TypeScriptHub()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
