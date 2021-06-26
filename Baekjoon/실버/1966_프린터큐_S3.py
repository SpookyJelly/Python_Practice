#1966번
import sys
sys.stdin = open("1966_input.txt","r")

def resort(printer:list)->list:
    cnt = 0
    while True:
        max_priority = max(printer)[0]
        first = printer.pop(0)
        if first[0] != max_priority:
            printer.append(first)
        else: # first == max_priority 임
            cnt += 1
            if first[1] == "target":
                return cnt


TC = int(input())
# TC = 1
for _ in range(TC):
    N,M = map(int,input().split())
    
    # 숫자 리스트
    printer = list(map(int,input().split()))
    for idx in range(len(printer)):
        if idx == M:
            printer[idx] = (printer[idx],"target")
        else:
            printer[idx] = (printer[idx],"non-target")

    print(resort(printer))