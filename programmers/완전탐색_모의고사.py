# 완전 탐색 
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 10000문제 정도면 껌이니까 그냥 요령없이 처음부터 끝까지 쭉 간다
def solution(answers:list):

    supo1 = [1,2,3,4,5]
    supo1_len = len(supo1)
    supo2 = [2,1,2,3,2,4,2,5]
    supo2_len = len(supo2)
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    supo3_len = len(supo3)

    ans1=ans2=ans3= 0
    for idx in range(len(answers)):
        if answers[idx] == supo1[idx%supo1_len]:
            ans1 +=1
        if answers[idx] == supo2[idx%supo2_len]:
            ans2 +=1
        if answers[idx] == supo3[idx%supo3_len]:
            ans3+=1
    
    answer = []
    max_cnt = max(ans1,ans2,ans3)
    for (idx,ans) in enumerate([ans1,ans2,ans3]):
        if max_cnt == ans:
            answer.append(idx+1)

    return answer


print(solution([1,3,2,4,2]))
