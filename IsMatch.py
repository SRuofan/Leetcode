# To solve this problem, we should divide the problem into several sub-problems
# we should look forward to the next digit of string p and s to check if there is a * sitting at p[1] or s[1]
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        :Usage: regular expression realized in python code, but not passed the leetcode because of running time limited
        """
        s = list(s)
        p = list(p)

        if s == [] and p == []:
            return True


        # Check if p[1] is '*', then we should skip 'correct' number of same characters as p[0] in string s.
        # The prerequisite is that len(p) >= 2

        if len(p) >= 2 and p[1] == '*':
            # Create temporary variable saving string s
            # We should also consider this '*' is the last character in string p
            next_s = s[:]
            if len(p) >= 3:
                next_p = p[2:len(p)]
                # We skip any numbers of characters same as p[0] in string s
                while next_s != [] and (next_s[0] == p[0] or p[0] == '.'):
                    next_s.pop(0)
                    if self.isMatch(next_s, next_p):
                        return True
                # When the character before '*'(p[0]) is different to s[0], we should skip p[0] and p[1]
                return self.isMatch(s, next_p)
            # When '*' is the last character
            else:
                while next_s != [] and (next_s[0] == p[0] or p[0] == '.'):
                    next_s.pop(0)
                    if self.isMatch(next_s, ''):
                        return True
                return self.isMatch(s, '')

        # The same operation for string s
        if len(s) >= 2 and s[1] == '*':
            next_p = p[:]
            if len(s) >= 3:
                next_s = s[2: len(s)]
                while next_p != [] and (next_p[0] == s[0] or s[0] == '.'):
                    next_p.pop(0)
                    if self.isMatch(next_s, next_p):
                        return True
                return self.isMatch(next_s, p)
            else:
                while next_p != [] and (next_p[0] == s[0] or s[0] == '.'):
                    next_p.pop(0)
                    if self.isMatch('', next_p):
                        return True
                return self.isMatch('', p)

        # When the next character in both s and p is not '*', we should verify if s[0] == p[0] or one of s[0] and p[0] is '.'
        # Check both strings terminate simutaneously
        if (s == [] and p != []) or (s != [] and p == []):
            return False
        # Check if the character is the same and return the next sub-problem
        if s[0] == p[0] or s[0] == '.' or p[0] == '.':
            s.pop(0)
            p.pop(0)
            return self.isMatch(s, p)
        # Then, return false if this two character is different
        if s[0] != p[0]:
            return False
