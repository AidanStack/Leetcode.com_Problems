# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if
# either(a == c and b == d), or (a == d and b == c) - that is, one domino can be  rotated to be equal to another domino.
#
# Return the number of pairs(i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].
#
# Example 1:
# Input: dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]]
# Output: 1

def numEquivDominoPairs(self, doms):
    result = 0

    dict = {}
    dict_prime = {}

    for i in range(len(doms)):

        if (doms[i][0], doms[i][1]) not in dict and (doms[i][1], doms[i][0]) not in dict:

            dict[(doms[i][0], doms[i][1])] = 0
            dict_prime[(doms[i][0], doms[i][1])] = 1

        elif (doms[i][0], doms[i][1]) in dict:

            dict[(doms[i][0], doms[i][1])] += dict_prime[(doms[i][0], doms[i][1])]
            dict_prime[(doms[i][0], doms[i][1])] += 1

        elif (doms[i][1], doms[i][0]) in dict:

            dict[(doms[i][1], doms[i][0])] += dict_prime[(doms[i][1], doms[i][0])]
            dict_prime[(doms[i][1], doms[i][0])] += 1

    for i in dict:
        result += dict[i]

    return result