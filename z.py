import sys

def print_alignment_matrix(seq_a, seq_b):
    print('  ' + ' '.join(seq_b))

    for char_a in seq_a:
        row = []
        for char_b in seq_b:
            if char_a == char_b:
                row.append('1')
            else:
                row.append('0')
        print(char_a, ' '.join(row))

# find the longest common prefix of seq and the suffix of seq starting at i
def z_naive(seq, i):
    k = 0
    while i + k <= len(seq) and seq[i + k] == seq[k]:
        k += 1
    return k

args = sys.argv[1:]

print_matrix = '--print-matrix' in args
if print_matrix:
    args.remove('--print-matrix')

if len(args) != 2:
    print(f"Usage: z.py [--print-matrix] <query_string> <search_string>\n"
          f"\nexample:\n z.py ACTG TTGATCACTGCCGAT" )
    sys.exit(1)

query, search = args

concat_string = query + '$' + search

# print self-alignment matrix of the concatenated query+reference
if print_matrix:
    print_alignment_matrix(concat_string, concat_string)

# z_array[0] is a placeholder so that z_array[i] is the Z value at position i
z_array = [0]
for i in range(1, len(concat_string)):
    z_array.append(z_naive(concat_string, i))

# position i in concat_string is position i - len(query) - 1 in search
match_found = False
for i, score in enumerate(z_array):
    if score == len(query):
        print(f"Exact match found at index {i - len(query) - 1}")
        match_found = True

if not match_found:
    print("No matches found!")
