# https://leetcode.com/problems/palindrome-number/

import math

class Solution:
    def inPowersOfTen(self, number: int) -> int:
        while number > 0:
            remainder = number % 10
            number -= remainder
            number /= 10
            yield remainder
        return 0
        
    def numberAt(self, number: int, target_index: int) -> int:
        return (number % 10 ** (target_index+1) - (number % 10 ** target_index))/(10**target_index)
    
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        first_base = 10**(math.floor(math.log10(x)))
        first_num = x // first_base
        
        last_num = x % 10
        if first_num != last_num:
            return False
        x -= first_num * first_base
        x -= last_num
        x /= 10
        return self.isPalindrome(x)
            
        
    def isPalindromeString(self, x: int) -> bool:
        if x < 0:
            # Assuming negative numbers can't be palindromes
            return False
        num_as_str = str(x)
        mid = math.ceil(len(num_as_str)/2)
        for i in range(mid):
            if num_as_str[i] != num_as_str[-(i+1)]:
                return False
        return True
        
        
def test_palindrome():
    sol = Solution()
    
    cases = {121: True, 123: False, 10: False, 1234: False, 4334: True, 100021: False}
    
    for num, result in cases.items():
        assert sol.isPalindromeString(num) == result
    # for num, result in cases.items():
        # assert sol.isPalindrome(num) == result
        
if __name__ == '__main__':
    test_palindrome()
