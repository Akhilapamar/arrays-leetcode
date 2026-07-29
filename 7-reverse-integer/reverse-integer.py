class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        result = 0
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check overflow BEFORE multiplying##
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return 0
            
            result = result * 10 + digit
        
        result *= sign
        
        # Final safety check (for negative boundary)
        if result < INT_MIN or result > INT_MAX:
            return 0
        
        return result


# ----------- Test Cases -----------

if __name__ == "__main__":
    sol = Solution()

    print(sol.reverse(123))          # 321
    print(sol.reverse(-123))         # -321
    print(sol.reverse(120))          # 21
    print(sol.reverse(-10))          # -1  ✅
    print(sol.reverse(-1563847412))  # 0   ✅
