"""
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.

"""


class Solution:
    def reorderLogFiles(self, logs: list) -> list[str]:
        digits, letter = [], []
        for log in logs:
            # 여기서 log는 logs의 요소들
            # 근데 그 요소들을 공백 단위로 쪼개고, 그 중 1번 인덱스에 있는게 숫자인지 확인
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letter.append(log)

        # 분리를 했으니 이제 정렬을 해야지
        # sort는 key로 함수를 받아, lambda도 받는다.
        # 여기서 우선순위는 x.split()[1:] 을 오름차순으로, 동일하다면 x.split()[0]을 오름차순으로 정렬한다. (정방향)
        letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letter + digits

"""
Success Details 
Runtime: 36 ms, faster than 71.45% of Python3 online submissions for Reorder Data in Log Files.
Memory Usage: 14.3 MB, less than 67.16% of Python3 online submissions for Reorder Data in Log Files.

"""