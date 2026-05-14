class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],
        '5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],
        '9':['w','x','y','z']}
        ans = []
        n = len(digits)
        def helper(i,curr_s):
            if i >=n:
                ans.append(curr_s[:])
                return
            digit = digits[i]
            for letter in mapping[digit]:
                new_s=curr_s+letter
                helper(i+1,new_s)
            return
        helper(0,'')
        return ans
            