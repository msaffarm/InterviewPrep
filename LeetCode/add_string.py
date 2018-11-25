# Given two non-negative 
# integers num1 and num2 represented as string, return the sum of num1 and num2.

# Note:

# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert 
# the inputs to integer directly.


####################
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        max_num, min_num = num2,num1
        if len(num1) >= len(num2):
            max_num = num1
            min_num = num2
        length_diff = len(max_num) - len(min_num)
        res = []
        carry = 0
        min_num = list(min_num)[::-1]
        max_num = list(max_num)[::-1]    
        for idx,ch in enumerate(min_num):
            dig, carry = (int(ch)+int(max_num[idx])+carry)%10,(int(ch)+int(max_num[idx])+carry)//10
            res.append(str(dig))
        
        min_length = len(min_num)
        for i in range(length_diff):
            dig, carry = (int(max_num[i+min_length])+carry)%10,(int(max_num[i+min_length])+carry)//10
            res.append(str(dig))

        if carry:
        	res.append(str(carry))

        # print(res[::-1])
        return "".join(res[::-1])


def main():
	s = Solution()
	print(s.addStrings("1","9"))



if __name__ == '__main__':
	main()