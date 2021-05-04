import pygame
import pygame_menu
import sorting

pygame.init()
# Get resolution info
displayInfo = pygame.display.Info()
window_w = int(displayInfo.current_w / 2)
window_h = int(displayInfo.current_h / 2)

# Initialize global variables
selected_algorithm = None
min_value = None
max_value = None
array_size = None
bar_width = None
array = []
x = 0
y = 0

"""
Implementation of sorting algorithms
"""
# Insertion sort
def insertion_sort(array):
    i = 1
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        while i < len(array):
            j = i
            while j > 0 and array[j - 1] > array[j]:
                #swapping the value of [j - 1] and [j]
                array[j - 1], array[j] = array[j], array[j - 1]
                j = j - 1
                window.fill((255,255,255))
                display_bars(array)
                pygame.time.delay(1)
                pygame.display.update()
            i = i + 1
        running = False


# Bubble sort
def bubble_sort(array):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for i in range(len(array) - 1):
            for j in range(len(array) - i - 1):
                if array[j] > array[j + 1]:
                    t = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = t
                window.fill((255,255,255))
                display_bars(array)
                pygame.time.delay(1)
                pygame.display.update()
        running = False




# Set window size and title
window = pygame.display.set_mode([window_w, window_h])
pygame.display.set_caption("Sorting visualizer")

def set_algo(value, key):
    global selected_algorithm
    selected_algorithm = key
    print (selected_algorithm)

def set_min_value(value):
    global min_value
    min_value = int(value)
    print(min_value)

def set_max_value(value):
    global max_value
    max_value = int(value)
    print(max_value)

def set_array_size(value):
    global array_size
    global bar_width
    array_size = int(value)
    bar_width = window_w / array_size
    print(array_size)

def sort_display():
    init_array = sorting.init_array(min_value, max_value, array_size)
    if selected_algorithm == 0:
        insertion_sort(init_array)
    if selected_algorithm == 1:
        bubble_sort(init_array)

        

def display_bars(array):
    for i in range(len(array)):
        pygame.draw.rect(window, (255, 0, 0), (x + bar_width * i, y, bar_width, array[i] * window_h / max_value))


menu = pygame_menu.Menu('Sorting', window_w, window_h)
menu.add.text_input('Minimum value: ', onchange = set_min_value)
menu.add.text_input('Maximum value: ', onchange = set_max_value)
menu.add.text_input('Array size: ', onchange = set_array_size)
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