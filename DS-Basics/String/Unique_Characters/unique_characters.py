def count_unique(word):
    seen = set()
    for c in word:
        seen.add(c)
    return seen
if __name__ == "__main__":
    string = "Muhammad Ismail"
    print(count_unique(string))