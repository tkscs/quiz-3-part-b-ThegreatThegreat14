def check_palindrome(string):
    if len(string) == 1:
        return True
    else:
        if len(string) % 2 == 0:
            i = 1
            while True:
                if i != len(string)/2 + 1:
                    if string[i - 1] == string[-i]:
                        i = i + 1
                    else:
                        return False
                else:
                    return True
        else:
            i = 1
            while True:
                if i != (len(string) - 1)/2 + 1:
                    if string[i - 1] == string[-i]:
                        i = i + 1
                    else:
                        return False
                else:
                    return True

print(check_palindrome(""))