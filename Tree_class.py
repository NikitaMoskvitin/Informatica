class Zveno:

    '''Класс звеньев'''

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:

    '''Класс дереьв'''

    def __init__(self):
        self.root = None

    def _insert_full(self, a):

        '''Эта функция вставляет звено в дерево'''

        Tree.__insert(self, self.root, a)

    def __insert(self, Node, a):

        '''ВНУТРЕННЯЯ ФУНКЦИЯ, вставляет звено в дерево'''

        if a <= Node.value:
            if Node.left == None:
                Node.left = Zveno(a)
            else:
                Node = Node.left
                Tree.__insert(self, Node, a)
        else:
            if Node.right == None:
                Node.right = Zveno(a)
            else:
                Node = Node.right
                Tree.__insert(self, Node, a)

    def __find_full(self, a):

        '''ВНУТРЕННЯЯ ФУНКЦИЯ, ищет нужный элемент в дереве, начиная с корня'''

        return Tree.__find(self, self.root, None, a)

    def __find(self, Node, back, a):

        '''ВНУТРЕННЯЯ ФУНКЦИЯ, ищет нужный элемент в дереве'''

        if Node.value == a:
            return Node, back
        elif Node.value < a:
            back = Node
            Node = Node.right
            Node, back = Tree.__find(self, Node, back, a)
            return Node, back
        else:
            back = Node
            Node = Node.left
            Node, back = Tree.__find(self, Node, back, a)
            return Node, back

    def _create_tree(self):

        '''Эта функция создает дерево'''

        _list = list(map(int, input().split()))
        self.root = Zveno(_list[0])
        for i in range(len(_list) - 1):
            Tree._insert_full(self, _list[i + 1])


    def _delete_underTree(self, a):

        '''Эта функция удаляет поддерево'''

        Node, back = Tree.__find_full(self, a)
        if back.left == Node:
            back.left = None
        else:
            back.right = None

    def _check(self):

        '''Эта функция проверяет дерево на пустоту'''

        if self.root == None:
            return 0
        else:
            return 1

    def _delete_Tree(self):

        '''Эта функция удаляет все дерево'''

        self.root = None

    def _find_depth_full(self):

        '''Эта функция ищет максимальную глубину дерва'''

        return Tree.__find_depth(self, self.root)

    def __find_depth(self, Node):

        '''ВНУТРЕННЯЯ ФУНКЦИЯ, ищет максимальную глубину дерева'''

        if Node == None:
            return 0
        else:
            return max(Tree.__find_depth(self, Node.left), Tree.__find_depth(self, Node.right)) + 1

    def _find_depth_min_full(self):

        '''Эта функция ищет минимальную глубину дерва'''

        return Tree.__find_depth_min(self, self.root)

    def __find_depth_min(self, Node):

        '''ВНУТРЕННЯЯ ФУНКЦИЯ, ищет минимальную глубину дерева'''

        if Node == None:
            return 0
        else:
            return min(Tree.__find_depth_min(self, Node.left), Tree.__find_depth_min(self, Node.right)) + 1

    def _balance(self):

        '''Эта функция проверяет сбалансировано ли дерево'''

        _min = Tree.__find_depth_min(self, self.root)
        _max = Tree.__find_depth(self, self.root)
        if _max - _min <= 1:
            return 1
        else:
            return 0

    def _sym_print_full(self):

        '''Эта функция печатает дерево в симметричном порядке'''

        Tree.__sym_print(self, self.root)

    def __sym_print(self, Node):

        '''ВНУТРЕННЯЯ ФУНКЦИЯ, печатает дерево в симметричном порядке'''

        Tree.__sym_left(self, Node)
        print(Node.value, end = ' ')
        Tree.__sym_right(self, Node)

    def __sym_left(self, Node):

        '''ВНУТРЕННЯЯ ФУНКЦИЯ, вспомогательная функция, для печати дерева в симметричном порядке'''

        if Node.left == None:
            return
        else:
            Tree.__sym_print(self, Node.left)

    def __sym_right(self, Node):

        '''ВНУТРЕННЯЯ ФУНКЦИЯ, вспомогательная функция, для печати дерева в симметричном порядке'''

        if Node.right == None:
            return
        else:
            Tree.__sym_print(self, Node.right)

    def _stright_print_full(self):

        '''Эта функция печатает дерево в прямом порядке'''

        Tree.__straight_print(self, self.root)

    def __straight_print(self, Node):

        '''ВНУТРЕННЯЯ ФУНКЦИЯ, печатает дерево в прямом порядке'''

        print(Node.value, end = ' ')
        Tree.__straight_left(self, Node)
        Tree.__straight_right(self, Node)

    def __straight_left(self, Node):

        '''ВНУТРЕННЯЯ ФУНКЦИЯ, вспомогательная функция, для печати дерева в прямом порядке'''

        if Node.left == None:
            return
        else:
            Tree.__straight_print(self, Node.left)

    def __straight_right(self, Node):

        '''ВНУТРЕННЯЯ ФУНКЦИЯ, вспомогательная функция, для печати дерева в прямом порядке'''

        if Node.right == None:
            return
        else:
            Tree.__straight_print(self, Node.right)

    def _back_print_full(self):

        '''Эта функция печатает дерево в обратном порядке'''

        Tree.__back_print(self, self.root)

    def __back_print(self, Node):

        '''ВНУТРЕННЯЯ ФУНКЦИЯ, печатает дерево в обратном порядке'''

        Tree.__back_left(self, Node)
        Tree.__back_right(self, Node)
        print(Node.value, end = ' ')

    def __back_left(self, Node):

        '''ВНУТРЕННЯЯ ФУНКЦИЯ, вспомогательная функция, для печати дерева в обратном порядке'''

        if Node.left == None:
            return
        else:
            Tree.__back_print(self, Node.left)

    def __back_right(self, Node):

        '''ВНУТРЕННЯЯ ФУНКЦИЯ, вспомогательная функция, для печати дерева в обратном порядке'''

        if Node.right == None:
            return
        else:
            Tree.__back_print(self, Node.right)

    def _round_width(self):

        '''Это функция печатет дерево обходм в ширину'''

        a = []
        b = []
        a.append(self.root.value)
        b.append(self.root.value)
        while len(a) != 0:
            Node, back = Tree.__find_full(self, a[0])
            if b.count(Node.value) > 1:
                for i in range(b.count(Node.value) - 1):
                    Node = Node.left
            if Node.left != None:
                a.append(Node.left.value)
                b.append(Node.left.value)
            if Node.right != None:
                a.append(Node.right.value)
                b.append(Node.right.value)
            a.pop(0)
        for i in range(len(b)):
            print(b[i], end=' ')

    def _delete_node(self, a):

        '''Эта функция удаляет звено'''

        Node, back = Tree.__find_full(self, a)
        main_Node = Node
        main_back = back
        if Node.left != None:
            back = Node
            Node = Node.left
            k = 0
            while Node.right != None:
                back = Node
                Node = Node.right
                k = 1
            if Node.left != None:
                main_Node.value = Node.value
                Tree._delete_node(self, Node.value)

            else:
                main_Node.value = Node.value
                if k == 1:
                    back.right = None
                else:
                    back.left = None
        elif Node.right != None:
            back = Node
            Node = Node.right
            k = 0
            while Node.left != None:
                back = Node
                Node = Node.left
                k = 1
            if Node.right != None:
                main_Node.value = Node.value
                Tree._delete_node(self, Node.value)
            else:
                main_Node.value = Node.value
                if k == 1:
                    back.left = None
                else:
                    back.right = None
        else:
            if main_back.left == main_Node:
                main_back.left = None
            else:
                main_back.right = None

t = Tree()
while True:
    print('1 - Cоздание дерева(числа вводятся через пробел) \n2 - Проверка дерева на пустоту \n3 - Удаляет дерво \n4 - Добавляет новое звено \n5 - Удаляет поддерево \n6 - Показывает максимальную глубину \n7 - Печатает дерево в прямом порядке \n8 - Печатает дерево в обратном порядке \n9 - Печать дерева в симметричном порядке \n10 - Проверка на сбалансированность \n11 - Удаление звена \n12 - Печать дерева обходом в ширину \n13 - Показывает минимальную глубину')
    a = int(input())
    if a == 1:
        t._create_tree()
    elif a == 2:
        if t._check() == 1:
            print('Дерево не пусто')
        else:
            print('Дерево пусто')
    elif a == 3:
        t._delete_Tree()
    elif a == 4:
        b = int(input())
        t._insert_full(b)
    elif a == 5:
        b = int(input())
        t._delete_underTree(b)
    elif a == 6:
        print(t._find_depth_full())
    elif a == 7:
        t._stright_print_full()
        print(end='\n')
    elif a == 8:
        t._back_print_full()
        print(end='\n')
    elif a == 9:
        t._sym_print_full()
        print(end='\n')
    elif a == 10:
        if t._balance() == 1:
            print('Дерево сблансированно')
        else:
            print('Дерево не сблансированно')
    elif a == 11:
        b = int(input())
        t._delete_node(b)
    elif a == 12:
        t._round_width()
        print(end='\n')
    elif a == 13:
        print(t._find_depth_min_full())



