N = int(input())
protein = [250, 40, 10]
protein_cnt = [0, 0, 0]
# 땅콩 큐브 10
# 닭가슴살 40
# 순수한 단백질 큐브 250


for i in range(len(protein)):
    while N >= protein[i]:
        N -= protein[i]
        protein_cnt[i] += 1

if N:
    print(-1)
else:
    print('{} {} {}'.format(protein_cnt[2], protein_cnt[1], protein_cnt[0]))