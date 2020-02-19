"""
Знайдіть кількість входжень заданого числа x до впорядкованого за неспаданням масиву цілих чисел array
"""
def bsearch_leftmost(array, x):
    """ Бінарний пошук для відшукання найпершого входження заданого числа
    :param array: Відсортований за неспаданням масив цілих чисел
    :param x: Шукане число
    :return: Номер шуканого елемента у масиві
    """
    left = 0 # ліва границя пошуку
    right = len(array) # права границя пошуку
    while left < right:
        m = left + (right - left) // 2 # середина
        if array[m] < x:
            left = m + 1
        else:
            right = m
    return left 
def bsearch_rightmost(array, x):
    """ Бінарний пошук для відшукання останнього входження заданого числа
    :param array: Відсортований за неспаданням масив цілих чисел
    :param x: Шукане число
    :return: Номер шуканого елемента у масиві
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
def counter(array, x):
    """ кількість входжень заданого числа.
    :param array: Масив цілих чисел впорядкований за неспаданням
    :param x:     Шуканий елемент
    :return:      Кількість входжень
    """
    if array[bsearch_rightmost(array,x)-1]!=x:
        return 0
    return bsearch_rightmost(array,x)-bsearch_leftmost(array,x)+1

