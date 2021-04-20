#1918번 후위 표기식

# 입력
#
# 첫째 줄에 중위 표기식이 주어진다. 단 이 수식의 피연산자는 A~Z의 문자로 이루어지며 수식에서 한 번씩만 등장한다.
# 그리고 -A+B와 같이 -가 가장 앞에 오거나 AB와 같이 *가 생략되는 등의 수식은 주어지지 않는다. 표기식은 알파벳 대문자와 +, -, *, /, (, )로만 이루어져 있으며, 길이는 100을 넘지 않는다.
#
# 출력
#
# 첫째 줄에 후위 표기식으로 바뀐 식을 출력하시오
# 핵심은 완전히 찍어누를수 있을때만 그냥 스택에 append.. 우선순위가 같아도 끄집어내야한다.

lst = list(input())
# 출력용 리스트 / 연산자용 스택
postfix = []
stack = []

out_dict ={
    '(':3,
    '+':1,
    '-':1,
    '*':2,
    '/':2,
}
in_dict ={
    '(':0,
    '+':1,
    '-':1,
    '*':2,
    '/':2,
}


for elem in lst:
    if elem.isalpha():
        postfix.append(elem)
    elif elem == ')':
        while stack[-1] != '(':
            postfix.append(stack.pop())
        stack.pop()
    else:
        while stack and out_dict[elem]<=in_dict[stack[-1]]:
            postfix.append(stack.pop())
        stack.append(elem)


while stack:
    postfix.append(stack.pop())

print(''.join(postfix))

