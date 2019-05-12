import string


class KMP:
    @staticmethod
    def search(str, p):

        i = 0
        j = 0
        lps = KMP.buildLongestPrefixSuffix(p)
        while i < len(str):
            if p[j] == str[i]:
                j += 1
                i += 1
            if j == len(p):
                return i - j

            # no match means we check lower prefix sum or increment
            if p[j] != str[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1

    @staticmethod
    def buildLongestPrefixSuffix(p):
        # lps[i] = length of the longest prefix suffix
        lps = [0] * len(p)
        lps[0] = 0

        matchedLength = 0
        i = 1

        while i < len(p):

            # if matched, increment match length
            if p[i] == p[matchedLength]:
                matchedLength += 1
                lps[i] = matchedLength
                i += 1
            else:
                # if no match, check if we can match prefix of previous
                if matchedLength != 0:
                    matchedLength = lps[matchedLength - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    @staticmethod
    def prettySearch(str, p):
        idx = KMP.search(str, p)
        if idx != -1:
            print("pattern found at index: %i" % (idx))
            print(str[:idx] + '(' + str[idx:idx + len(p)] + ')' + str[idx + len(p):])
        else:
            print("pattern not found")


class BoyerMoore:

    @staticmethod
    def buildLastOccurrence(p):
        lo = {c: -1 for c in string.ascii_letters}

        for i, c in enumerate(p):
            lo[c] = i

        return lo

    @staticmethod
    def search(str, p):
        lo = BoyerMoore.buildLastOccurrence(p)
        idx = len(p)

        offset = 1

        while idx <= len(str):

            # all chars matched
            if offset >= len(p):
                return idx - offset

            # check char
            elif str[idx - offset] == p[-offset]:
                offset += 1

            # shift by last occurrence
            else:
                idx += max(1, offset - lo[str[idx - offset]])
                offset = 1

        return -1

    @staticmethod
    def prettySearch(str, p):
        idx = BoyerMoore.search(str, p)
        if idx != -1:
            print("pattern found at index : %i" % idx)
            print(str[:idx] + '(' + str[idx:idx + len(p)] + ')' + str[idx + len(p):])
        else:
            print("pattern not found")


def example1():
    str = "aabbabxaba"
    p = 'abxab'

    KMP.prettySearch(str, p)
    BoyerMoore.prettySearch(str, p)


if __name__ == "__main__":
    example1()
