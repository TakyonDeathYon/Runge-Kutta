# Main script
def solve(func, t, y, h):
    # need to add checking for parameter correctness
    k_one = func(t, y)
    k_two = func(t + h / 2, y + k_one / 2)
    k_three = func(t + h / 2, y + k_one / 2)
    k_four = func(t + h, y + k_three)
    y_next = y + (k_one + 2 * k_two + 2 * k_three + k_four) * (h / 6)
    return y_next


def graph(func, t, y, h, steps):
    if steps == 1:
        return [[t + h, solve(func, t, y, h)]]
    y_next = solve(func, t, y, h)
    return [[t + h, solve(func, t, y, h)]] + graph(func, t + h, y_next, h, steps - 1)
