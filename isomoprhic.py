def isomorphic(s, t):
    if len(s) != len(t):
        return False
    mapping_s_to_t = {}
    mapping_t_to_s = {}
    for char_s, char_t in zip(s, t):
        if char_s not in mapping_s_to_t:
            mapping_s_to_t[char_s] = char_t
        elif mapping_s_to_t[char_s] != char_t:
            return False
        if char_t not in mapping_t_to_s:
            mapping_t_to_s[char_t] = char_s
        elif mapping_t_to_s[char_t] != char_s:
            return False
    return True
s1 = "egg"
t1 = "add"
print(isomorphic(s1, t1))
