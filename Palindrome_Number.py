class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # Commpute how many digits the number has
        i = 0
        x = abs(x)
        temp = x
        if x == 0:
            return True
        while temp/10 > 0:
            temp = temp/10
            i += 1

        # Check the middle digit
        if i%2 == 0:                  # There are odd digits
            middle = i/2
        else:
            middle = i/2+1
        for j in range(0, middle, 1):
            if int(x/(10**i))%10 == int(x/(10**j))%10:
                i -= 1
                j += 1
            else:
                return False

        return True
