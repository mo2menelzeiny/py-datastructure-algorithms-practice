
def all_unique(string):
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False
    return True


print(all_unique("car"))


def all_unique_bin(string: str):
    checker = 0
    for i in range(len(string)):
        val = ord(string[i])
        if checker & (1 << val):
            return False
        checker = checker | (1 << val)
    return True


print(all_unique_bin("carz"))
