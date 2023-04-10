def new_zveno(value):

    '''Создаем новое звено'''
    return {'value': value, 'next': None}

def sozd_spiska(head):

    '''Создание списка'''

    n = int(input())
    for i in range(n):
        value = int(input())
        current = new_zveno(value)
        if head == None:
            head = current
        else:
            prev['next'] = current
        prev = current
    return head

def dob_zv_golova(head):

    '''Добавление элемента в голову'''

    value = int(input())
    prev = new_zveno(value)
    prev['next'] = head
    head = prev
    return head

def dob_zv_conec(head):

    '''Добавление элементу в хвост'''

    current = head
    while current!= None:
        prev = current
        current = current['next']
    value = int(input())
    current = new_zveno(value)
    prev['next'] = current


def dob_posl_el(head):

    '''Добавление элемента после определнного элемнета'''

    value = int(input())
    current = head
    while current['value'] != value:
        current = current['next']
    prev = current
    b = int(input())
    current = new_zveno(b)
    current['next'] = prev['next']
    prev['next'] = current

def udol_1zv(head):

    '''Удаление первого элемента'''

    prev = head
    current = prev['next']
    head = current
    return head

def udol_lastzv(head):

    '''Удаление последнего элемента'''

    perv1 = head
    current = head['next']
    while current != None:
        prev2 = perv1
        perv1 = current
        current = current['next']
    prev2['next'] = None


def udol_opred_el(head):

    '''Удаление определенного элемента'''

    value = int(input())
    current = head
    while current['value'] != value:
        prev = current
        current = current['next']
    prev['next'] = current['next']

def pechat(head):

    '''Печать списка'''

    current = head
    while current != None:
        print(current['value'])
        current = current['next']

def udol_spiska(head):

    '''Удаление списка'''

    head = None
    return head

head = None
while 1 > 0:
    i = int(input())
    if i == 1:
        head = sozd_spiska(head)
    elif i == 2:
        head = dob_zv_golova(head)
    elif i == 3:
        dob_zv_conec(head)
    elif i == 4:
        dob_posl_el(head)
    elif i == 5:
        head = udol_1zv(head)
    elif i == 6:
        udol_lastzv(head)
    elif i == 7:
        udol_opred_el(head)
    elif i == 8:
        head = udol_spiska(head)
    elif i == 9:
        pechat(head)


