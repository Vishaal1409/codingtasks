import time
def build_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps
def kmp_search(text, pattern):
    lps = build_lps(pattern)
    i = j = 0
    comparisons = 0
    matches = []
    while i < len(text):
        comparisons += 1
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                matches.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return matches, comparisons
def naive_search(text, pattern):
    comparisons = 0
    matches = []
    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
        else:
            matches.append(i)
    return matches, comparisons
if __name__ == "__main__":
    text = "CATSABCBCABCDOGSABCBCABC"
    pattern = "ABCBCABC"
    start = time.time()
    kmp_matches, kmp_comp = kmp_search(text, pattern)
    kmp_time = time.time() - start
    start = time.time()
    naive_matches, naive_comp = naive_search(text, pattern)
    naive_time = time.time() - start
    print("\nKMP Algorithm:")
    print("Matches found at:", kmp_matches)
    print("Comparisons:", kmp_comp)
    print("Time Taken: {:.6f} seconds".format(kmp_time))
    print("\nNaive Algorithm:")
    print("Matches found at:", naive_matches)
    print("Comparisons:", naive_comp)
    print("Time Taken: {:.6f} seconds".format(naive_time))