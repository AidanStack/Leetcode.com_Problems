# A decimal number is called deci - binary if each of its digits is either 0 or 1 without any leading zeros.For example,
# 101 and 1100 are deci - binary, while 112 and 3001 are not.
#
# Given a string n that represents a positive decimal integer, return the  number of positive deci - binary numbers neede
# so that they sum up to n.
#
# Example 1:
# Input: n = "32"
# Output: 3
# Explanation: 10 + 11 + 11 = 32
#
# Example2:
# Input: n = "82734"
# Output: 8
#
# Example3:
#
# Input: n = "27346209830709182346"
# Output: 9

class Solution:
    def minPartitions(self, n):
        result = 0
        while int(n) > 0:
            n = ''.join([str(int(i ) -1) if int(i ) >0 else i for i in n])
            result += 1
        return result
