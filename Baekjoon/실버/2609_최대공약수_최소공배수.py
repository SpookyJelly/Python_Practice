#2609번
# 두개의 자연수를 입력받아 최대공약수와 최소 공배수를 출력하는 프로그램 작성

def aliquot_maker(num:int)->set:
    aliquot = []
    for idx in range(1,num+1):
        if num % idx == 0 :
            aliquot.append(idx)
    return set(aliquot)

num1 ,num2 = map(int,input().split())
aliquot_set1 = aliquot_maker(num1)
aliquot_set2 = aliquot_maker(num2)

a = aliquot_set1.intersection(aliquot_set2)

ans = max(list(a))
print(ans)
print(ans*(num1//ans)*(num2//ans))