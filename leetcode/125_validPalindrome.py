"""
Given a string s, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

"""
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''

        for idx in range(len(s)):
            if 65<= ord(s[idx]) <= 90 or 97 <= ord(s[idx]) <= 122 or 48<= ord(s[idx]) <= 57:
                result += s[idx]

        result = result.replace(' ','')
        result = result.lower()
        return result == result[::-1]

# a = Solution() # 클래스 간만에 쓰니까 헷갈렸네. 객체 a를 Solution 클래스로 만들어주려면 뒤에 ()까지 반드시 추가해야함

"""

Success Details 
Runtime: 64 ms, faster than 21.73% of Python3 online submissions for Valid Palindrome.
Memory Usage: 14.6 MB, less than 64.69% of Python3 online submissions for Valid Palindrome.

--> 문자를 필터링 하는 방식이 확실히 너무 느리다. 이거 보완 가능한 방법은?

1. .isalnum() 문자열 메서드 사용하기
 이것은 이 문자열이 숫자형이나거나 알파벳형이면 True를 반환해주고, 아니면 False를 반환한다.
 이걸 쓰면 엄청 길었던 조건문을 짧게 바꿀 수 있겠다.
 
2. 정규표현식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]','',s)
    단, 정규표현식을 사용하려면, re 라이브러리를 import 해야한다.

3. 데크 자료형을 이용한 문자 필터링
  -> 아직 안배워서 잘 모르겠다.
  
# 대부분의 문자열 처리 문제는 슬라이싱으로 해결하는 것이 가장 빠르다.
 
"""





