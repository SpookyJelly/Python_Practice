# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로b
import sys
sys.stdin =open('1181_input.txt','r')

N = int(input())

words = []
for _ in range(N):
    words.append(input())


words = list(set(words))

# 길이 순 정렬 / 2순위 : 사전 순 정렬
words = sorted(words,key= lambda x : [len(x),x]) 


for word in words:
    print(word)