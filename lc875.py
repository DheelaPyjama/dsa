# Koko eating bananas
import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            return hours <= h

        l,r=1,max(piles)
        while l < r:
            k = (l+r) // 2
            if k_works(k):
                r=k
            else:
                l=k+1
        return l
            
        