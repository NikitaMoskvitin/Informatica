def new_zveno(value):

    '''Создаем новое звено'''
    return {'prev': None, 'value': value, 'next': None}

def sozd_spiska():

    '''Создание списка'''

    list = {'head': None, 'tail': None}
    n = int(input())
    for i in range(n):
        value = int(input())
        current = new_zveno(value)
        if list['head'] == None:
            list['head'] = current
            list['tail'] = current
        else:
            prev['next'] = current
            current['prev'] = prev
            list['tail'] = current
        prev = current
    return list

def dob_zv_golova(list):

    '''Добавление элемента в голову'''

    value = int(input())
    prev = new_zveno(value)
    current = list['head']
    prev['next'] = list['head']
    list['head'] = prev
    current['prev'] = prev
    return list

def dob_zv_conec(list):

    '''Добавление элементу в хвост'''

    value = int(input())
    current = new_zveno(value)
    prev = list['tail']
    prev['next'] = current
    current['prev'] = prev
    list['tail'] = current
    return list

def dob_posl_el(list):

    '''Добавление элемента после определнного элемнета'''

    value = int(input())
    current = list['head']
    while current['value'] != value:
        current = current['next']
    prev = current
    b = int(input())
    current = new_zveno(b)
    current['next'] = prev['next']
    current2 = prev['next']
    prev['next'] = current
    current['prev'] = prev
    current2['prev'] = current

def udol_1zv(list):

    '''Удаление первого элемента'''

    prev = list['head']
    current = prev['next']
    list['head'] = current
    current['prev'] = None
    return list

def udol_lastzv(list):

    '''Удаление последнего элемента'''

    current = list['tail']
    prev = current['prev']
    list['tail'] = prev
    prev['next'] = None
    return list


def udol_opred_el(list):

    '''Удаление определенного элемента'''

    value = int(input())
    current = list['head']
    while current['value'] != value:
        prev = current
        current = current['next']
    prev['next'] = current['next']
    current = current['next']
    current['prev'] = prev

def pechat_pram(list):

    '''Печать списка в прямом порядке'''

    current = list['head']
    while current != None:
        print(current['value'])
        current = current['next']

def pechat_obr(list):

    '''Печать списка в обратном порядке'''

    current = list['tail']
    while current != None:
        print(current['value'])
        current = current['prev']

def udol_spiska(list):

    '''Удаление списка'''

    list = {'head': None, 'tail': None}
    return list

while 1 > 0:
    i = int(input())
    if i == 1:
        list = sozd_spiska()
    elif i == 2:
        list = dob_zv_golova(list)
    elif i == 3:
        list = dob_zv_conec(list)
    elif i == 4:
        dob_posl_el(list)
    elif i == 5:
        list = udol_1zv(list)
    elif i == 6:
        list = udol_lastzv(list)
    elif i == 7:
        udol_opred_el(list)
    elif i == 8:
        list = udol_spiska(list)
    elif i == 9:
        pechat_pram(list)
    elif i == 10:
        pechat_obr(list)
