def string_len(s):
    if s == '':
        return 0
    else:
        return 1 + string_len(s[1:])
