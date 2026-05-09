class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k>=len(num):
            return "0"
        stack = []
        pop_ind = [1]*len(num)
        num2=num+"0"
        ans_str=""
        for i in range(len(num2)):
            while k and stack and int(num2[stack[-1]])>int(num2[i]):
                pop_ind[stack.pop()] = 0
                k-=1
            stack.append(i)
        print(pop_ind)
        for i in range(len(num)):
            if len(ans_str)==0 and num[i]=='0':
                continue
            if pop_ind[i]==1:
                ans_str+= num[i] 

        return ans_str if len(ans_str) else "0"
        
                

