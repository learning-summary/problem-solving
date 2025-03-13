def solution(arr):
    answer = 1
    n = len(arr)

    for i in range(n):
        for j in range(i, n):
            if arr[i][j] != arr[j][i]:
                answer = 0
                break

    return answer