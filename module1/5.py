def build_lps(pattern):
    """Build the LPS (Longest Prefix Suffix) table."""
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
if __name__ == "__main__":
    pattern = "ABCBCABC"
    lps = build_lps(pattern)
    print("Pattern:", pattern)
    print("LPS Table:", lps)