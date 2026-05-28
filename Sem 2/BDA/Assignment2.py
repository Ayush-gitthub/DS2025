import csv

surname_fullname = {}  # s1 blocks
initial_fullname = {}  # s2 blocks
pairs = []

def get_s1_key(name):
    words = name.split()
    return words[-1] if words else None

def get_s2_key(name):
    words = name.split()
    if len(words) == 1:
        return words[0][0] + words[0][0]
    return words[0][0] + words[-1][0] if words else None

with open('dblp_names.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if len(row) >= 2:
            pairs.append((row[0], row[1]))
            for name in [row[0], row[1]]:
                k1 = get_s1_key(name)
                k2 = get_s2_key(name)
                surname_fullname.setdefault(k1, []).append(name)
                initial_fullname.setdefault(k2, []).append(name)

# Recall for s1
matches_s1 = sum(1 for o, n in pairs if get_s1_key(o) == get_s1_key(n))
Rec_s1 = matches_s1 / len(pairs)

# Recall for s2
matches_s2 = sum(1 for o, n in pairs if get_s2_key(o) == get_s2_key(n))
Rec_s2 = matches_s2 / len(pairs)

print(f"Rec s1: {Rec_s1:.4f}, Rec s2: {Rec_s2:.4f}")