def build_partial_match_table(pattern):
    table = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
        table[i] = j

    return table

def kmp_search(text, pattern):
    partial_match_table = build_partial_match_table(pattern)
    j = 0

    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = partial_match_table[j - 1]

        if text[i] == pattern[j]:
            j += 1

        if j == len(pattern):
            # Pattern found at position i - j + 1 in the text.
            print("Pattern found at index:", i - j + 1)
            j = partial_match_table[j - 1]

# Example usage
text = "ABABABABCABABABABCABABABABC"
pattern = "ABABABC"
kmp_search(text, pattern)
