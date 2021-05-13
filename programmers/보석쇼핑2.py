def solution(gems):
    
    gems_set = set(gems)
    set_len = len(gems_set)

    start_p=0 # 시작 포인터 위치
    end_p = len(gems)-1 # 끝 포인터 위치 인덱스
    answer = [0,0]

    # 끝,시작 인덱스 구하는 거
    def grinder(start,end,mode):
        if mode == 'e':
            while True:
                if set(gems[start:end+1]) == gems_set:
                    end -= 1
                else:
                    return end+1
        if mode == 's':
             while True:
                if set(gems[start:end+1]) == gems_set:
                    start+=1
                else:
                    return start-1          
            
    end = grinder(start_p, end_p, 'e')
    start = grinder(start_p, end, 's')

    answer[0] = start+1
    answer[1] = end+1

    return answer

gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))