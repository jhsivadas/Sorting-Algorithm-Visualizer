import pyximport
pyximport.install()
import pygame
import algorithms
import random
import slider as sld
import button as btn

pygame.init()
WIDTH = 1200
HEIGHT = 700
DSP = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
sort = ""
pygame.display.set_caption("Sorting Algorithm Visualizer")
font = pygame.font.Font('freesansbold.ttf', 15)

# Creating slider objects
arr_size = sld.Slider(275, 125, 125)
sort_speed = sld.Slider(690, 125, 615)

# Creating all the button objects
merge = btn.Button(170, 30, 130, 40, (255, 255, 255), DSP, font, "Merge Sort")
quick = btn.Button(310, 30, 130, 40, (255, 255, 255), DSP, font, "Quick Sort")
bubble = btn.Button(450, 30, 130, 40, (255, 255, 255), DSP, font, "Bubble Sort")
insertion = btn.Button(590, 30, 130, 40, (255, 255, 255), DSP, font, "Insertion Sort")
selection = btn.Button(730, 30, 130, 40, (255, 255, 255), DSP, font, "Selection Sort")
start = btn.Button(1040, 30, 100, 40, (0, 255, 0), DSP, font, "Sort Array")
create = btn.Button(1010, 100, 160, 40, (255, 255, 255), DSP, font, "Create New Array")

"""
This function determines if a button is clicked on. 
When a button is clicked on, it sets the sorting algorithm to the button's algorithm, shades the button, and 
sets all other buttons back to default.
"""
def click(event, arr_type):
    if event.type == pygame.MOUSEBUTTONDOWN and merge.hovering():
        merge.color = (211, 211, 211)
        change_back()
        return "merge"
    elif event.type == pygame.MOUSEBUTTONDOWN and quick.hovering():
        quick.color = (211, 211, 211)
        change_back()
        return "quick"
    elif event.type == pygame.MOUSEBUTTONDOWN and bubble.hovering():
        bubble.color = (211, 211, 211)
        change_back()
        return "bubble"
    elif event.type == pygame.MOUSEBUTTONDOWN and insertion.hovering():
        insertion.color = (211, 211, 211)
        change_back()
        return "insertion"
    elif event.type == pygame.MOUSEBUTTONDOWN and selection.hovering():
        selection.color = (211, 211, 211)
        change_back()
        return "selection"
    return arr_type

"""
This function sets all buttons (except for the button that was pressed) back to the default color. 
"""
def change_back():
    if not merge.hovering():
        merge.color = (255, 255, 255)
    if not quick.hovering():
        quick.color = (255, 255, 255)
    if not bubble.hovering():
        bubble.color = (255, 255, 255)
    if not insertion.hovering():
        insertion.color = (255, 255, 255)
    if not selection.hovering():
        selection.color = (255, 255, 255)

"""
This function sets the sorting object's algorithm based off the most recent sorting algorithm selection.
The algorithm will be implemented onto the array when the start button is pressed.
"""
def create_sorting(obj, arr_type, arr, draw_screen, speed):
    speed = speed + 5
    if arr_type == "merge":
        obj.merge_sort(0, len(arr), arr, draw_screen, speed)
    elif arr_type == "quick":
        obj.quick_sort(0, len(arr) - 1, arr, draw_screen, speed)
    elif arr_type == "bubble":
        obj.bubble_sort(arr, draw_screen, speed)
    elif arr_type == "selection":
        obj.selection_sort(arr, draw_screen, speed)
    elif arr_type == "insertion":
        obj.selection_sort(arr, draw_screen, speed)


"""
This function draws all aspects of the screen including: 
- Title Bar
- Buttons
- Slider
- Current list/array 
"""
def draw_screen(arr, swap1=None, swap2=None, err=None):
    DSP.fill((255, 240, 240))

    # Drawing the title bar
    pygame.draw.rect(DSP, (0, 0, 0), pygame.Rect(0, 0, WIDTH, 150))
    pygame.draw.rect(DSP, (17, 57, 83), pygame.Rect(1, 1, WIDTH - 2, 148))

    txt = font.render("Select Sorting", True, (255, 255, 255))
    DSP.blit(txt, (25, 35))
    txt = font.render("Algorithm: ", True, (255, 255, 255))
    DSP.blit(txt, (25, 50))

    # Drawing the Buttons
    merge.draw_button()
    quick.draw_button()
    bubble.draw_button()
    insertion.draw_button()
    selection.draw_button()
    start.draw_button()
    create.draw_button()

    # Drawing the Slider
    txt = font.render("Array Size:", True, (255, 255, 255))
    DSP.blit(txt, (27, 118))
    pygame.draw.rect(DSP, (105, 105, 105), pygame.Rect(125, 122, 300, 5))
    pygame.draw.circle(DSP, (0, 0, 0), (arr_size.x, arr_size.y), 10)
    txt = font.render(str(arr_size.return_num()), True, (0, 0, 0))
    DSP.blit(txt, (arr_size.x - 15, arr_size.y - 30))

    # Drawing Speed
    txt = font.render("Sorting speed:", True, (255, 255, 255))
    DSP.blit(txt, (500, 118))
    pygame.draw.rect(DSP, (105, 105, 105), pygame.Rect(615, 122, 300, 5))
    pygame.draw.circle(DSP, (0, 0, 0), (sort_speed.x, sort_speed.y), 10)

    # Drawing Errors
    if err:
        txt = font.render("Error: Create New", True, (255, 0, 0))
        DSP.blit(txt, (900, 40))
        txt = font.render("Unsorted Array", True, (255, 0, 0))
        DSP.blit(txt, (900, 55))

    # Drawing the Array
    for i in range(len(arr)):
        x_loc = i * (WIDTH / len(arr))
        rect_width = (WIDTH / len(arr))
        rect_height = (arr[i] * (((3 / 4) * HEIGHT) / max(arr)))
        pygame.draw.rect(DSP, (255, 255, 255), pygame.Rect(x_loc, 150, rect_width, rect_height))
        if i == swap1:
            pygame.draw.rect(DSP, (200, 0, 0), pygame.Rect(x_loc, 150, rect_width, rect_height))
        elif i == swap2:
            pygame.draw.rect(DSP, (0, 200, 0), pygame.Rect(x_loc, 150, rect_width, rect_height))
        else:
            pygame.draw.rect(DSP, (44, 118, 171), pygame.Rect(x_loc, 150, rect_width - 1, rect_height - 1))

    pygame.display.update()

"""
This function checks if an array is sorted.
"""
def check_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

"""
This function registers mouse input to drag the slider. It alters the slider's x-positioning
based off where the User drags the slider.
Allows for list/array values between 0 and 300.
"""
def drag_slider(event, drag, slider, type):
    # Slider controls
    if event.type == pygame.MOUSEBUTTONDOWN and slider.hovering():
        drag = True
    if event.type == pygame.MOUSEBUTTONUP:
        drag = False
    if event.type == pygame.MOUSEMOTION:
        pos = pygame.mouse.get_pos()
        if ((type == 0 and (pos[0] > 130 and pos[0] < 425)) \
                or (type == 1 and (pos[0] > 616 and pos[0] < 914))) and drag:
            slider.x = pos[0]
    return drag

"""
Main Function - Runs the Pygame application
"""
def main():
    clock = pygame.time.Clock()
    run = True
    drag_arr = False
    drag_speed = False

    # Creating array and algorithm object
    arr = [random.randint(1, 100) for i in range(100)]
    arr_type = ""
    obj = algorithms.Algos("")
    speed = 75
    err = False
    # Draws initial screen
    draw_screen(arr)
    while run:
        clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Registers User Interaction
            arr_type = click(event, arr_type)
            drag_arr = drag_slider(event, drag_arr, arr_size, 0)
            drag_speed = drag_slider(event, drag_speed, sort_speed, 1)
            draw_screen(arr, err=err)

            # Alters the array relative to the slider value/location
            pos = pygame.mouse.get_pos()
            if drag_arr and pos[0] > 130 and pos[0] < 425:
                arr = [random.randint(1, 100) for i in range(arr_size.return_num())]
            elif drag_speed and pos[0] > 615 and pos[0] < 914:
                speed = sort_speed.return_num()

            # Creates new array on "Create Array" Button input
            if event.type == pygame.MOUSEBUTTONDOWN and create.hovering():
                arr = [random.randint(1, 100) for i in range(arr_size.return_num())]

            # Starts sorting when start button is pressed (if the list isn't already sorted)
            if event.type == pygame.MOUSEBUTTONDOWN and start.hovering():
                if not check_sorted(arr):
                    create_sorting(obj, arr_type, arr, draw_screen, speed)
                    err = False
                    draw_screen(arr, err=False)
                else:
                    err = True
    pygame.quit()

if __name__ == '__main__':
    main()