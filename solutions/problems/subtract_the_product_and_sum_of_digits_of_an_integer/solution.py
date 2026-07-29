class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        tot=0
        while n>0:
            d=n%10
            product*=d
            tot+=d
            n=n//10
        return product-tot
     



        