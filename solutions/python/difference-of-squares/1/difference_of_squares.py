def square_of_sum(number):
    lst = list(range(1, number + 1))
    return sum(map(lambda x: x, lst)) ** 2


def sum_of_squares(number):
    lst = list(range(1, number + 1))
    return sum(map(lambda x: x ** 2, lst))


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)