# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can
# be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

class Solution:
    def longestPalindrome(self, s):
        result = 0
        print(set(s))
        odds = []
        biggest_odd = ''
        biggest_odd_count = 0
        for char in set(s):
            if s.count(char) % 2 == 0:
                result += s.count(char)
            else:
                if s.count(char) > biggest_odd_count:
                    biggest_odd = char
                    biggest_odd_count = s.count(char)
        print(biggest_odd)
        print(biggest_odd_count)
        for char in set(s):
            if s.count(char) % 2 != 0 and char != biggest_odd:
                result += s.count(char) - 1
            elif s.count(char) % 2 != 0:
                result += biggest_odd_count
        return result

# input -> "ajaufghrufhkvhvielllllllfjsssjsfjjsnmcjeufnulwealjvaf"
# output -> 41