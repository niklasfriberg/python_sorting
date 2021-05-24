import pygame
import pygame_menu
import sorting
import math

pygame.init()
# Get resolution info
displayInfo = pygame.display.Info()
window_w = int(displayInfo.current_w / 2)
window_h = int(displayInfo.current_h / 2)

# Initialize global variables
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TURQUOISE = (0, 255, 255)
selected_algorithm = None
min_value = 0
max_value = 100
array_size = 20
time_delay = 1000
bar_width = None
array = []
color_array = []
x = 0
y = 0

"""
Implementation of sorting algorithms
"""
# Insertion sort
def insertion_sort():
    i = 1
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        while i < len(array):
            j = i
            while j > 0 and array[j - 1] > array[j]:
                color_array[j] = BLUE
                color_array[j - 1] = BLUE
                #swapping the value of [j - 1] and [j]
                array[j - 1], array[j] = array[j], array[j - 1]
                draw_bars()
                color_array[j] = RED
                color_array[j - 1] = RED
                j = j - 1
            i = i + 1
        running = False


# Bubble sort
def bubble_sort():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for i in range(len(array) - 1):
            for j in range(len(array) - i - 1):
                color_array[j] = BLUE
                color_array[j + 1] = BLUE
                draw_bars()
                if array[j] > array[j + 1]:
                    t = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = t
                color_array[j] = RED
                color_array[j + 1] = RED
                

        running = False

# Merge sort
def merge_sort(array, l, r):
    mid = (l + r) // 2
    if l < r:
        merge_sort(array, l, mid)
        merge_sort(array, mid + 1, r)
        merge(array, l, mid, mid + 1, r)

def merge(array, x1, y1, x2, y2):
    i = x1
    j = x2
    temp = []
    while i <= y1 and j <= y2:
        color_array[i] = BLUE
        color_array[j] = BLUE
        draw_bars()
        color_array[i] = RED
        color_array[j] = RED
        if array[i] < array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1

    while i <= y1:
        color_array[i] = BLUE
        draw_bars()
        color_array[i] = RED
        temp.append(array[i])
        i += 1
    while j <= y2:
        color_array[j] = BLUE
        draw_bars()
        color_array[j] = RED
        temp.append(array[j])
        j += 1
    j = 0
    for i in range(x1, y2 + 1):
        array[i] = temp[j]
        j += 1
        color_array[i] = GREEN
        draw_bars()
        color_array[i] = RED

# Quick sort
# Using hoares partition scheme
def quick_sort(array, lo = 0, hi = None):
    if hi == None:
        hi = len(array) - 1
    
    if lo < hi:
        p = partition(array, lo, hi)
        quick_sort(array, lo, p)
        quick_sort(array, p + 1, hi)

def partition(array, lo, hi):
    pivot_number = math.floor((hi + lo) / 2)
    pivot = array[pivot_number]
    color_array[pivot_number] = TURQUOISE
    i = lo - 1
    j = hi + 1
    while True:
        i += 1
        while array[i] < pivot:
            color_array[i] = BLUE
            draw_bars()
            color_array[i] = RED
            i += 1
        j -= 1
        while array[j] > pivot:
            color_array[j] = BLUE
            draw_bars()
            color_array[j] = RED
            j -= 1
        if i >= j:
            color_array[pivot_number] = RED
            return j
        color_array[i] ,color_array[j] = GREEN, BLUE
        draw_bars()
        array[i], array[j] = array[j], array[i]
        color_array[i], color_array[j] = BLUE, GREEN
        draw_bars()
        color_array[i], color_array[j] = RED, RED
        

# Set window size and title
window = pygame.display.set_mode([window_w, window_h])
pygame.display.set_caption("Sorting visualizer")

def display_final():
    draw_bars()
    pygame.time.delay(10)

def init_color():
    global color_array
    color_array = [(255,0,0) for _ in range(array_size)]

def set_algo(value, key):
    global selected_algorithm
    selected_algorithm = key
    print (selected_algorithm)

def set_min_value(value):
    global min_value
    min_value = value

def set_max_value(value):
    global max_value
    max_value = value

def set_array_size(value):
    global array_size
    array_size = value

def set_time_delay(value):
    global time_delay
    time_delay = value

def sort_display():
    global array
    global bar_width
    bar_width = window_w / array_size
    init_color()
    array = sorting.init_array(int(min_value), int(max_value), int(array_size))
    if selected_algorithm == 0:
        insertion_sort()
        display_final()
    if selected_algorithm == 1:
        bubble_sort()
        display_final()
    if selected_algorithm == 2:
        merge_sort(array, 0, array_size - 1)
        display_final()
    if selected_algorithm == 3:
        quick_sort(array)
        display_final()


def draw_bars():
    global array
    global color_array
    window.fill((255,255,255))
    for i in range(len(array)):
        pygame.draw.rect(window, color_array[i], (x + bar_width * i, y, bar_width * 0.7, array[i] * window_h / max_value))
    pygame.time.delay(int(time_delay))
    pygame.display.update()

menu = pygame_menu.Menu('Sorting', window_w, window_h)
menu.add.text_input('Minimum value: ', 0, input_type=pygame_menu.locals.INPUT_INT, onchange = set_min_value)
menu.add.text_input('Maximum value: ', 100, input_type=pygame_menu.locals.INPUT_INT, onchange = set_max_value)
menu.add.text_input('Array size: ', 20, input_type=pygame_menu.locals.INPUT_INT, onchange = set_array_size)
menu.add.text_input('Tick time (ms): ', 1000, input_type=pygame_menu.locals.INPUT_INT, onchange = set_time_delay)
menu.add.dropselect(
    title = 'Sorting algorithm',
    items=[('Insertion sort', 0),
    ('Bubble sort', 1),
    ('Merge sort', 2),
    ('Quick sort', 3)],
    font_size=20,
    selection_option_font_size=20,
    onchange=set_algo
)
menu.add.button('Start', sort_display)


def main_menu():
    runMenu = True
    menu.mainloop(window)
    while runMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
    

# Game loop
main_menu()



# Quit game
pygame.quit()