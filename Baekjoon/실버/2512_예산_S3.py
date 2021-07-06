# 2512번
import sys
sys.stdin = open('2512_input.txt', 'r')
input = sys.stdin.readline

N = int(input())
desire_budget_lst = list(map(int, input().split()))
total_budget = int(input())

max_desire = max(desire_budget_lst)


def bin_search(start, end, total_budget):
    while start <= end:
        mid_v = (start+end) // 2
        result = do_satistfiy(mid_v, total_budget)
        # 가예산으로 전부 떡을 치면 --> 좀 더 올려보자
        if result:
            ans = mid_v
            start = mid_v + 1
        # 가예산 편성이 안되면 --> 좀 낮추자
        else:
            end = mid_v - 1
    return ans


def do_satistfiy(mid_v, total_budget):

    for budget in desire_budget_lst:
        total_budget -= mid_v if mid_v <= budget else budget

    # 가측정된 예산으로 모든 도시에 예산 할당이 가능하면 True 반환한다 --> 가측정 예산 키우자
    return True if total_budget >= 0 else False


print(bin_search(0, max_desire, total_budget))
