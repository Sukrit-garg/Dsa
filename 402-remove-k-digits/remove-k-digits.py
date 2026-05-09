class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):        
            return '0'

        stack = []

        for c in num:
            while k and stack and c < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(c)
            
        for _ in range(k):
            stack.pop()
        
        res = ''.join(stack).lstrip('0')
        
        return res if res else "0"