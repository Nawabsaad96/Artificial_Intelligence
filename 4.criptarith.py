from itertools import permutations

def solve(letters, words, result):
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        # Avoid leading zeroes
        if any(mapping[word[0]] == 0 for word in words + (result,)):
            continue
        total = sum(int("".join(str(mapping[ch]) for ch in word)) for word in words)
        res = int("".join(str(mapping[ch]) for ch in result))
        if total == res:
            print("Solution:")
            for k in mapping:
                print(f"{k} = {mapping[k]}")
            return True
    print("No solution found.")
    return False

if __name__ == "__main__":
    puzzle = ("SEND", "MORE", "MONEY")
    unique_letters = set("".join(puzzle))
    if len(unique_letters) > 10:
        print("Too many unique letters!")
    else:
        solve(unique_letters, puzzle[:-1], puzzle[-1])
