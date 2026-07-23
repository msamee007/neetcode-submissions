class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        a = [0] * n
        stack = []      # stores indices

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                x= stack.pop()
                a[x] = i - x
            stack.append(i)

        return a