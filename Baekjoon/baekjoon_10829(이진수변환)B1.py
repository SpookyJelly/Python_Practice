#10829번 이진수 변환

"""

자연수 N이 주어진다. N을 이진수로 바꿔서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 100,000,000,000,000)

출력
N을 이진수로 바꿔서 출력한다. 이진수는 0으로 시작하면 안 된다.

"""

def binary(num):
# q = 몫, r = 나머지
     q,r= divmod(num,2)

     if q == 1:
         return str(q) + str(r)

     return binary(q)+str(r)


# print(binary(8))
# print(binary(53))
print(binary(int(input())))