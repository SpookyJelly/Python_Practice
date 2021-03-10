#2920번 음계(B2)

"""

문제
다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. c는 1로, d는 2로, ..., C를 8로 바꾼다.

1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.

연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.

입력
첫째 줄에 8개 숫자가 주어진다. 이 숫자는 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.

출력
첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.


"""

# 아니....문제 조건 생각해보면 ascending이랑 desceding 조건이 이거 밖에 없다... 나머지는 다 else 처리하면 되나?
music_lst = list(map(int,input().split()))
ascending = [1,2,3,4,5,6,7,8]
descending = [8,7,6,5,4,3,2,1]

if music_lst == ascending:
    print('ascending')
elif music_lst == descending:
    print('descending')
else:
    print('mixed')

    # ??? 진짜라고?
