# 주식 가격

"""

초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.

"""

# 기본 아이디어 -> index를 반복해서 현재 내 위치보다 작은 값을 반복해서 찾은 다음, 그 위치의 차이가 곧 정답이라고 생각함
# 근데 접근하다보니까, pop도 필요하고, for문도 여러개 필요하고 그런다.

def solution(prices):
    answer = []
    prices = prices + [0]

    for idx in range(len(prices)):
        for i in range(1,prices[idx]+1):
            try:
                a = prices.index(prices[idx]-i) # 문제가 있다. price[idx] 다음에서부터 찾는게 아니라 price의 처음부터 찾아버리는 바람에... 좋지 않다
                if a >= 0:
                    a = a-idx
                    # prices.pop(0)
                    break
            except:
                a = len(prices) - idx
                # prices.pop(0)

        answer.append(a)


    return answer




prices = [1,2,3,2,3]

print(solution(prices))

# 다시 접근해야겠다. .index()도, .pop(0)도 모두 O(N) 복잡도이다. -> pop 쓰면 리스트 전체가 또 변경되서 for문 에러 -> while로 변경?