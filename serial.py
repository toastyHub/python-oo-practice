"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
    def __init__(self, start=0):
        self.add_one = start
        self.start = self.add_one
        
    def generate(self):
        self.add_one += 1
        return self.add_one - 1
    
    def reset(self):
        self.add_one = self.start

