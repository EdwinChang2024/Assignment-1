import pytest
from week1 import editor
## dont change anything!!!
def test_num():
	assert editor('data/number.txt') == '1857617284'

import unittest
from week1 import editor

class TestWeek1a(unittest.TestCase):
    def test_number_file(self):
        self.assertEqual(editor("./data/numbers.txt"), "1234567890")

    def test_story_file(self):
        modified_content, top_five = editor("./data/story.txt")
        self.assertEqual(modified_content, "once upon a time, there was a curious cat named whiskers. whiskers loved to explore the neighborhood and make new friends. one day, whiskers stumbled upon a mysterious garden filled with colorful flowers and enchanting creatures. intrigued, whiskers decided to venture deeper into the garden, unaware of the adventure that awaited.")
        self.assertListEqual(top_five, ["a", "and", "the", "to", "whiskers"])

    def test_invalid_file(self):
        with self.assertRaises(ValueError):
            editor("./data/invalid.txt")

if __name__ == '__main__':
    unittest.main()