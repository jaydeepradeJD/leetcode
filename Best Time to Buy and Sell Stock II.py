class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy_ptr, sell_ptr = 0, 1
        if len(prices) == 1:
            return 0
        
        while (sell_ptr < len(prices)) and (buy_ptr < len(prices)):
            if prices[sell_ptr] > prices[buy_ptr]:
                profit += prices[sell_ptr] - prices[buy_ptr]
                buy_ptr = sell_ptr
                sell_ptr += 1
            else:
                buy_ptr = sell_ptr
                sell_ptr += 1    
        return profit