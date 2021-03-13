"""
Given a list of daily temperatures T,
return a list such that, for each day in the input,
tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].


"""
class Solution:
    def dailyTemperatures(self, T: list) -> list:
        stack = [] # 여기에서 인덱스를 받는다
        result = [0]*len(T) # 결과를 받는 곳
        for i in range(len(T)):
            current = T[i]
            # 스택이 있고 현재 값이 스택 제일 끝. 그러니까 계속 쌓이고 있는 값보다 크다면
            while stack and current > T[stack[-1]]:
                last = stack.pop()
                ans = i-last
                result[last] = ans

            stack.append(i)
        return result

a = Solution()
print(a.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

"""
Success Details 
Runtime: 488 ms, faster than 94.19% of Python3 online submissions for Daily Temperatures.
Memory Usage: 18.7 MB, less than 63.03% of Python3 online submissions for Daily Temperatures.


"""
