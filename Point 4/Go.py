# Python equivalent of the Go code for reversing a string

def reverse_string(s):
    r = list(s)  # convert string to list of characters (Python strings are immutable)
    i, j = 0, len(r) - 1
    while i < j:
        r[i], r[j] = r[j], r[i]  # swap characters
        i += 1
        j -= 1
    return ''.join(r)  # convert list of characters back to string