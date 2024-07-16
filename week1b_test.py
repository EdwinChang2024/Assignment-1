import pytest
from week1 import editor
## dont change anything!!!
def test_story1():
	new_text, top_five = editor('data/story.txt')
	expected=['the','of','and','with','a']
	assert set(top_five)==set(expected)
	assert new_text == '''the man and his wife, talking of the latest armed robbery in the suburb, were distracted by the sight of the little boy's pet cat effortlessly arriving over the seven-foot wall, descending first with a rapid bracing of extended forepaws down on the sheer vertical surface, and then a graceful launch, landing with swishing tail within the property.'''

import unittest
from week1 import editor

class TestWeek1b(unittest.TestCase):
    def test_number_file_longer(self):
        self.assertEqual(editor("./data/numbers_longer.txt"), "1234567890")

    def test_story_file_with_punctuation(self):
        modified_content, top_five = editor("./data/story_with_punctuation.txt")
        self.assertEqual(modified_content, "once upon a time, there was a curious cat named whiskers. whiskers loved to explore the neighborhood and make new friends. one day, whiskers stumbled upon a mysterious garden filled with colorful flowers and enchanting creatures. intrigued, whiskers decided to venture deeper into the garden, unaware of the adventure that awaited.")
        self.assertListEqual(top_five, ["the", "a", "and", "to", "whiskers"])

    def test_empty_file(self):
        self.assertEqual(editor("./data/empty.txt"), "")

if __name__ == '__main__':
    unittest.main()