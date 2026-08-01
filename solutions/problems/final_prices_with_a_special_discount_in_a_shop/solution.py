# class Solution:
#     def finalPrices(self, prices: List[int]) -> List[int]:

#         if a[i]>a[i+1]:
#             a[i]-a[i+j]
#         else:
#             if a[i]>a[i+2]:
#                 a[i]-a[i+2]
class Solution:
    def finalPrices(self, prices):
        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                prices[idx] -= prices[i]

            stack.append(i)

        return prices
# class Solution:
#     def finalPrices(self, prices):
#         stack = []  # will store indices

#         for i in range(len(prices)):
#             # resolve discounts for previous items
#             while stack and prices[stack[-1]] >= prices[i]:
#                 idx = stack.pop()
#                 prices[idx] -= prices[i]

#             stack.append(i)

#         return prices