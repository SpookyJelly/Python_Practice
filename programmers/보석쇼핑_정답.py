def solution(gems):
    size = len(set(gems))
    dic = {gems[0]:1}
    temp = [0,len(gems)-1]
    start=end=0

    while (start<len(gems) and end < len(gems)):
        if len(dic) == size:
            if end-start < temp[1] - temp[0]:
                temp = [start,end]


            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1

        else:
            end+=1
            if end == len(gems):
                break

            dic[gems[end]] = dic.get(gems[end],0) + 1 # 아래 주석이랑 동일한 코드

            
            # if gems[end] in dic.keys():
            #     dic[gems[end]] += 1
            # else:
            #     dic[gems[end]] = 1

    return [temp[0]+1, temp[1]+1]


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))