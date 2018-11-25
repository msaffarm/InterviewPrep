# recursive impelmentation of pow(x,n)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1.0
        if n < 0:
            x = 1/x
            n = -n
        return x**(n%2) * self.myPow(x*x,n//2)
        


def main():
    s = Solution()
    print(s.myPow(2,-5))


if __name__ == '__main__':
    main()