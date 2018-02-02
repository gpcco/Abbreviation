"""
@package: abbreviation
@brief: 
@author: 
@contact: 
"""

__version__ = 0000-00-00


class Word(str):
    """Custom string manipulation with extended string modification features."""

    def __init__(self, string):
        """Initialize Word class"""
        super(Word, self).__init__(string)

    def get_vowels(self):
        """Return only the vowels of a string"""

    def get_consonants(self):
        """Return only the consonants of a string"""

    def remove_vowels(self):
        """Return string with removed vowels"""

    def remove_consonants(self):
        """Return string with removed consonants"""

    def filter_out_special_characters(self):
        """Remove and modify the string to get rid of special characters"""

    def convert_string_to_numerical_dict(self):
        """Return a dict with numbers as key and each char as value"""
        # example output
        # {0: 'h', 1: 'e', 2: 'l', 3: 'l', 4: 'o'}

    def convert_numerical_dict_to_string(self):
        """Return a string from a numerical dict"""

    def get_numerical_dict(self):
        """Return the numerical dict"""

    def get_char_in_numerical_dict(self, key_number):
        """Return the value of given number from numerical dict"""

    def add_char_to_string(self):
        """Add a char to a string"""

    def remove_char_from_string(self):
        """Remove a char from a string"""

    def add_char_to_numerical_dict(self):
        """Add a char to a numerical dict"""

    def remove_char_from_numerical_dict(self):
        """Remove a char from a numerical dict"""

    def compare_string(self, other):
        """Compare the current string to another Word object's string"""

    def compare_dict(self, other):
        """Compare the current numerical dict to another Word object's dict"""
