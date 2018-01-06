class Solution:
    def selfDividingNumbers(self, left, right):
        def self_dividing(num):
            """
            Alternate implementation of self_dividing:
            def self_dividing(n):
                x = n
                while x > 0:
                    x, d = divmod(x, 10)
                    if d == 0 or n % d > 0:
                        return False
                return True
            """
            for n in str(num):
                if n == '0' or num % int(n) != 0:
                    return False
            return True
        ans = []
        for i in range(left, right + 1):
            if self_dividing(i):
                ans.append(i)
        return ans  # Equals filter(self_dividing, range(left, right+1)
