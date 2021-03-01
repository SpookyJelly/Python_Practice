"""
Write a function that reverses a string.
The input string is given as an array of characters char[].

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

"""

class Solution:
    def reverseString(self, s:list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 조건에 맞는 문자열 하나를 가르키는 포인터를 지정해서 해결
        # 2개의 포인터를 이용해서 범위를 조정해가며 풀이한다.
        left,right = 0, len(s)-1
        while left<right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1

"""
Success Details 
Runtime: 188 ms, faster than 91.08% of Python3 online submissions for Reverse String.
Memory Usage: 18.5 MB, less than 57.88% of Python3 online submissions for Reverse String.

추가 풀이

1. .reverse() 메서드 사용하기
-> 문제에서도 return 값이 필요없고, 원본만 반환하면 된다고 했기에 무관

2. s[:] = s[::-1] 사용
-> s = s[::-1]은 오답이 나는데, 이 문제는 공간 복잡도를 O(1)로 잡았기 때문이다.
-> 공간 복잡도 O(1)는 자료의 크기와 무관하게 항상 동일한 시간이 걸려야한다.
-> s = s[::-1]은 아마도 s의 크기를 파악하는 과정이 추가로 들어가기 때문에 O(1)이 아닌듯

"""


a = Solution()
B = ['A','A','A','B','B','B']
print(a.reverseString(B))
print(B)


