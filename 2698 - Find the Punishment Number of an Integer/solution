class Solution:
    def continuousSubeqSum(self, n) -> bool:
        lt = []
        def cuur(index):
            if sum([int("".join(i)) for i in lt]) == int(int("".join(n))**0.5)  and sum([len(i) for i in lt]) == len(n):
                return True
            for size in range(1,len(n)-index+1):
                lt.append(n[index: index+size])
                if index+size >= len(n):
                    if sum([int("".join(i)) for i in lt]) == int(int("".join(n))**0.5):
                        return True
                    lt.pop(-1)
                    return
                if cuur(index+size):
                    return True
                lt.pop(-1)
            lt.pop(-1)
        return cuur(0) or False

    def punishmentNumber(self, n: int) -> int:
        ans = 0
        lt = [1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369, 370, 379, 414, 657, 675, 703, 756, 792, 909, 918, 945, 964, 990, 991, 999, 1000]
        for i in lt:
            if n >= i:
                ans += i*i
        return ans
        