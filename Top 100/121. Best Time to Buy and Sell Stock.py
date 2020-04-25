"""
  Complexity Analysis

    Time complexity : O(n2)
    Space complexity : O(1)
    Only two variables - \text{maxprofit}maxprofit and \text{profit}profit are used.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_dif = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                dif = prices[j] - prices[i]
                if max_dif < dif:
                    max_dif = dif
        return max_dif


"""
  The points of interest are the peaks and valleys in the given graph. We need to find the largest peak following the smallest valley. We can maintain two variables - minprice and maxprofit corresponding to the smallest valley and maximum profit (maximum difference between selling price and minprice) obtained so far respectively.
"""


# Steps:

# 1. Track: MinPrice
# 2. Track max_profit.

"""
  Complexity Analysis:
    Time complexity : O(n)
    Space complexity : O(1) 
""" 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            
            profit = prices[i] - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit
