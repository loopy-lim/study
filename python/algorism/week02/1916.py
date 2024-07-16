import heapq

N = int(input())
M = int(input())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((c, b))
start, end = map(int, input().split())


q = []
board = [float("inf") for _ in range(N + 1)]
board[start] = 0
heapq.heappush(q, (0, start))

while q:
    val, cur = heapq.heappop(q)
    if val > board[cur]:
        continue
    for next_val, next in arr[cur]:
        sum_val = val + next_val
        if sum_val >= board[next]:
            continue

        board[next] = sum_val
        heapq.heappush(q, (sum_val, next))
    # print(q, board)


print(board[end])
