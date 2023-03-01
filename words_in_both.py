# Author: Justin Huang
# GitHub username: huangjus
# Date: 2/28/23
# Description: Takes two strings as input and returns a set of lower-case words that appear in both strings.

def words_in_both(string1, string2):

    """
    Find the words that appear in both input strings.

    string1: The first input string.
    string2: The second input string.
    """

    words1 = string1.lower().split()
    words2 = string2.lower().split()

    common_words = set(words1) & set(words2)

    return common_words
