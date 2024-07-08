import numbers

S = input()

Ss = "("
Se = ")"
Bs = "["
Be = "]"

stack = []


def check_sum_number():
    if len(stack) > 2:
        if isinstance(stack[-1], numbers.Number):
            if isinstance(stack[-2], numbers.Number):
                stack.append(stack.pop() + stack.pop())


def safe_pop():
    if len(stack) == 0:
        raise
    return stack.pop()


def append_something(number, s):
    p = safe_pop()
    if p == s:
        stack.append(number)
        return
    if isinstance(p, numbers.Number):
        if safe_pop() != s:
            raise
        stack.append(p * number)
        check_sum_number()
        return
    raise


def run():
    for i in S:
        # print(i, stack)
        check_sum_number()
        if i == Ss:
            stack.append(i)
            continue
        if i == Bs:
            stack.append(i)
            continue
        if i == Se:
            append_something(2, Ss)
            continue
        if i == Be:
            append_something(3, Bs)
            continue


try:
    run()
    print(sum(stack))
except:
    print(0)
