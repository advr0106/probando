import unittest
from arab_to_roman import convert_to_roman

class TestRomanConverter(unittest.TestCase):
    def test_valid_number(self):
        # Arrange
        input_number = "12"
        expected_output = "XII"
        
        # Act
        result = convert_to_roman(input_number)
        
        # Assert
        self.assertEqual(result, expected_output)
        
    def test_invalid_number_range(self):
        # Arrange
        input_number = "5132"
        expected_output = "Wrong number you may introduce a number between 0 and 5000"
        
        # Act
        result = convert_to_roman(input_number)
        
        # Assert
        self.assertEqual(result, expected_output)
        
    def test_invalid_input(self):
        # Arrange
        input_number = "Prueba"
        expected_output = "Wrong value, we just accept positive entire numbers"
        
        # Act
        result = convert_to_roman(input_number)
        
        # Assert
        self.assertEqual(result, expected_output)
        
    def test_null_input(self):
        # Arrange
        input_number = ""
        expected_output = "Wrong value, we just accept positive entire numbers"
        
        # Act
        result = convert_to_roman(input_number)
        
        # Assert
        self.assertEqual(result, expected_output)
        
    def test_number_0(self):
        # Arrange
        input_number = "0"
        expected_output = ""
        
        # Act
        result = convert_to_roman(input_number)
        
        # Assert
        self.assertEqual(result, expected_output)