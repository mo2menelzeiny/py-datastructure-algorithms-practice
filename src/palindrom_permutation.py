def is_palindrome(string):
    # count letters
    letters_count = {}
    for i in range(len(string)):
        letter = string[i]
        # avoid counting spaces
        if letter != " ":
            # avoid un-allocated key errors
            if letters_count.get(letter):
                letters_count[letter] += 1
            else:
                letters_count[letter] = 1
    # count odd and even counts
    odd_count = 0
    for k, v in letters_count.items():
        if v % 2 != 0:
            odd_count += 1
    if odd_count > 1:
        return False  # if more than one odd return false

    return True  # if all letters have even count return true


print(is_palindrome("ba ba"))
print(is_palindrome("ba bazn"))
print(is_palindrome("tact coa"))
