# 10828번 스택

"""

정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

"""
# 아 이거 시간 문제가 아니라 123처럼 여러가릿수 들어오는 경우도 있구나 , push에 <-- 이거 수정하자.
import sys
from collections import deque

sys.stdin = open('10828_input.txt', 'r')
input=sys.stdin.readline

def push(num: str, stack: list) -> list:
    # 이상하게 stack.append 하면 None type이 return 된다??
    stack.append(int(num))
    return stack


def pop(stack: list) -> int:
    if stack:
        return stack.pop()
    else:
        return -1

def top(stack: list) -> int:
    if stack:
        return int(stack[-1])
    else:
        return -1



def empty(stack:list) -> int:
    if stack:
        return 0
    else:
        return 1


def size(stack:list) -> int:
    return len(stack)



TC = int(input())
stack = deque()
for tc in range(TC):
    order = input().strip()

    if 'push' in order:
        p, num = order.split()
        stack = push(num, stack)
    elif order == 'top':
        print(top(stack))
    elif order == 'size':
        print(size(stack))
    elif order == 'pop':
        print(pop(stack))
    elif order == 'empty':
        print(empty(stack))

# 흠 시간 초과?
# input=sys.stdin.readline 으로 시간 줄여봤다.
# #주의할 점은 숫자가 아닌 문자열로 입력을 받는 경우엔 줄바꿈(\n)까지 입력으로 받으니 input().strip() 을 사용하거나 input().strip().split() 을 사용하시는게 좋습니다.
# 아니 진짜네....놀랍다...그냥 입력 ㅏㅌ입만 바꿨는데