def split(string, size):
    words = []
    word = ""
    for i in range(size):
        if string[i] == " ":
            words.append(word)
            word = ""
            continue
        word += string[i]
        if i == size - 1:
            words.append(word)
    return words


def urlify(string, size):
    words = split(string, size)
    result = ""
    for i in range(len(words) - 1):
        result += words[i] + "%20"
    return result + words[len(words) - 1]


print(urlify("Mr Hany Osman            ", 13))
print(urlify("Mr Hany Osman", 13))
