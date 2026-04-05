class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} 
        for i in nums:
            count[i] = 1 + count.get(i,0) 

        r = []
        for i, cnt in count.items():
            r.append([cnt, i])
        r.sort()

        result = []
        while len(result) < k:
            result.append(r.pop()[1])
        return result