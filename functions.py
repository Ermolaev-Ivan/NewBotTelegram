# две функции окончаний не абсолютные, но для наших нужд подходящие
def ending(el):
    num_list = [12, 13, 14, 15, 16, 17, 18, 19]
    a = el % 10
    if el in num_list:
        return ""
    elif a == 2 or a == 3 or a == 4:
        return "а"
    else:
        return ""


def ending2(el):
    if el == 1:
        return "-го человека"
    else:
        return "-х человек"