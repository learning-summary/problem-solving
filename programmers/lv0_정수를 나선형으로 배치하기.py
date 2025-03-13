def solution(n):
    answer = [[0] * n for _ in range(n)]
    # 오른쪽, 아래, 왼쪽, 위
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    y, x = 0, -1
    cnt, dir = 1, 0

    while cnt <= n ** 2:
        ny, nx = y + dy[dir], x + dx[dir]

        if 0 <= ny < n and 0 <= nx < n and not answer[ny][nx]:
            answer[ny][nx] = cnt
            cnt += 1
            y, x = ny, nx
        else:
            dir = (dir + 1) % 4

    return answer

#     answer = [[0 for _ in range(n)] for _ in range(n)]
#     i = 0
#     val = 1

#     while i < n - i:
#         # right
#         for j in range(i, n - i):
#             answer[i][j] = val
#             val += 1
#         # down
#         for j in range(i + 1, n - i):
#             answer[j][-1 - i] = val
#             val += 1
#         # left
#         for j in range(n - i - 2, i - 1, -1):
#             answer[n - i - 1][j] = val
#             val += 1
#         # up
#         for j in range(n - i - 2, i, -1):
#             answer[j][i] = val
#             val += 1
#         i += 1

#     return answer