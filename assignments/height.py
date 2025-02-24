def solve():
    n = int(input())
    boys = sorted(list(map(int, input().split())))
    girls = sorted(list(map(int, input().split())))

    combined = []
    b_idx = 0
    g_idx = 0

    while b_idx < n or g_idx < n:
        if b_idx < n and (not combined or boys[b_idx] >= combined[-1]) and (not combined or combined[-1] not in boys):
            combined.append(boys[b_idx])
            b_idx += 1
            continue

        if g_idx < n and (not combined or girls[g_idx] >= combined[-1]) and (not combined or combined[-1] not in girls):
            combined.append(girls[g_idx])
            g_idx += 1
            continue

        print("NO")
        return

    for i in range(len(combined) - 1):
        if (combined[i] in boys and combined[i+1] in boys) or (combined[i] in girls and combined[i+1] in girls):
            print("NO")
            return

    print("YES")

t = int(input())
for _ in range(t):
    solve()