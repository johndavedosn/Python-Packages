def get_middle_elements(lst):
    length = len(lst)
    if length % 2 == 1:
        return lst[length // 2],
    else:
        middle_left = lst[length // 2 - 1]
        middle_right = lst[length // 2]
        return middle_left, middle_right
def weird_algo(l, n):
    l_copy = list(l)
    mids = get_middle_elements(l)
    if len(mids) == 1 and mids[0] == n:
        return l.index(mids[0])
    if len(mids) == 2:
        if mids[0] == n or mids[1] == n:
            return l.index(mids[0] if n == mids[0] else mids[1])
    for mid in mids:
        l_copy.remove(mid)
    if len(l_copy) <= 1:
        raise ValueError("Element was not found")
    return weird_algo(l_copy, n)
