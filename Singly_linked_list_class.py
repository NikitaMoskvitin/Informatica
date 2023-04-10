class Zveno:

    '''Класс звеньев'''

    def __init__(self, data):
        self.value = data
        self.next = None

class Spisoc:

    '''Класс списков'''

    def __init__(self):
        self.head = None

    def dob_v_nachalo(self):

        '''Функция добаляет элемент в начало'''
        a = input()
        current = Zveno(a)
        current.next = self.head
        self.head = current

    def dob_v_conec(self):

        '''Функция добовляет элемент в конец'''

        a = input()
        current = self.head
        while current != None:
            prev = current
            current = current.next
        current = Zveno(a)
        prev.next = current

    def vstavka_posl(self):

        '''Функция добовляет элемент послк элемента с введеным значением'''

        a = input()
        current = self.head
        while current.value != a:
            prev = current
            current = current.next
        prev = current
        b = input()
        current = Zveno(b)
        current.next = prev.next
        prev.next = current

    def udol_nachalo(self):

        '''Функция удаляет начальный элемент'''

        prev = self.head
        current = prev.next
        self.head = current

    def udol_conec(self):

        '''Функция удаляет последний элемент'''

        current = self.head
        while current.next != None:
            prev = current
            current = current.next
        prev.next = None

    def udol_posl(self):

        '''Функция удаляет элемент с введеным значением'''

        a = input()
        current = self.head
        while current.value != a:
            prev = current
            current = current.next
        prev.next = current.next

    def pechat(self):

        '''Функция печаете список'''

        current = self.head
        while current != None:
            print(current.value)
            current = current.next

    def udol(self):

        '''Функция удаляет список'''

        self.head = None

n = int(input())
s = Spisoc()
for i in range(n):
    if i == 0:
        s.dob_v_nachalo()
    else:
        s.dob_v_conec()

while 1 > 0:
    i = int(input())
    if i == 1:
        s.dob_v_nachalo()
    elif i == 2:
        s.dob_v_conec()
    elif i == 3:
        s.vstavka_posl()
    elif i == 4:
        s.udol_nachalo()
    elif i == 5:
        s.udol_conec()
    elif i == 6:
        s.udol_posl()
    elif i == 7:
        s.pechat()
    elif i == 8:
        s.udol()


