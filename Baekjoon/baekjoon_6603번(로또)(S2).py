# 로또 (S2) 재귀

"""
독일 로또는 {1, 2, ..., 49}에서 수 6개를 고른다.
로또 번호를 선택하는데 사용되는 가장 유명한 전략은 49가지 수 중 k(k>6)개의 수를 골라
집합 S를 만든 다음 그 수만 가지고 번호를 선택하는 것이다.

예를 들어, k=8, S={1,2,3,5,8,13,21,34}인 경우
이 집합 S에서 수를 고를 수 있는 경우의 수는 총 28가지이다.
([1,2,3,5,8,13], [1,2,3,5,8,21], [1,2,3,5,8,34], [1,2,3,5,13,21], ..., [3,5,8,13,21,34])

집합 S와 k가 주어졌을 때, 수를 고르는 모든 방법을 구하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있다.
 첫 번째 수는 k (6 < k < 13)이고,
 다음 k개 수는 집합 S에 포함되는 수이다. S의 원소는 오름차순으로 주어진다.

입력의 마지막 줄에는 0이 하나 주어진다.

각 테스트 케이스마다 수를 고르는 모든 방법을 출력한다. 이때, 사전 순으로 출력한다.

각 테스트 케이스 사이에는 빈 줄을 하나 출력한다.

"""
# 숫자를 고르는 것시니까, 순열이 아닌 조합이 필요.
import sys
sys.stdin = open('6603_input.txt','r')

# 근데 조합을 만드는걸 잘 못해서, 순열을 만든다음, 중복을 제거하는 방식으로 했다. --> 당연히 시간초과가 났다.
def perm(L):

    if L == 6:
        a = sorted(result)
        if a not in all:
            all.append(a)
        return

    for i in range(len(sample)):
        v = visited
        r = result
        s = sample
        if not visited[i]:
            visited[i] = 1
            result[L] = sample[i]
            ########전처리 끗
            perm(L+1)
            ####### 후처리
            visited[i] =0

# 조합을 만드는 함수
def comp(L):

    if L == 6:
        a = sorted(result)
        if a not in all:
            all.append(a)
        return
    for i in range(len(sample)):
        if not sample[i] in result: #and not visited[i]: # 조건 하나 더 추가하니까 되었다. sample[i] 즉 요소 하나가 이미, result에 있다면, depth를 확장하지 않는것이다.
            # 아니, 이런...아예 방문처리를 하지 않아도 된다... 이번에 할당할 요소가 이미 result 안에 있는지 확인하는거 자체가 이미
            # 방문 처리와 동일하다.
            # visited[i] = 1
            result[L] = sample[i]
            ########전처리 끗
            comp(L+1)
            ####### 후처리
            # visited[i] =0
# 그냥 순열
def perm2(L):
    if L == 6:
        all2.append(result[:])
        return

    for i in range(len(sample)):
        if not visited[i]:
            visited[i] = 1
            result[L] = sample[i]
            #####전처리
            perm2(L+1)
            ######후처리

            visited[i] = 0



while True:


    s_lst = list(map(int,input().split()))
    if s_lst == [0]:
        break

    k = s_lst[0] # 골라야 할 숫자의 갯수
    sample = s_lst[1:] # 숫자들의 리스트

    visited = [0] * len(sample) # 방문 여부를 테스트할 리스트 <-- 이건 순열에서나 필요하지, 조합에서는 필요가 없다...
    result = [0] * 6 # 순열/ 조합 이 될 리스트
    all = [] # 조합이 저장되어 있는 리스트
    all2 = [] # 순열이 저장되어 있는 리스트
    comp(0) # < -주어진 sample에 대하여 조합을 만드는 재귀함수
    perm2(0) # <- 주어진 sample에 대해 순열을 만드는 재귀함수
    # perm(0) <-- 순열을 만든다음, 중복제거를 사용하여 만든 조합 ( 가장 느리고, 비효율적)

    print('조합입니다')
    for idx in range(len(all)):
        print(*all[idx])
    print()

    print('순열입니다')
    for idx in range(len(all2)):
        print(*all2[idx])
    print()
