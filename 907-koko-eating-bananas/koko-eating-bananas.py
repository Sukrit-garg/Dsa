class Solution:
    def calculateHours(self,speed,piles):
        time = 0
        for i in piles:
            time+=(i+speed-1)//speed
        return time
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low<=high:
            mid = (low+high)//2
            time = self.calculateHours(mid,piles)
            if time >h:
                low = mid+1
            else:
                high = mid-1
        return low