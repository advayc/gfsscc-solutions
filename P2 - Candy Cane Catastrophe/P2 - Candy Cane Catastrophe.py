n = int(input())
counts = list(map(int, input().split()))
min_count = min(counts)
total_candy_canes = sum(counts)
print(total_candy_canes - min_count + 1)
