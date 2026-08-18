def check_balance(w):
    counts = [0, 0]
    for c in w:
        if c == "(":
            counts[0] += 1
        if c == ")":
            counts[1] += 1

    return counts[0] == counts[1]


def check_correct(w):
    stacks = []

    for c in w:
        if c == "(":
            stacks.append(c)
        else:
            if stacks and stacks[-1] == "(":
                stacks.pop()

    return len(stacks) == 0


def detatch(w):
    for i in range(2, len(w), 2):
        u = w[:i]
        v = w[i:]

        if check_balance(u):
            return u, v

    return w, ""


def four_four(w):
    s = ""

    for i in range(1, len(w) - 1):
        if w[i] == ")":
            s += "("
        else:
            s += ")"

    return s


def check(w):
    if w == "":
        return ""

    u, v = detatch(w)

    if check_correct(u):
        u = u + check(v)
    else:
        s = "(" + check(v) + ")"
        u = s + four_four(u)

    return u


def solution(p):
    return check(p)
