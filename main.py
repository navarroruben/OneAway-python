# Ruben Navarro
# 12/10/2019
# main.py
# CTCI - One Away
# Given two strings, checks if there are 1 or 2 edits aware from modification. Returns true for 1 edit, false if otherwise.

# checks if both strings are empty
def check_if_empty(s, s2):
    if not s or s2:
        return False

# checks if
def check_edits(s, s2):
    total = 0
    if len(s2) > len(s):
            return False
    elif len(s) > len(s2):
        total += 1
        if (len(s) - len(s2)) > 1:
            return False

    for c in s2:
        num = s.count(c)
        if num == 0:
            total += 1
            if total > 1:
                return False

    return True


# driver

str = "pales"
str2 = "pake"

flag = check_if_empty(str.lower(), str2.lower())
flag2 = check_edits(str.lower(), str2.lower())

if flag2 is not True:
    print("More than 1 edit away")
    exit()
else:
    print("1 Edit away")
