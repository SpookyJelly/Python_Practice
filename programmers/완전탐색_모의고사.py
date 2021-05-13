# 완전 탐색 
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 10000문제 정도면 껌이니까 그냥 요령없이 처음부터 끝까지 쭉 간다
def solution(answers:list):

    # 학생별로 찍는 순서 패턴화
    supo1 = [1,2,3,4,5]
    supo1_len = len(supo1)
    supo2 = [2,1,2,3,2,4,2,5]
    supo2_len = len(supo2)
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    supo3_len = len(supo3)

    # 학생 1,2,3의 정답 횟수 초기화
    ans1=ans2=ans3= 0
    # % 연산자를 이용하여 idx의 증가 각자의 패턴 주기를 일치시킴
    # ex. idx == 6 -> 학생1은 supo1[1], 학생 2는 supo[6]와 answers[6]을 비교해야한다.
    # 그렇기 때문에, 각자의 정답 패턴 리스트의 길이를 넘어가는 경우, 다시 처음으로 돌아올 수 있게 % 연산자를 이용했다
    for idx in range(len(answers)):
        if answers[idx] == supo1[idx%supo1_len]:
            ans1 +=1
        if answers[idx] == supo2[idx%supo2_len]:
            ans2 +=1
        if answers[idx] == supo3[idx%supo3_len]:
            ans3+=1
    
    answer = []
    # 득점이 가장 높은 경우 산출
    max_cnt = max(ans1,ans2,ans3)
    # 학생 1,2,3의 득점을 enumterate를 통해 idx와 같이 출력
    # 학생들의 ans가 max_cnt와 일치한다면 idx+1를 answer에 append
    for (idx,ans) in enumerate([ans1,ans2,ans3]):
        if max_cnt == ans:
            answer.append(idx+1)
    # answer 반환
    return answer


print(solution([1,3,2,4,2]))
