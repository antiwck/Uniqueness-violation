from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    u=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    dict = defaultdict(list)
    ctr=0
    for i in u:
        dict[i].append(a[ctr])
        ctr+=1
    total = 0
    for i in dict:
        total += max(dict[i])
    print(total)
