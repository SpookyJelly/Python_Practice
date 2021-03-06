# 2605번 줄세우기
"""
학생들이 한 줄로 줄을 선 후, 첫 번째 학생부터 차례로 번호를 뽑는다.
첫 번째로 줄을 선 학생은 무조건 0번 번호를 받아 제일 앞에 줄을 선다.
두 번째로 줄을 선 학생은 0번 또는 1번 둘 중 하나의 번호를 뽑는다.
0번을 뽑으면 그 자리에 그대로 있고, 1번을 뽑으면 바로 앞의 학생 앞으로 가서 줄을 선다.
 세 번째로 줄을 선 학생은 0, 1 또는 2 중 하나의 번호를 뽑는다.
그리고 뽑은 번호만큼 앞자리로 가서 줄을 선다.
마지막에 줄을 선 학생까지 이와 같은 방식으로 뽑은 번호만큼 앞으로 가서 줄을 서게 된다.
각자 뽑은 번호는 자신이 처음에 선 순서보다는 작은 수이다.
예를 들어 5명의 학생이 줄을 서고,
첫 번째로 줄을 선 학생부터
 다섯 번째로 줄을 선 학생까지 차례로 0, 1, 1, 3, 2번의 번호를 뽑았다고 하자,
첫 번째 학생부터 다섯 번째 학생까지 1부터 5로 표시하면 학생들이 줄을 선 순서는 다음과 같이 된다.

첫 번째 학생이 번호를 뽑은 후 : 1
두 번째 학생이 번호를 뽑은 후 : 2 1
세 번째 학생이 번호를 뽑은 후 : 2 3 1
네 번째 학생이 번호를 뽑은 후 : 4 2 3 1
다섯 번째 학생이 번호를 뽑은 후 : 4 2 5 3 1
따라서 최종적으로 학생들이 줄을 선 순서는 4, 2, 5, 3, 1이 된다.

줄을 선 학생들이 차례로 뽑은 번호가 주어질 때 학생들이 최종적으로 줄을 선 순서를 출력하는 프로그램을 작성하시오.

"""

# 그러니까 뽑은 숫자만큼 앞으로 이동하는 방식.
# 학생들은 문자타입이 되야할듯. '1' ~ '5'
# 자신들이 뽑는 숫자는 으음....range(5)내에서 차례로 뽑으면 되겠지? 인덱스 매칭 시키면 되겠다.
# 앞으로 가는것은 위치교환하면...또 바뀌는구나. insert 써야겠네.

# 으음...근데 처음 리스트를 어떻게 설정할까? 빈 리스트? 아니면 미리 채워놓아야하나??

# 학생의 수 100 이하,... 앞으로 n 칸 간다 --> 앞에 새끼랑 n회 자리 바꾼다.
# 처음에 학생들 하나씩 빈리스트에 집어넣는다 -> 이후에 for문으로 n회 자리 바꾸는 거 시행시킴 (n은 카드에서 뽑은 수)

# 필요 변수 : 빈 리스트, 학생들의 수 int --> 1,N+1 list로 바꾼 후 str 처리


def bubble(lst, K)->list:
    # 마지막 리터럴을 K회 위치바꾸기.
    N = len(lst)
    for i in range(K):
        if i < N-1:
            lst[N-1-i], lst[N-2-i] = lst[N-2-i], lst[N-1-i]
    return lst


M = int(input())

student_lst = list(map(str, range(1, M+1)))
queue = []
draw_lst = list(map(int, input().split()))

for idx in range(M):
    # 이어붙일때는 자료형 통일해라, 너무 인터프리터 믿지말고.
    queue += [student_lst[idx]]
    ans = bubble(queue, draw_lst[idx])
print(*ans)


