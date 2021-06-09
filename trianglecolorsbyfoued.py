
a = [[[0, 0], [0.5, -1], [0.3, 0]], [[0.3, 0], [0.5, -1], [1.5, 1]], [[0.5, -1],
[1.5, -0.2], [1.5, 1]], [[1.5, -0.2], [2, -0.5], [1.5, 1]], [[2, -0.5], [2, 0],
[1.5, 1]], [[0.3, 0], [0.5, 1], [0, 0]]]


l0=a[0]
dic={'R':[l0[0]],'G':[l0[1]],'B':[l0[2]]}
add = list(map(lambda x:x, l0))
flag = set()
for arr in range(1,len(a)):
    for subarr in a[arr]:
        for k,v in dic.items():
            if subarr in v:
                flag.add(k)
    for subarr in a[arr]:
        if subarr in add:
            continue
        else:
            if subarr not in dic['G'] and 'G' not in flag:
                add.append(subarr)
                dic['G'].append(subarr)
                flag.add('G')
            elif subarr not in dic['R'] and 'R' not in flag:
                add.append(subarr)
                dic['R'].append(subarr)
                flag.add('R')
            elif subarr not in dic['B'] and 'B' not in flag:
                add.append(subarr)
                dic['B'].append(subarr)
                flag.add('B')
    if len(flag) >= 3:
        flag=set()
color=[]
for arr in a:
    line=[]
    for subarr in arr:
        for k,v in dic.items():
            if subarr in v:
                line.append(k)
    color.append(line)
print(dic)
print(add)
print()
c = 0
for i in a:
    
    print(c, i, color[c])
    c += 1
