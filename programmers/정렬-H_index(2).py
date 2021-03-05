# 정렬 H-index(2)
# 접근방법
"""
1. H-index는 citations의 길이를 넘어설 수 없다.
2. len(citation)만큼 반복
3. 매 루프마다 i가 증가, i는 잠재적 H-index이다.
4. 만약, i보다 citation의 요소가 더 크다면 cnt를 키운다.
5. 그렇게 cnt가 i보다 커지면 (잠재적 H-index보다 실제 요소들의 index가 높다) for문을 탈출하고 i를 하나 높혀준다
6. 모든 요소를 다 살펴보는데, break 없이 for문이 종료되면, cnt의 값이 곧 실제 H-index가 된다.
7. cnt는 i에 따라 계속 달라지므로, 매 for문 종료시마다 해당 값이 최대인지 확인해야한다.


"""
def solution(citations):
    answer = 0
    i = -1
    while i<= len(citations):
        i += 1
        cnt = 0
        for idx in range(len(citations)):
            if cnt >= i :
                break
            if citations[idx] >= i:
                cnt += 1
        if cnt > answer:
            answer = cnt
    return answer


cit = [6,6]
#cit =[3, 0, 6, 1, 5]
print(solution(cit))