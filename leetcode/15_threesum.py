# 15. threesum (medium)
class Solution:
    def threeSum(self, nums:list) -> list:
        result = []
        nums.sort() # 여기가 핵심인듯, 포인터의 이득을 극한으로 살릴라고, 방향성을 주었다
        # 작으면 left가 커지게, 크면 right가 작아지게
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left<right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0 :
                    left +=1
                elif sum > 0:
                    right -=1
                else: # 여기도 엄청 스마트하다. else로 들어오는 경우는 일단 전부 정답 케이스인 경우.
                    # 이제 여기서부터 정답처리 및 "중복 스킵"의 과정이 들어간다.
                    result.append([nums[i],nums[left],nums[right]])
                    # 이하 두개의 while문은 left right 포인터의 zen을 해치지 않는다.
                    # (left 포인터는 조사 범위의 가장 좌측을 벗어나지 않고, right 포인터는 조사 범위의 가장 우측을 벗어나지 않는다)
                    # 그럼과 동시에 중복 체크를 하는 방식도 스마트하다...
                    # 만약에 left 다음이 left와 동일하면 left를 증가시켜 right와 가까워지게 해 while문 탈출조건에 가까워지게한다.
                    # 그리고 else문 마지막에 보면 양쪽 포인터가 동시에 증감하는데, 어느 한 쪽만 커진다면 sum =0 인 상태를 무조건 해치게 된다.\
                    # 따라서 둘 다 움직여야하는 것이 맞다.

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left > right and nums[right] == nums[right-1]:
                        right -= 1
                    left+=1
                    right-=1
        return result
a= Solution()
print(a.threeSum([-1,0,1,2,-1,4]))


'''
Success Details 
Runtime: 832 ms, faster than 77.58% of Python3 online submissions for 3Sum.
Memory Usage: 17.4 MB, less than 75.06% of Python3 online submissions for 3Sum.
Next challenges:

'''


        # 조합과 순열로 풀어볼라니까 더 어렵고, 중복 순열 / 중복 개념까지 끌고 와야한다.
        # 거기다가 재귀 구조로 해결하는 내 특성 상, 단순한 브루트 포스보다 더 시간이 오래 걸릴 것이라 생각된다.
        # 문제에 나온대로 2포인터로 풀어보자
        # N = 3
        # result=[0]*N    # 조합으로 변할 리스트
        # check = [0] * len(nums)
        # def com(L:int):
        #     if L == N:
        #         if sum(result) == 0:
        #             print(result)
        #         return
        #     else:
        #         for i in range(len(nums)):
        #             if check[i] == 0:
        #                 result[L] = nums[i]
        #                 check[i] = 1
        #                 com(L+1)
        #                 check[i] = 0
        #             # if not nums[i] in result:
        #             #     result[L] = nums[i]
        #             #     com(L+1)
        #
        # com(0)
