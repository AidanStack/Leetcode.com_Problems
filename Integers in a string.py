# You are given a string word that consists of digits and lowercase English letters.
#
# You will replace every non-digit character with a space. For example, "a123bc34d8ef34" will become " 123  34 8  34".
# Notice that you are left with some integers that are separated by at least one space: "123", "34", "8", and "34".
#
# Return the number of different integers after performing the replacement operations on word.
#
# Two integers are considered different if their decimal representations without any leading zeros are different.
#
# Example 1:
#
# Input: word = "a123bc34d8ef34"
# Output: 3
# Explanation: The three different integers are "123", "34", and "8". Notice that "34" is only counted once.

class Solution:
    def numDifferentIntegers(self, word):

        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        switch = 'off'

        nums = []

        index = 0

        for i in range(len(word)):
            if switch == 'off':
                if word[i] in digits:
                    nums.append(word[i])
                    switch = 'on'
            elif switch == 'on':
                if word[i] in digits:
                    nums[index] += word[i]
                else:
                    index += 1
                    switch = 'off'

        for i in range(len(nums)):
            nums[i] = str(int(nums[i]))

        return len(set(nums))

