from collections import deque

antrian = deque([1,2,3,4,5])

print("data sekarang", antrian)

antrian.append(6)
print("data masuk ", 6)
print("data sekarang", antrian)

out = antrian.popleft()
print("data keluar", out)
print("Data sekarang", antrian)
