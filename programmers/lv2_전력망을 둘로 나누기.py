def dfs(start, g, n):
    result = 0
    stack = []
    visited = [False] * (n + 1)
    stack.append(start)
    visited[start] = True

    while stack:
        now = stack.pop()
        result += 1

        for i in g[now]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True

    return result


def solution(n, wires):
    answer = n

    # ADJ list 생성
    g = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        g[v1].append(v2)
        g[v2].append(v1)

    # wire 하나씩 자르기
    for v1, v2 in wires:
        g[v1].remove(v2)
        g[v2].remove(v1)

        # 2개의 네트워크별 송전망 개수 구하기
        n1, n2 = dfs(v1, g, n), dfs(v2, g, n)
        answer = min(answer, abs(n1 - n2))

        # 다음 탐색을 위해 graph 복구
        g[v1].append(v2)
        g[v2].append(v1)

    return answer