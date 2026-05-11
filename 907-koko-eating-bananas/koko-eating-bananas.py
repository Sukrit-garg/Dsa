class Solution:
    def calculateHours(self,speed,piles):
        time = 0
        for i in piles:
            if i%speed==0:
                time+=i//speed
            else:
                time+=i//speed+1
        return time
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = 0
        while low<=high:
            mid = (low+high)//2
            time = self.calculateHours(mid,piles)
            if time >h:
                low = mid+1
            else:
                ans = mid
                high = mid-1
        return ans