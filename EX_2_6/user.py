def bsearch_rightmost(array, x):
    """ Бінарний пошук для відшукання останнього входження заданого числа
    :param array: Відсортований за неспаданням масив цілих чисел
    :param x:     Шукане число
    :return:      Номер шуканого елемента у масиві
    """
    left = 0 # ліва границя пошуку
    right = len(array) # права границя пошуку
    while left < right:
        m = left + (right - left) // 2 # Середина
        if array[m] <= x:
            left = m + 1
        else:
            right = m
    return left - 1
