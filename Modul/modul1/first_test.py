def spam(number):
    return 'bulochka' * number



def my_sum(list_of_numbers):
    a = 0
    for i in list_of_numbers:
        if type(i) == int:
            a += i
    return a



def shortener(string):
    w = []
    for i in string.split():
        if len(i) > 6:
            i = i[:6] + "*"
            w.append(i)
        else:
            w.append(i)
    return " ".join(w)


def compare_ends(words):
    spk = []
    j = 0
    for i in words:
        if len(i) >= 2 and i[0] == i[-1]:
            spk.append(i)
            j += 1
    return j



