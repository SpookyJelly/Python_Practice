# 2628번 (종이자르기)
"""

점선을 따라 이 종이를 칼로 자르려고 한다.
가로 점선을 따라 자르는 경우는 종이의 왼쪽 끝에서 오른쪽 끝까지,
세로 점선인 경우는 위쪽 끝에서 아래쪽 끝까지 한 번에 자른다.
예를 들어, <그림 1>의 가로 길이 10㎝이고 세로 길이 8㎝인 종이를 3번 가로 점선,
4번 세로 점선, 그리고 2번 가로 점선을 따라 자르면 <그림 2>와 같이 여러 개의 종이 조각으로 나뉘게 된다.
이때 가장 큰 종이 조각의 넓이는 30㎠이다.

입력으로 종이의 가로 세로 길이, 그리고 잘라야할 점선들이 주어질 때,
가장 큰 종이 조각의 넓이가 몇 ㎠인지를 구하는 프로그램을 작성하시오.

입력

첫줄에는 종이의 가로와 세로의 길이가 차례로 자연수로 주어진다.
가로와 세로의 길이는 최대 100㎝이다.
둘째 줄에는 칼로 잘라야하는 점선의 개수가 주어진다.
셋째 줄부터 마지막 줄까지 한 줄에 점선이 하나씩 아래와 같은 방법으로 입력된다.
가로로 자르는 점선은 0과 점선 번호가 차례로 주어지고,
세로로 자르는 점선은 1과 점선 번호가 주어진다.
입력되는 두 숫자 사이에는 빈 칸이 하나씩 있다.

첫째 줄에 가장 큰 종이 조각의 넓이를 출력한다. 단, 넓이의 단위는 출력하지 않는다.

"""

# 접근방법.
# 자르는 방법은 둘째 치더라도, 잘린 애들을 어떻게 처리할 것인가?
# 음..굳이 원본 가져갈 필요 없이, 가로길이, 세로 길이만 데이터화 해서 가지면 되지 않을까?
# 괜찮을지도? 가로 세로 길이를 매 시행마다 바꿔주고, 자른 데이터는 어딘가에 어펜드해서 보관하면 될 거 같다
# 전의 값도 가지고 있어야겠네, 한번 커트할때마다 사각형은 2개가 된다는 사실도 기억.
# 가로 : W , 세로 : H


def selectsort(lst):

    for i in range(len(lst)-1):
        min_idx = i
        for j in range(1+i,len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[min_idx],lst[i] = lst[i], lst[min_idx]
    return lst

# 리스트 정렬부터 해야겠다.
def maxilen(lst):
    maxi = 0
    hao =[]
    for idx in range(len(lst)-1):
        tem = lst[idx+1]-lst[idx]
        hao.append(tem)
    return max(hao)

# 결국 최대 값만 반환하면 되므로, 자른 지점을 기록 한 후, 그 기록으로부터 만들어지는 최대 거리를
# 높이와 거리 상으로만 구하면 됨
W, H = list(map(int,input().split()))
width = [W,0]
height = [H,0]

result = []  # 서걱베기의 희생자들의 수용소
TC = int(input())
for tc in range(TC):
    type, line = list(map(int,input().split()))
    if type: # 세로로 자르는 경우
        width.append(line)
    else: # 가로로 자르는 경우
        height.append(line)

width = selectsort(width)
height = selectsort(height)

print(maxilen(width)*maxilen(height))

