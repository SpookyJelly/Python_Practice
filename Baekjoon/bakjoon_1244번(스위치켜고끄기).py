# 1244번 스위치 켜고 끄기

"""
1부터 연속적으로 번호가 붙어있는 스위치들이 있다.
스위치는 켜져 있거나 꺼져있는 상태이다.
<그림 1>에 스위치 8개의 상태가 표시되어 있다.
 ‘1’은 스위치가 켜져 있음을, ‘0’은 꺼져 있음을 나타낸다.
그리고 학생 몇 명을 뽑아서, 학생들에게 1 이상이고 스위치 개수 이하인 자연수를 하나씩 나누어주었다.
학생들은 자신의 성별과 받은 수에 따라 아래와 같은 방식으로 스위치를 조작하게 된다.


남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
즉, 스위치가 켜져 있으면 끄고, 꺼져 있으면 켠다. <그림 1>과 같은 상태에서 남학생이 3을 받았다면,
이 학생은 <그림 2>와 같이 3번, 6번 스위치의 상태를 바꾼다.

여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서
 가장 많은 스위치를 포함하는 구간을 찾아서,
그 구간에 속한 스위치의 상태를 모두 바꾼다.
 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.

입력으로 스위치들의 처음 상태가 주어지고, 각 학생의 성별과 받은 수가 주어진다.
학생들은 입력되는 순서대로 자기의 성별과 받은 수에 따라 스위치의 상태를 바꾸었을 때,
스위치들의 마지막 상태를 출력하는 프로그램을 작성하시오.

첫째 줄에는 스위치 개수가 주어진다. 스위치 개수는 100 이하인 양의 정수이다.
둘째 줄에는 각 스위치의 상태가 주어진다.
켜져 있으면 1, 꺼져있으면 0이라고 표시하고 사이에 빈칸이 하나씩 있다.
셋째 줄에는 학생수가 주어진다. 학생수는 100 이하인 양의 정수이다.
넷째 줄부터 마지막 줄까지 한 줄에 한 학생의 성별, 학생이 받은 수가 주어진다.
남학생은 1로, 여학생은 2로 표시하고, 학생이 받은 수는 스위치 개수 이하인 양의 정수이다.
학생의 성별과 받은 수 사이에 빈칸이 하나씩 있다.

출력 :

스위치의 상태를 1번 스위치서부터 마지막 스위치 까지 한 줄에 20개씩 출력

"""
# 접근방법, 여학생/ 남학생에 맞는 함수들을 만들어서 매 케이스에 적용

# 0 -> 1 1->0 전환
def tiktok(num):
    if num:
        num = 0
    else:
        num = 1
    return num

# 앞 뒤가 같으면 계속 리스트에 어펜드 시킨 후 쭉쭉 가져오기
def dawnbringer(lst,idx):
    lst[idx] = tiktok(lst[idx])
    i = 1
    # 만약에 switch의 0이 이상한 값이 아니였으면, 범위값이 좀 달라졌겠지
    while idx-i > 0 and idx+i < len(lst):
        # 인덱스 기준으로 좌우가 같으면 바꿔줌.
        # 언제까지? idx-i와 idx+i의 한계까지
        if lst[idx-i] == lst[idx+i]:
            lst[idx-i] = tiktok(lst[idx-i])
            lst[idx+i] = tiktok(lst[idx+i])

        else:
            break
        i += 1
    return lst




N = int(input())
#N = 8
# 스위치 시작 번호를 1번으로 맞추기 위해 임의의 문자열로 이루어진 리스트 추가
# 실제 switch의 길이는 N+1
switch =['null'] +list(map(int,input().split()))
#switch = ['null']+[0,1,0,1,0,0,0,1]
stu_Num = int(input())
#stu_Num = 2
#print(switch)
for i in range(stu_Num):
    t, card = map(int,input().split())
    # 남학생이라면,
    if t%2:
        for idx in range(1,len(switch)):
            if idx % card == 0:
                switch[idx] = tiktok(switch[idx])
        #print("남학생을 거쳤다.",switch)

    # 여학생이라면
    else:
        #for idx in range(1,len(switch)):
        switch = dawnbringer(switch,card)
        #print("여학생을 거쳤다",switch)

# 출력형식을 맞춰주기 위한 반복문.
ans = []
for k in range(1,len(switch)):
    ans.append(switch[k])
    if len(ans) == 20:
        print(*ans)
        ans = []
print(*ans)



###########테스트용 라인################

#print("최종 결과다.",switch)
#print("정답의 형상 :",*switch[1:])
#print(N)
#print(switch)
#print(switch[1])
#print(dawnbringer(switch,3))

# 0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1