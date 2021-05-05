#1477 휴게소 세우기

# 입력
# 첫째 줄에 현재 휴게소의 개수 N, 더 지으려고 하는 휴게소의 개수 M, 고속도로의 길이 L이 주어진다. 
# N은 100보다 작거나 같으며, M도 100보다 작거나 같다. L은 100보다 크거나 같고, 1000보다 작거나 같은 정수이다. 
# 모든 휴게소의 위치는 중복되지 않으며, N+M은 L보다 작다. 둘째 줄에, 휴게소의 위치가 공백을 사이에 두고 주어진다.

# 출력
# 첫째 줄에 M개의 휴게소를 짓고 난 후에 휴게소가 없는 구간의 최댓값의 최솟값을 출력한다.


# N,M,L = map(int,input().split()) # N : 휴게소의 갯수 , M : 더 지으려고 하는 휴게소의 개수 , 고속도로의 길이 : L
N,M,L = 6,7,800
# rest_area = list(map(int,input().split()))
rest_area = [622,411,201,555,755,82]

rest_area.sort()

rest_area = [0]+rest_area+[L]

left = 1 # 초기 left 값
right = rest_area[-1] - rest_area[0]# 초기 right 값
result = 0
while left <= right:
    mid = (left+right) // 2
    ans = 0
    for idx in range(1,len(rest_area)):
        # 두 지점의 거리가 mid보다 더 커서 휴게소를 증설 할 수 있다.
        # 몇개 만큼? rest_area[idx]와 신설 휴게소의 거리가 mid가 될 만큼 !
        if rest_area[idx] - rest_area[idx-1] > mid:
            # 뺀 값에 왜 -1을 해주냐고? 휴게소가 설치된 곳에 또 설치 하지 않으려고 한다.
            # 즉, rest_area[idx] - rest_area[idx-1] 를 소숫점 단위로 만들라고 하는거
            ans += ((rest_area[idx]-rest_area[idx-1])-1) // mid

    # 더 지어야하는 휴게소 갯수보다 더 많이 지었다. --> 규제를 더 빡빡하게 한다 --> mid를 키워야한다 --> 작은 값인 left를 증가
    # 여기 있으면 현재 값보다 더 큰값만 보러간다 (최대값)
    if ans > M:
        left = mid + 1 # +1 해주는 이유 : 무한 루프를 막으려고


    # 더 지어야하는 휴게소 갯수보다 적게 지었다 --> 규제를 완화한다 --> mid를 줄인다 --> 큰 값인 right 감소
    else:
        right = mid - 1
        result = mid # 임시저장 (최소값)
# if에 넣어야하는지, else에 넣어야하는지 구분하는 방법:
# 정답과 일치하는 경우를 찾았을 때, 이번 케이스보다 더 작은놈을 찾아야하나? 큰놈을 찾아야하나 생각해보기
# 작은놈 찾아야하는 경우는 전체 범위가 좁아지는 right 감소 구역 / else 에 넣고
# 큰놈 찾아야하는 경우는 전체 범위가 넓어지는 left 증가 구역 / if에 넣어야한다.
print(result)

        