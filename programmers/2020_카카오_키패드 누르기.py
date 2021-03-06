def solution(numbers, hand):
    answer = ''
    numbers = list(map(str,numbers))

    left_hand = [3,0] # 왼손 포인터 위치
    right_hand = [3,2] # 오른손 포인터 위치

    keypad_dic = {
        '1': [0, 0], '2': [0, 1], '3': [0, 2],
        '4': [1, 0], '5': [1, 1], '6': [1, 2],
        '7': [2, 0], '8': [2, 1], '9': [2, 2],
        '*': [3, 0], '0': [3, 1], '#': [3, 2],

    }
    # keypad_dic[elem] = 입력값의 포인터 위치

    for elem in numbers:

        if elem == '1' or elem == '4' or elem == '7':
            answer += 'L'
            left_hand = keypad_dic[elem]

        elif elem == '3' or elem == '6' or elem == '9':
            answer += 'R'
            right_hand = keypad_dic[elem]

        else: # 입력값 2,5,8,0
            left_dis = abs(left_hand[0]-keypad_dic[elem][0]) + abs(left_hand[1] - keypad_dic[elem][1])
            right_dis = abs(right_hand[0]-keypad_dic[elem][0]) + abs(right_hand[1] - keypad_dic[elem][1])

            if left_dis < right_dis: # 왼손의 거리가 오른손보다 가까울때
                answer += 'L'
                left_hand = keypad_dic[elem]
            elif left_dis > right_dis: # 오른손의 거리가 왼손보다 가까울때
                answer += 'R'
                right_hand = keypad_dic[elem]
            else: # 두 손의 거리가 같을 때
                if hand == 'left':
                    answer += 'L'
                    left_hand = keypad_dic[elem]
                else:
                    answer += 'R'
                    right_hand = keypad_dic[elem]

    return answer

# 접근방법
# 키패드의 위치를 index화 시킨다
# 왼손의 위치, 오른손의 위치를 포인터로 만든다.
# 각 포인터의 위치와 입력 키패드의 위치를 인덱스 비교해서 더 작은 값을 출력하게 한다.

numbers2 = [1,3,4,5,8,2,1,4,5,9]
hand2 = 'right'

print(solution(numbers2,hand2))

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = 'left'

print(solution(numbers,hand))


numbers3 = [1,2,3,4,5,6,7,8,9,0]
hand3 = 'right'

print(solution(numbers3,hand3))
