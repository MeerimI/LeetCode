class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
             
        candy = []
        for i in range(len(candies)):
            b = 0
            res = candies[i] + extraCandies  
            for j in candies:                 
                if res >= j:                   
                    b += 1                     
            if b == len(candies):
                candy.append(True)
            else:
                candy.append(False)    
        return candy