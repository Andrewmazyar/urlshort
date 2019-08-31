import random
import string


class Shorter:

    def __init__(self, size=10):
        self.size = size if size is not None else 10

    def issue(self):
        letter = string.ascii_letters
        return ''.join(random.choice(letter) for _ in range(self.size))