import sys
from heapq import heappush, heappop

INF = sys.maxsize  # 2_147_483_647 = 2^31

# 인풋 처리
input = sys.stdin.readline
v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))


# 최단경로 알고리즘 선언
def dijkstra(start, graph):
    distance = [INF] * (v + 1)
    q = []
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heappop(q)

        # start부터 now까지의 거리가 기존이 더 가까운 경우
        if distance[now] < dist:
            continue

        # start부터 now까지가 더 가까워졌으므로 인접 node까지의 거리 갱신
        for node, w in graph[now]:
            cost = dist + w
            if distance[node] > cost:
                distance[node] = cost
                heappush(q, (cost, node))

    return distance


# 문제 풀이
dist = dijkstra(start, graph)

# 거리 출력
for i in range(1, v + 1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])