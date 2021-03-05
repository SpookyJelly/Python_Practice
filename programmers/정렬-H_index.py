# 정렬 H-index
"""
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

제한사항

과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
논문별 인용 횟수는 0회 이상 10,000회 이하입니다.


"""
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    print(citations)
    for i in range(len(citations)):
        cnt = 0
        for j in range(0,i+1):
            if citations[j] >= citations[i]:
                cnt += 1
        if cnt == citations[i] and cnt >= len(citations) - i:
            answer = cnt
            return answer
# 복잡도는 O(n^2)인데, 역순으로 살피니까 금방 return값을 찾을 수 있지않을까?
# 아 나머지 논문 조건을 빼먹었구나... 넣었는데도 빵꾸났다.

"""
- 개선방안

*1. H-index는 citations의 원소가 아닐 수도 있어요.

[12,11,10,9,8,1] => 5
[6,6,6,6,6,1] => 5

두 testcase 모두 인용 횟수가 5 이상인 논문이 5개 이상 있으므로 H-index가 5가 됩니다!
문제에 citations 원소 중에 H-index가 있단 말이 없더라구요..
이것 때문에 엄청 헤맸네요ㅠㅠ

*2. 모든 논문의 인용 횟수가 논문의 갯수보다 많을 때는 논문의 갯수를 return 해야 해요!

[20,21,22,23] => 4 // 댓글 보고 수정했습니다! 감사합니다ㅎㅎ
[4,4,4] => 3

"""

# 최대 인용 횟수 찾은 다음 -1 씩 해가면서 조사?
# 논문의 갯수에서 -1 씩???

# cit = [3,0,6,1,5]
cit = [12,11,10,9,8,1]
print(solution(cit))

