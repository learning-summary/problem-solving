# 인풋 처리
v, e = map(int, input().split())
edge = []
for _ in range(e):
    a, b, w = map(int, input().split())
    edge.append((a, b, w))
parent = [i for i in range(v + 1)]

# union-find
def find_root(x):
    global parent
    if parent[x] == x:
        return x
    return find_root(parent[x])

def union(a, b):
    global parent
    ra = find_root(a)
    rb = find_root(b)

    if ra < rb:
        parent[rb] = ra
    else:
        parent[ra] = rb

# kruskal
edge.sort(key=lambda x: x[2])
answer = 0
edge_cnt = 0

for a, b, w in edge:
    # 너무 많은 edge 선택 시, RecursionError 발생
    if edge_cnt > v - 1:
        break
    if find_root(a) != find_root(b):
        union(a, b)
        answer += w

print(answer)