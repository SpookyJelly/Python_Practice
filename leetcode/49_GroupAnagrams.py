#49. Group Anagrams

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
"""

# 개쩌는 아이디어 : 애너그램 관계인 문자열은, 정렬하면 같은 값이 된다.

class Solution:
    def groupAnagrams(self, strs: list) -> list:
        word_dic = {

        }
        # 딕셔너리 자료형의 장점을 십분 이용하자
        for word in strs:
            a = ''.join(sorted(word))
            print(a)
            # .get()에 그냥 sorted(word) 넣으니까 list는 unhashable하다고 나오는데, 애초에 hash 가 뭘까?
            # 아무튼, sorted 하면 리스트가 나오는데, 그걸 join 메서드를 이용해서 다시 문자꼴로 묶어줬다.
            # 그리고 항상 자주 쓰던 방식으로, 키 값 없이도 디폴트 값 만들어주는 사전을 이용했다.
            word_dic[a] = word_dic.get(a,[]) + [word]
        # 마지막으로 동일 범주로 묶인 value들을 일괄 반환하자
        return word_dic.values()



a =Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(a.groupAnagrams(strs))

"""
Success Details 
Runtime: 92 ms, faster than 88.71% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.4 MB, less than 71.87% of Python3 online submissions for Group Anagrams.
Next challenges:

"""