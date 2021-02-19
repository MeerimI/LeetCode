class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
             
        result = []
        for i in range(len(candies)):
            b = 0
            res = candies[i] + extraCandies  
            for j in candies:                 
                if res >= j:                   
                    b += 1                     
            if b == len(candies):
                result.append(True)
            else:
                result.append(False)    
        return result
