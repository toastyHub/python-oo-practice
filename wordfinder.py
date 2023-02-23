"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    '''Reads a dictionary, returns the number of words read'''

    def __init__(self, file_path):
        # opens a file at the passed path
        txt_file = open(file_path)
        # Passes file to parse() method
        self.words = self.parse(txt_file)
        #  Prints out the number of words
        print(f"{len(self.words)} words read")
    
    def parse(self, txt_file):
        '''Returns a dictionary of all words in file'''
        # Iterates over each word in txt_file, removes spaces using .strip()
        # Returns a dictionary of all words with spaces removed
        return [word.strip() for word in txt_file]
    
    def random_word(self):
        '''Returns a random word'''
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    '''Alt WordFinder that excludes blank lines and comments'''
    
    def parse(self, txt_file):

        return [word.strip() for word in txt_file
                if word.strip and not word.startswith('#')]