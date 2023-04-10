def heap_up_min(a, i):

    '''Добавление элемента в минимальную кучу'''

    if len(a) == 1:
        return
    if i == 0:
        return
    if a[i] < a[( i - 1 )//2]:
        a[(i - 1) // 2], a[i] = a[i], a[(i-1)//2]
        k = (i-1) // 2
        heap_up_min(a,k)

def heap_down_min(a,i):

    '''Опускание элемента в минимальной куче'''

    if 2*i + 2 > len(a):
        return
    if a[i] > a[2*i + 1]:
        a[2*i + 1 ], a[i] = a[i], a[2*i + 1 ]
        k = 2*i + 1
        heap_down_min(a,k)
    if 2*i + 3 > len(a):
        return
    if a[i] <= a[2*i + 1] and a[i] <= a[2*i+2]:
        return
    if a[i] > a[2*i + 2]:
        a[2*i + 2 ], a[i] = a[i], a[2*i + 2 ]
        k = 2*i + 2
        heap_down_min(a,k)

def heap_up_max(a, i):

    '''Добавление элемента в максимальную кучу'''

    if len(a) == 1:
        return
    if i == 0:
        return
    if a[i] > a[( i - 1 )//2]:
        a[(i - 1) // 2], a[i] = a[i], a[(i-1)//2]
        k = (i-1) // 2
        heap_up_max(a,k)

def heap_down_max(a,i):

    '''Опускание элемента в максимальной куче'''

    if 2*i + 2 > len(a):
        return
    if a[i] < a[2*i + 1]:
        a[2*i + 1 ], a[i] = a[i], a[2*i + 1 ]
        k = 2*i + 1
        heap_down_max(a,k)
    if 2*i + 3 > len(a):
        return
    if a[i] >= a[2*i + 1] and a[i] >= a[2*i+2]:
        return
    if a[i] < a[2*i + 2]:
        a[2*i + 2 ], a[i] = a[i], a[2*i + 2 ]
        k = 2*i + 2
        heap_down_max(a,k)

def heap_min(a):

    '''Создание минимальной кучи'''

    h_min = []
    for j in range(len(a)):
        h_min.append(a[j])
        i = len(h_min) - 1
        heap_up_min(h_min, i)
    return h_min

def heap_max(a):

    '''Создание максимальной кучи'''

    h_max = []
    for j in range(len(a)):
        h_max.append(a[j])
        i = len(h_max) - 1
        heap_up_max(h_max, i)
    return h_max

def min_sort(h_min):

    '''Минимальная сортировка'''

    h_min_sort = []
    h_min_sort.append(h_min[0])
    for j in range(len(h_min) - 1):
        h_min[0] = h_min.pop()
        i = 0
        heap_down_min(h_min, i)
        h_min_sort.append(h_min[0])
    return h_min_sort

def max_sort(h_max):

    '''Максимальная сортировка'''

    h_max_sort = []
    h_max_sort.append(h_max[0])
    for j in range(len(h_max) - 1):
        h_max[0] = h_max.pop()
        i = 0
        heap_down_max(h_max, i)
        h_max_sort.append(h_max[0])
    return h_max_sort


