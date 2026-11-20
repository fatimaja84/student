def avg(grades):
    total = 0
    for grade in grades:
        total = total + grade
    return total / len(grades)


def max_grade(grades):
    return max(grades)


def min_grade(grades):
    return min(grades)
