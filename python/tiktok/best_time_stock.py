from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        highest_profit = 0

        for price in prices[1:]:
            if (price - lowest_price) > highest_profit:
                highest_profit = price - lowest_price
            if price < lowest_price:
                lowest_price = price

        return highest_profit