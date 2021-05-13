#메뉴 리뉴얼

# 기존에는 단품으로만 제공하던 메뉴를 조합해서 
# 코스요리 형태로 재구성해서 새로운 메뉴를 제공하기로 결정했습니다. 
# 어떤 단품메뉴들을 조합해서 코스요리 메뉴로 구성하면 좋을 지 고민하던 
# "스카피"는 이전에 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 
# 코스요리 메뉴로 구성하기로 했습니다.
# 단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하려고 합니다.
# 또한, 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만
# 코스요리 메뉴 후보에 포함하기로 했습니다.

# [문제]
# 각 손님들이 주문한 
# 단품메뉴들이 문자열 형식으로 담긴 배열 orders, 
# "스카피"가 추가하고 싶어하는 코스요리를 구성하는 
# 단품메뉴들의 갯수가 담긴 배열 course가 매개변수로 주어질 때, 
# "스카피"가 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로 
# 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

# [제한사항]
# orders 배열의 크기는 2 이상 20 이하입니다.
# orders 배열의 각 원소는 크기가 2 이상 10 이하인 문자열입니다.
# 각 문자열은 알파벳 대문자로만 이루어져 있습니다.
# 각 문자열에는 같은 알파벳이 중복해서 들어있지 않습니다.
# course 배열의 크기는 1 이상 10 이하입니다.
# course 배열의 각 원소는 2 이상 10 이하인 자연수가
# 오름차순으로 정렬되어 있습니다.
# course 배열에는 같은 값이 중복해서 들어있지 않습니다.
# 정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아
# 전 순으로 오름차순 정렬해서 return 해주세요.
# 배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬되어야 합니다.
# 만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면,
# 모두 배열에 담아 return 하면 됩니다.
# orders와 course 매개변수는 return 하는 배열의
# 길이가 1 이상이 되도록 주어집니다.


# 기본 아이디어 : 가장 많이 등장한 메뉴 추린 다음에, course 갯수 만큼 조합 구현?
from itertools import combinations

def solution(orders, course):

    ordered = {}

    for order in orders:
        for menu in order:
            ordered[menu] = ordered.get(menu,1) +1
    print(ordered)

    ordered_lst = list((ordered.items()))
    print(ordered_lst)
    print(sorted(ordered_lst,key=lambda x : (-x[1],x[0])))




    answer = []


    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))