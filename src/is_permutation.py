

def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    ss1 = sorted(s1)
    ss2 = sorted(s2)
    for i in range(len(ss1)):
        if ss1[i] != ss2[i]:
            return False
    return True


print(is_permutation("car", "rcaa"))
print(is_permutation("car", "rca"))
print(is_permutation("cara", "rcaa"))