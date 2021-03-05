def solution(board, moves):
    answer = 0
    stack = []

    # moves의 element를 임시변수로 삼아 반복한다
    for move in moves:

        i = 0
        # i == depth <-- while문 조건에 부합한다면 한단계씩 깊은 곳을 탐색한다.
        # board[i][move-1]이 0이면 i를 증가시킴으로서, 0이 나오지 않을때까지 반복한다
        while 0 <= i < len(board) - 1 and board[i][move - 1] == 0:
            i += 1

        # 그럼 while문을 탈출하였을때, board[i][move-1]은 0이 아닌 값이 들어있을것이다.
        # 이걸 잡아주고, 그 자리를 0으로 바꿔주자
        pick = board[i][move - 1]
        board[i][move - 1] = 0

        # 하지만, 0 ~ len(board)-1 까지 증가하는 i의 특성상, pick = 0이 되는 경우가 있다.
        # 그렇게 된다면 코드가 설계 의도와 다르게 작동하므로 (비어있음을 뜻하는 0 이 스택에 들어가게 됨)
        # pick이 0이 아닌 값일 때만, 스택에 넣고 제거하는 과정을 겪게 한다.
        if pick:
        # 스택이 0보다 크고, pick이 0이 아니면서, stack의 top이 pick 과 같으면, 크레인 게임의 조건을 만족한다.
            if len(stack) > 0 and pick and stack[-1] == pick:
                stack.pop()
                answer += 2

            # 반면, 스택이 0이거나, pick이 0이 아니면서, stack의 top이 pick과 다르면 그대로 스택에 넣어준다.
            else:
                stack.append(pick)

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board,moves))