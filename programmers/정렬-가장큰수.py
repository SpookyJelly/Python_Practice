# 가장 큰 수
"""
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항

numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.


"""


def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers)) # list를 취해주는 이유 : sort 메서드는 map object에 사용할 수 가 없어서.
    # 정렬 힌트 : x*3를 해주어 반복된 문자열로 만든 고단위 수를 만들었다.
    # 이렇게 할 경우, 3 -> 3333 30 -> 3030이 되어, 목적에 맞게정렬을 할 수 있었다.
    #[9,5,34,3,30] --> 9534303
                #      9534330
    # [999,555,343434,333,303030]
    # [9,5,34,3,30]
    numbers.sort(key=lambda x: x*3, reverse=True) # 최초 코드 : lambda x : x[0:]

    for elem in numbers:
        answer += elem

    return str(int(answer)) # 0000의 경우를 제거하기 위해서 정수로 변환후 다시 문자로 출력 -> 0


# arr = ['9', '93', '92', '2']
#
# arr.sort(key=lambda x: (x[0:]), reverse=True)
#
# print(arr)
# num = [3,30,34,5,9]
num = [0,0,0,0,0]
print(solution(num))