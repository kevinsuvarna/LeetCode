class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        curr_min = prices[0]
        profit = 0
        ovr_profit = 0
        i = 0
        for i in range(0, len(prices)-1):
            if prices[i] < prices[i+1] and curr_min == -1:
                curr_min = prices[i]
            else:
                profit = prices[i] - curr_min
                if profit > ovr_profit:
                    ovr_profit = profit
                if prices[i+1] < curr_min:
                    curr_min = prices[i+1]
        profit = prices[i+1] - curr_min
        if profit > ovr_profit:
            ovr_profit = profit
        return ovr_profit
        # l, r = 0, 1
        # maxP = 0

        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         maxP = max(maxP, prices[r] - prices[l])
        #     else:
        #         l = r
        #     r += 1
        
        # return maxP