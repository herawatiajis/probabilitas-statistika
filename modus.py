data = [0,0,1,2,2,6,9]

counts = []
for i in data:
    counts.append(data.count(i))

max_count = max(counts)

mode = []
for i in data:
    if data.count(i) == max_count and i not in mode:
        mode.append(i)

if len(mode) == 1:
    print("Modus:", mode[0])
elif len(mode) > 1:
    print("Modus:", mode)
else:
    print("Tidak ada modus")








