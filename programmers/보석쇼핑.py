# 보석쇼핑
# 진열된 모든 종류의 보석을 적어도 1개이상 포함하는 가장 짧은 구간을 찾아서 구매

#진열대 번호 순서대로 보석들의 이름이 저장된 배열 gems가 매개변수로 주어집니다. 이때 모든 보석을 하나 이상 포함하는 가장 짧은 구간을 찾아서 return 하도록 solution 함수를 완성해주세요.
# 가장 짧은 구간의 시작 진열대 번호와 끝 진열대 
# 번호를 차례대로 배열에 담아서 return 하도록 하며, 만약 가장 짧은 구간이 
# 여러 개라면 시작 진열대 번호가 가장 작은 구간을 return 합니다.

# gems 배열의 크기는 1 이상 100,000 이하입니다.
# gems 배열의 각 원소는 진열대에 나열된 보석을 나타냅니다.
# gems 배열에는 1번 진열대부터 진열대 번호 순서대로 보석이름이 차례대로 저장되어 있습니다.
# gems 배열의 각 원소는 길이가 1 이상 10 이하인 알파벳 대문자로만 구성된 문자열입니다.

# 배열 크기 보니까 완전탐색은 안될거 같고...일단 각 보석을 어떻게 추릴지 생각해봐야겠어
# 1. 구매해야하는 보석을 추리기 -> 집합으로 만들면 될듯
# 2. 일단 풀셋 리스트 하나 만들기
# 3. 새로운 풀셋 하나 찾으면 인덱스 차이 비교해서 음...


# 배열 자체를 변경하는 것은 무리가 있을 거 같다.
# 투 포인터를 이용하는 문제임을 파악했다 -> 구현부터 먼저 해보자
def solution(gems):
    
    gems_set = set(gems)
    set_len = len(gems_set)

    start_p=0 # 시작 포인터 위치
    end_p = 0 # 끝 포인터 위치
    answer = [0,float('inf')]

    while end_p <= len(gems):
        # 매번 set을 해주면 너무 비효율적이라고 생각이 드는데 --> 고정된 값으로 가져가는건 어떨까? 아니면 이미 set 된 순간 플래그 올려서  더이상 set 연산 안하게 만들던가 --> 움직이면 변할 수도 있어 
        if set(gems[start_p:end_p+1]) == gems_set: # 일단 셋이면?
            if answer[1] - answer[0] > end_p-start_p:
                answer[1] = end_p
                answer[0] = start_p
            start_p += 1
        else:
            end_p += 1

    answer[0] += 1
    answer[1] += 1

    return answer

# 효율성 대 실패


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))