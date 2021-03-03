# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.The order
# of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the
# given words are sorted lexicographicaly in this alien language.
#
# Example 1:
# Input: words = ["hello", "leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in the alien language, then sequence is sorted.
#
# Example 2:
# Input: words = ["word", "world", "row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
#
# Example 3:
# Input: words = ["apple", "app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter( in size.) According to
# lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less
# than any other character(More info).
#
# Constraints:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.


class Solution:
    def isAlienSorted(self, words, order):

        for i in range(len(words) - 1):

            if len(words[i]) > len(words[i + 1]):
                if words[i + 1] == words[i][0:len(words[i + 1])]:
                    return False
                for j in range(len(words[i + 1])):
                    if order.index(words[i][j]) < order.index(words[i + 1][j]):
                        break
                    elif order.index(words[i][j]) == order.index(words[i + 1][j]):
                        pass
                    elif order.index(words[i][j]) > order.index(words[i + 1][j]):
                        return False

            else:
                for j in range(len(words[i])):
                    if order.index(words[i][j]) < order.index(words[i + 1][j]):
                        break
                    elif order.index(words[i][j]) == order.index(words[i + 1][j]):
                        pass
                    elif order.index(words[i][j]) > order.index(words[i + 1][j]):
                        return False

        return True



