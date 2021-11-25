def upper(s,i):
    if s[i] == s[i].upper():
        return s[i]
    else:
        return upper(s,i+1)
