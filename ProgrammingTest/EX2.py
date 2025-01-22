# Function complexisy is O(N), assuming dict operations are O(1).
def sol(word: str) -> str:
    uniques = {}
    counts = []
    chars = []

    for x in word:
        if (uniques.get(x) is not None):
            tmp_index = uniques[x]
            counts[tmp_index] += 1
        else:
            uniques[x] = len(counts)
            counts.append(1)
            chars.append(x)

    for i in range(0,len(counts)):
        if (counts[i] == 1):
            return chars[i]
        

inputs = [
    "abcdefg",
    "aabbccddff",
    "a124a12$a124",
    "tahetahe5ehat",
    "!@#$%^&*()_+=-0987543211!@#$%^^&*(0)",
]

for x in inputs:
    print(x, sol(x))