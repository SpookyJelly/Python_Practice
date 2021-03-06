#주식 가격

def solution(prices):
    answer = []
    while len(prices) > 1:
        a = prices.pop(0)
        cnt = 0
        for elem in prices:
            if a <= elem:
                cnt += 1
            else:
                cnt +=1
                break
        answer.append(cnt)
    return answer +[0]

# 큐를 이용하라고 하니까.. prices를 큐로 사용할지 아니면 다른 리스트를 만들어서 큐로 쓸지가 고민이다.
# 어? 맨 앞에꺼 뺀 다음에 그걸 a로 삼는다. for i in range(len(prices)) 대소 비교?
# 일단 만들어봤다 <-- 성공, 그러나 효율성 테스트 꽝


from collections import deque
def solution2(prices):
    prices = deque(prices)
    answer = deque()

    while len(prices) > 1:
        a = prices.popleft()
        cnt = 0
        for elem in prices:
            if a<=elem:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    return list(answer)+[0]

# dequeue로 만들어볼까? dequeue는 list의 .pop(0) 메소드의 느린 속도를 보완해줄것이라고 생각한다.
# 그냥 통과했다...헐.... dequeue는 .pop(0)과 동일한 기능을 하는 .popleft()가 O(1)의 시간 복잡도를 가진다고 함.
# (정확히 말하면 각 명령을 O(1)로 지원함)

def solution3(prices):
    prices = deque(prices)
    answer = deque()

    while prices:
        a = prices.popleft()
        cnt = 0
        for elem in prices:
            if a<=elem:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    return list(answer)
prices = [1,2,3,2,3]

# 이게 제일 낫다. solution2에서 종료조건을 while len(prices) > 1로 한 이유가
# 마지막 요소를 pop 할때 비교대상이 없어서 오류 날 것 같아서 그런것이다.
# 근데 생각해보니 pop 한 시점에서 prices는 텅 비어되어, for elem 문이 돌지 않게 된다.
# 그래서 바로 answer에 0이 append 된다.. 조금 더 컴퓨터적으로 생각하는 연습이 필요하다. 주의하자.

print(solution2(prices))
print(solution3(prices))


# 후기: 어렵지 않은 문제인데도 이 코드를 가지고 고민했던게, O(N^2) 이하의 시간 복잡도를 어떻게든 만들어볼라고 했었다.
# 그런데 풀이 후기를 보니 O(N^2) 미만으로 푼 사람은 없다고 한다.
# 애초에 O(N^2)에서 N을 최대한 줄이는것이 문제의 의도 인것 같다.
