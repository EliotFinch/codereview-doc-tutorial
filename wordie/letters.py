import random

class letters:
    """Class for letters."""
    def __init__(self, s: str):
        if not s.isalpha():
            raise ValueError("String must be only letters.")
        self._s = s

    def __repr__(self):
        return f"letters({self._s})"

    def __str__(self):
        return self._s

    def shuffle(self):
        """Shuffle the letters. Shuffling is done in-place."""
        self._s = ''.join(random.sample(self._s, len(self._s)))
