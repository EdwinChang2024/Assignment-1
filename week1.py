#Week 1 Test

# For file with only numbers, you should only return one thing(i.e.the first 10 characters)

# For file with story,you NEED to return two things(i.e. a modified string AND a list)
#  you can return multiple values by simply return them separated by commas like the following
# def editor(fname):
#
#     return 'modifystring', [a,b,c,d]

# HINT: to call your function for the story.txt file, use the following command
# editor("./data/story.txt")
# return statement should be in the format below
# return 'modifystring', [a,b,c,d]



import re
from collections import Counter

def editor(fname):
    #YOUR CODE STARTS HERE
    #Week 1 Test

# For file with only numbers, you should only return the first 10 characters
# For file with story, you NEED to return two things (i.e. a modified string AND a list)
#  you can return multiple values by simply return them separated by commas like the following
# def editor(fname):
#     return 'modifystring', [a,b,c,d]

# HINT: to call your function for the story.txt file, use the following command
# editor("./data/story.txt")
# return statement should be in the format below
# return 'modifystring', [a,b,c,d]

import re
from collections import Counter

def editor(fname):
    with open(fname, 'r') as f:
        content = f.read().strip()

    if fname.endswith('number.txt'):
        return content[:10]
    elif fname.endswith('story.txt'):
        modified_content = content.lower()
        word_counts = Counter(re.findall(r'\w+', modified_content))
        top_five = [word for word, _ in word_counts.most_common(5)]
        return modified_content, top_five
    else:
        raise ValueError(f"Unsupported file type: {fname}")