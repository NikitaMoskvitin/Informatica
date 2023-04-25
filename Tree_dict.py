def New_node(x):

    '''Это вспомогательная функция, которая создает узел'''

    Node = { 'left' : None, 'right' : None, 'value' : x}
    return Node

def Chek(Node, a):

    '''Это вспомогательная функция, которая нужна для вставки элемента'''

    if Node['value'] >= a:
        if Node['left'] == None:
            Node['left'] = New_node(a)
        else:
            Node = Node['left']
            Chek(Node, a)
    else:
        if Node['right'] == None:
            Node['right'] = New_node(a)
        else:
            Node = Node['right']
            Chek(Node, a)

def Sozd_der():

    '''Функция создает дерево'''

    koren = None
    lst = list(map(int, input().split()))
    for i in range(len(lst)):
        if koren == None:
            koren = New_node((lst[i]))
        elif koren['left'] == None and lst[i] <= koren['value']:
            koren['left'] = New_node(lst[i])
        elif koren['right'] == None and lst[i] > koren['value']:
            koren['right'] = New_node(lst[i])
        else:
            if koren['value'] >= lst[i]:
                Node = koren['left']
                Chek(Node, lst[i])
            else:
                Node = koren['right']
                Chek(Node, lst[i])

    return koren

def proverka(koren):

    '''Функция проверяет дерево на пустоту'''

    if koren == None:
        print('Пусто')
    else:
        print('Не пусто')

def udol(koren):

    '''Функция удаляет дерево'''

    koren = None
    return koren

def Dob_zv(koren):

     '''Функция добавляет новое звено'''

     a = int(input())
     if koren['value'] >= a:
         Node = koren['left']
         Chek(Node, a)
     else:
         Node = koren['right']
         Chek(Node, a)

def poisk(Node, back, a):

    '''Это вспомогательная функция, которая помогает искать элемент'''

    if Node['value'] == a:
        return  Node, back
    elif Node['value'] < a:
        back = Node
        Node = Node['right']
        Node, back = poisk(Node, back, a)
        return Node, back
    else:
        back = Node
        Node = Node['left']
        Node, back = poisk(Node, back, a)
        return Node, back

def udol_poddereva(koren, a):

    '''Функция удаляет поддерево'''

    if koren['value'] == a:
        koren = udol(koren)
    else:
        back = koren
        if koren['value'] > a:
            Node = koren['left']
            Node, back = poisk(Node, back, a)
        else:
            Node = koren['right']
            Node, back = poisk(Node, back, a)

        if back['left'] == Node:
            back['left'] = None
        else:
            back['right'] = None

def glub(koren):

    '''Функция считает глубину дерева'''

    if koren == None:
        return 0
    else:
        return max(glub(koren['left']), glub(koren['right'])) + 1

def pechat_pram(koren):

    '''Функция печатет дерево в прямом порядке'''

    if koren == None:
        print('Нет дерева', end = ' ')
    else:
        print(koren['value'], end = ' ')
        _left(koren)
        _right(koren)

def _left(koren):

    '''Это вспомогательная функция, для печати дерева в прямом порядке'''

    if koren['left'] == None:
        return
    else:
        pechat_pram(koren['left'])

def _right(koren):

    '''Это вспомогательная функция, для печати дерева в прямом порядке'''

    if koren['right'] == None:
        return
    else:
        pechat_pram(koren['right'])

def pechat_obr(koren):

    '''Функция печатет дерево в обратном порядке'''

    if koren == None:
        print('Нет дерева', end = ' ')
    else:
        _left_obr(koren)
        _right_obr(koren)
        print(koren['value'], end = ' ')

def _left_obr(koren):

    '''Это вспомогательная функция, для печати дерева в обратном порядке'''

    if koren['left'] == None:
        return
    else:
        pechat_obr(koren['left'])

def _right_obr(koren):

    '''Это вспомогательная функция, для печати дерева в обратном порядке'''

    if koren['right'] == None:
        return
    else:
        pechat_obr(koren['right'])

def pechat_sim(koren):

    '''Функция печатет дерево в симметричномм порядке'''

    if koren == None:
        print('Нет дерева', end = ' ')
    else:
        _left_sim(koren)
        print(koren['value'], end=' ')
        _right_sim(koren)

def _left_sim(koren):

    '''Это вспомогательная функция, для печати дерева в симметричном порядке'''

    if koren['left'] == None:
        return
    else:
        pechat_sim(koren['left'])

def _right_sim(koren):

    '''Это вспомогательная функция, для печати дерева в симметричном порядке'''

    if koren['right'] == None:
        return
    else:
        pechat_sim(koren['right'])

def _min_glub(koren):

    '''Это вспомогательная функция, используется для нахождения минимальной глубины'''

    if koren == None:
        return 0
    else:
         return min(_min_glub(koren['left']), _min_glub(koren['right'])) + 1

def _balanced(koren):

    '''Эта функция определяет дерево сбалансированно или нет'''

    a = glub(koren)
    b = _min_glub(koren)
    if b + 1 < a:
        print('Дерево не сбаланисрованно')
    else:
        print('Дерево сбаланисрованно')

def udol_zvena(koren):

    '''Эта функция удаляет звено дерева'''

    a = int(input())
    if koren['value'] == a:
        udol_zvena_dop(koren)
    else:
        back = koren
        if koren['value'] > a:
            Node = koren['left']
            Node, back = poisk(Node, back, a)
            udol_zvena_dop(Node)
        else:
            Node = koren['right']
            Node, back = poisk(Node, back, a)
            udol_zvena_dop(Node)

def udol_zvena_dop(Node):

    '''Это вспомогательная функуия, используется для удаления звена'''

    zv = Node
    if Node['left'] != None:
        back = Node
        Node = Node['left']
        k = 0
        while Node['right'] != None:
            back = Node
            Node = Node['right']
            k = 1
        if Node['left'] != None:
            zv['value'] = Node['value']
            udol_zvena_dop(Node)
        else:
            zv['value'] = Node['value']
            if k == 0:
                back['left'] = None
            else:
                back['right'] = None
    elif Node['right'] != None:
        back = Node
        Node = Node['right']
        k = 0
        while Node['left'] != None:
            back = Node
            Node = Node['left']
            k = 1
        if Node['right'] != None:
            zv['value'] = Node['value']
            udol_zvena_dop(Node)
        else:
            zv['value'] = Node['value']
            if k == 0:
                back['right'] = None
            else:
                back['left'] = None
    else:
        udol_poddereva(koren, zv['value'])

def obh_shir(koren):

    '''Эта функуия печатет дерево обходя в ширину его'''

    a = []
    b = []
    a.append(koren['value'])
    b.append(koren['value'])
    while len(a) != 0:
        i = 0
        if koren['value'] == a[0]:
            Node = koren
        else:
            back = koren
            if koren['value'] > a[0]:
                Node = koren['left']
                Node, back = poisk(Node, back, a[0])
            else:
                Node = koren['right']
                Node, back = poisk(Node, back, a[0])
        if b.count(Node['value']) > 1:
            for i in range(b.count(Node['value']) - 1):
                Node = Node['left']
        if Node['left'] != None:
            a.append(Node['left']['value'])
            b.append(Node['left']['value'])
        if Node['right'] != None:
            a.append(Node['right']['value'])
            b.append(Node['right']['value'])
        a.pop(0)
    for i in range(len(b)):
        print(b[i], end = ' ')

while True:
    print('1 - Cоздание дерева(числа вводятся через пробел) \n2 - Проверка дерева на пустоту \n3 - Удаляет дерво \n4 - Добавляет новое звено \n5 - Удаляет поддерево \n6 - Показывает глубину \n7 - Печатает дерево в прямом порядке \n8 - Печатает дерево в обратном порядке \n9 - Печать дерева в симметричном порядке \n10 - Проверка на сбалансированность \n11 - Удаление звена \n12 - Печать дерева обходом в ширину \n13 - Показывает минимальную глубину')
    a = int(input())
    if a == 1:
        koren = Sozd_der()
    elif a == 2:
        proverka(koren)
    elif a == 3:
        koren = udol(koren)
    elif a == 4:
        Dob_zv(koren)
    elif a == 5:
        a = int(input())
        udol_poddereva(koren, a)
    elif a == 6:
        print(glub(koren))
    elif a ==7:
        pechat_pram(koren)
        print(end = '\n')
    elif a == 8:
        pechat_obr(koren)
        print(end = '\n')
    elif a == 9:
        pechat_sim(koren)
        print(end='\n')
    elif a == 10:
        _balanced(koren)
    elif a == 11:
        udol_zvena(koren)
    elif a == 12:
        obh_shir(koren)
        print(end='\n')
    elif a == 13:
        print((_min_glub(koren)))