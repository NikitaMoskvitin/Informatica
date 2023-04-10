class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):

        '''Функция проверяет пуст ли список'''

        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self,item):

        '''Функция добавляет элемент в стэк'''

        self.items.append(item)

    def pop(self):

        '''Функция удаляет элемент из стэка'''

        a = self.items.pop()

        return a
    def size(self):

        '''Функция вощварщает размер стэка'''

        return len(self.items)

    def pechat(self):

        '''Функция печатет стэк'''

        for i in range(len(self.items)):
            print(self.items[len(self.items) - 1 - i])

    def get(self):

        '''Функция возвращает верхний элемент'''

        return self.items[len(self.items) - 1]
