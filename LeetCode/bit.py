N = 4
visited = [[ 0 for j in range(1<<N)] for i in range(N)]
print(visited)

for i in range(1<<N):
    print(i)

for i in range(N):
    print(1<<i)

print(2 | 1)