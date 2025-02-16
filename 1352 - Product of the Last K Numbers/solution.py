class ProductOfNumbers:

    def __init__(self):
        self.lt2 = []
        self.z = -1

    def add(self, num: int) -> None:
        if num == 0:
            num = 1
            self.z = len(self.lt2)
        self.lt2.append(self.lt2[-1]*num if len(self.lt2) > 0 else num)

    def getProduct(self, k: int) -> int:
        if self.z!=-1 and len(self.lt2) - k <= self.z:
            return 0
        return self.lt2[-1]//(self.lt2[-k-1] if len(self.lt2) > k else 1)


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)