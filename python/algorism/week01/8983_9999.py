"""
다른 사람들이 푼 문제중 bisect_rigth와 같은 형식이 있고, dict를 사용하여 dp를 사용했기에 가지고 왔다.
%로 overflow를 막을 수 있다.
"""

### 1
from bisect import bisect_right
import sys

input = sys.stdin.readline
m, n, l = map(int, input().split())
m_list = sorted(map(int, input().split()))

cnt = 0
for _ in range(n):
    x, y = map(int, input().split())
    i = bisect_right(m_list, x)
    cnt += l >= min(abs(m_list[(i - 1) % m] - x), abs(m_list[i % m] - x)) + y
print(cnt)

### 2
from bisect import bisect_right
import sys

input = sys.stdin.readline
m, n, l = map(int, input().split())
m_list = sorted(map(int, input().split()))
dp = dict()
cnt = 0
for _ in range(n):
    x, y = map(int, input().split())
    if x not in dp:
        i = bisect_right(m_list, x)
        dp[x] = min(abs(m_list[(i - 1) % m] - x), abs(m_list[i % m] - x))
    cnt += l >= dp[x] + y
print(cnt)
