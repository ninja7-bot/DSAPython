# Check for a repeating character in a string.
def repfree(s):
    checked = []
    for i in range(len(s)):
        checked.append(s[i])
        for j in range(i+1, len(s)):
            if s[j] in checked:
                return False
    return True