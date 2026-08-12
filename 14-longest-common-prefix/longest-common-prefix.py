class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as prefix
        prefix = strs[0]
        
        for string in strs[1:]:
            # Reduce prefix until it matches the start of string
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix


# ----------- Test Cases -----------

if __name__ == "__main__":
    sol = Solution()
    
    print(sol.longestCommonPrefix(["flower","flow","flight"]))  # Expected: "fl"
    print(sol.longestCommonPrefix(["dog","racecar","car"]))     # Expected: ""

        