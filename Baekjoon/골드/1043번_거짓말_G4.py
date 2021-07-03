# 1043번 거짓말 : https://www.acmicpc.net/problem/1043

# 기본 아이디어 : 파티 한번 참석할때마다, 남은 모든 파티를 봐서, 지금 진실을 알게 될 사람이 이 자리에 있는지를 확인
# 1. 입력 받는다
# 2. 진실 알고 있는 사람을 집합으로 만듬
# 3. 파티를 순회하면서, 지금 파티에 진실을 아는 사람이 있는지 확인
# 3.1 있다면, 해당 파티를 진실 파티로 마크, 그리고 진실을 아는 사람 set 업데이트
# 3.2 없다면 일단 계속 순회
# 4. 순회가 종료되었을때, 진실 파티의 갯수 파악해서, 구라 파티가 몇개인지 확인한다.

# N,M 모두가 50 이하이므로 복잡도 계산 안해도 된다.

import sys
sys.stdin = open('1043_input.txt','r')
input = sys.stdin.readline

# N : 사람의 수 ,  M : 파티의 수
N, M = map(int,input().split())
know_truth = set(list(map(int,input().split()))[1:])


parties = []
for _ in range(M):
    party_member = list(map(int,input().split()))[1:]
    parties.append(party_member)

truth_party = [0] * M


for _ in range(M): # 파티 수만큼 반복해라.
    for idx, party in enumerate(parties):
        if know_truth.intersection(set(party)):
            # 여기는 이제 진실을 아는 사람들이 있는 파티니까...표시해야겠지
            truth_party[idx] = 1
            know_truth = know_truth.union(set(party))

print(truth_party.count(0))