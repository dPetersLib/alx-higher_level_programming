#!/user/bin/python3
def remove_char_at(str, n):
    n_str = ''
    for i, c in enumerate(str):
        if i == n:
            continue
        n_str += c
    return n_str