# 819. Most common word

"""
Given a string paragraph and a string array
of the banned words banned, r
eturn the most frequent word that is not banned.
It is guaranteed there is at least one word that is not banned,
and that the answer is unique.

The words in paragraph are case-insensitive and
the answer should be returned in lowercase.

Constraints:

1 <= paragraph.length <= 1000
paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
0 <= banned.length <= 100
1 <= banned[i].length <= 10
banned[i] consists of only lowercase English letters.
"""
# 정규표현식 사용
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list):
        # sub 모듈 == 첫번째 매개변수 -> 바꿔줄 변수 , 두번째 매개변수 -> 이것으로 바꾸겠다, 세번째 매개변수 : 어디에서?
        # .lower() -> 소문자 변환 .split() --> 띄어쓰기 단위로 구분

        # 결론적으로 re.sub는 paragraph을 소문자화 하고, 띄어쓰기 단위로 구분한 객체에서
        # 문자 + 숫자가 아닌 글자들을 ' ' 으로 바꾼 객체가 된다.
        paragraph = [word for word in re.sub(r'[^\w]',' ', paragraph).lower().split() if word not in banned]

        maxi = 0
        word_set = list(set(paragraph))
        for idx in range(len(word_set)):
            cnt = paragraph.count(word_set[idx])
            if maxi < cnt:
                maxi = cnt
                result = word_set[idx]
        return result



a = Solution()
paragraph ="Bob hit a ball, the hit BALL flew far after it was hit."
banned = ['hit']
print(a.mostCommonWord(paragraph,banned))

"""
Success Details 
Runtime: 36 ms, faster than 66.58% of Python3 online submissions for Most Common Word.
Memory Usage: 14.5 MB, less than 20.43% of Python3 online submissions for Most Common Word.

"""