import pygame as py
from datetime import datetime
import time
#Project by David Ribeiro
backgroundcolor = (210, 210, 210)
displaywin = py.display.set_mode((550, 600))

grid = [
    [1, 0, 0, 0, 9, 0, 0, 4, 0],
    [0, 0, 0, 1, 0, 0, 7, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 5, 0],
    [0, 4, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 2, 0],
    [0, 9, 0, 0, 0, 0, 8, 0, 0],
    [0, 0, 2, 0, 0, 6, 0, 0, 0],
    [0, 7, 0, 0, 3, 0, 0, 0, 0]
]
dummygrid= [
    [1, 0, 0, 0, 9, 0, 0, 4, 0],
    [0, 0, 0, 1, 0, 0, 7, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 5, 0],
    [0, 4, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 2, 0],
    [0, 9, 0, 0, 0, 0, 8, 0, 0],
    [0, 0, 2, 0, 0, 6, 0, 0, 0],
    [0, 7, 0, 0, 3, 0, 0, 0, 0]
]
oddevengrid= [
    [0, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 2, 0, 0, 2, 0, 0, 2, 0],
    [1, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 2, 0, 0, 2, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 0, 2, 0],
    [2, 0, 0, 2, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 2, 0, 0, 2],
    [0, 2, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 2, 0, 0, 2, 0, 0]
]
#I've had some serious trouble trying to get the game loading function to work. I understand file input and output
#works, but can't seem to get it to work with my code. I can however, save my current game to a TXT file, as sent
#annexed with the .py file
#
#with open('Sudoku.txt', 'r') as data_file:
#   lines = str(data_file.readlines()).split('\n')
#   grid = list(lines[0:8])
#   dummygrid = list(lines[9:19])
#   oddevengrid = list(lines[19:29])
#   print(grid)

#global variables
x = 0
y = 0
xpos = 0
ypos = 0
py.init()
introfont1 = py.font.SysFont('arialblack', 23)
introfont2 = py.font.SysFont('arialblack', 40)
controlsfont = py.font.SysFont('arial', 25)
boardfont = py.font.SysFont('arialblack', 35)
textfont = py.font.SysFont('arial', 22)
displaywin.fill(backgroundcolor)
py.display.update()

#Game introduction and controls
def intro():
    introtext1 = introfont1.render("Welcome to group 300 Odd/Even Sudoku!", True, (20, 20, 20))
    introtext2 = introfont2.render("Press any key to start!", True, (20, 20, 20))
    controlstext = introfont1.render(" Controls:", True, (20, 20, 20))
    controlstext1 = controlsfont.render("- Arrow keys: Move selection box", True, (70, 70, 100))
    controlstext2 = controlsfont.render("- Numbers 1 to 9: Input value in empty cell", True, (70, 70, 100))
    controlstext3 = controlsfont.render("- X Key: Close the game", True, (70, 70, 100))
    controlstext4 = controlsfont.render("- Z Key: Save the game board", True, (70, 70, 100))
    controlstext5 = controlsfont.render("- E Key: Erase a value", True, (70, 70, 100))
    controlstext6 = controlsfont.render("- P Key: Pause the game", True, (70, 70, 100))
    controlstext7 = controlsfont.render("- L Key: Load game from txt file", True, (70, 70, 100))
    displaywin.blit(introtext1, (20, 120))
    displaywin.blit(introtext2, (30, 220))
    displaywin.blit(controlstext, (30, 350))
    displaywin.blit(controlstext1, (30, 387))
    displaywin.blit(controlstext2, (30, 417))
    displaywin.blit(controlstext3, (30, 447))
    displaywin.blit(controlstext4, (30, 477))
    displaywin.blit(controlstext5, (30, 507))
    displaywin.blit(controlstext6, (30, 537))
    displaywin.blit(controlstext7, (30, 566))
    py.display.update()
    return

#Helper below the game board
def helper():
    helpertext2 = textfont.render("Empty cells with the letter e must contain even numbers,", True, (0, 0, 0))
    helpertext3 = textfont.render("Empty cells with the letter o must contain odd numbers.", True, (0, 0, 0))
    displaywin.blit(helpertext2, (50, 520))
    displaywin.blit(helpertext3, (55, 550))
    return

#Quality of life function to redraw elements superimposed when moving the selector box
def redraw():
    board_divider()
    board_oddeven()
    board_num()
    return board_divider(), board_oddeven(), board_num()

#Game loading function
def game_load():
    data_file = open('Sudoku.txt', 'r')
    global grid
    grid = list(data_file.readline())
    global dummygrid
    dummygrid = list(data_file.readline())
    global oddevengrid
    oddevengrid = list(data_file.readline())
    timestamp = data_file.readline()
    print(timestamp)
    timesave = data_file.readline()
    timenumb = [int(word) for word in timesave.split() if word.isdigit()]
    global time
    time = timenumb


#Function to project the GUI of the board
def board_divider():
    py.display.set_caption("Sudoku by group 300")
    for i in range(10):
        py.draw.line(displaywin, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        py.draw.line(displaywin, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
        if i % 3 == 0:
            py.draw.line(displaywin, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            py.draw.line(displaywin, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)
    return

#Function that marks cells for odd or even rules using a dummy function oddevengrid to map their locations
def board_oddeven():
    for x in range(0, 9):
        for y in range(0, 9):
            if oddevengrid[x][y] == 1:
                num = boardfont.render(str("o"), True, (180, 180, 200))
                displaywin.blit(num, ((x + 1) * 50 + 15, (y + 1) * 49.7))
            if oddevengrid[x][y] == 2:
                num = boardfont.render(str("e"), True, (220, 180, 180))
                displaywin.blit(num, ((x + 1) * 50 + 15, (y + 1) * 49.7))
    return

#Function that populated the game board's cells with numbers, distinguishing pre-existing and input numbers
def board_num():
    for x in range(0, 9):
        for y in range(0, 9):
            prenum = boardfont.render(str(grid[x][y]), True, (70, 70, 180))
            inputnum = boardfont.render(str(grid[x][y]), True, (0, 0, 0))
            if grid[x][y] != 0:
                if dummygrid[x][y] == grid[x][y]:
                    displaywin.blit(prenum, ((y + 1) * 50 + 15, (x + 1) * 50))
                else:
                    displaywin.blit(inputnum, ((y + 1) * 50 + 15, (x + 1) * 50))
    return

#Function that checks whether a number is pre-existing or not by compring grid with an unaltered dummy grid
def exist_rule():
    existcheck = grid[ypos][xpos] == 0 or grid[ypos][xpos] != dummygrid[ypos][xpos]
    return existcheck

#Function with all the error flags
def error_flags():
    exist_error_flg = False
    input_error_flg = False
    rowrepeat_error_flg = False
    colrepeat_error_flg = False
    odd_error_flg = False
    even_error_flg = False
    return

#Function that projects an error message when existcheck in exist_rule() is False
def exist_error():
    py.draw.rect(displaywin, backgroundcolor, (20, 520, 520, 100))
    errortext1 = introfont1.render("Error: Input number values in empty cells", True, (200, 0, 0))
    displaywin.blit(errortext1, (17, 530))
    return

#Function that projects an error message when someone tries to press an invalid character
def input_error():
    py.draw.rect(displaywin, backgroundcolor, (20, 530, 520, 100))
    errortext2 = introfont1.render("Error: Please input a valid character", True, (200, 0, 0))
    displaywin.blit(errortext2, (47, 530))
    return

#Function that projects an error message when an error related to odd cells is found, and also replaces the erroneous input
# values with 0 as with other functions below
def odd_error():
    py.draw.rect(displaywin, backgroundcolor, (20, 515, 500, 47))
    errortext3 = introfont1.render("Error: Input an odd value in 'o' cells", True, (200, 0, 0))
    if grid[ypos][xpos] == 0:
        pass
    else:
        grid[ypos][xpos] = 0
    displaywin.blit(errortext3, (50, 515))
    return

#Function that projects an error message when an error related to even cells is found
def even_error():
    py.draw.rect(displaywin, backgroundcolor, (20, 546, 500, 50))
    errortext4 = introfont1.render("Error: Input an even value in 'e' cells", True, (200, 0, 0))
    if grid[ypos][xpos] == 0:
        pass
    else:
        grid[ypos][xpos] = 0
    displaywin.blit(errortext4, (45, 546))
    return

#Function that projects an error message when an error related to repeats in rows is found
def rowrepeat_error():
    py.draw.rect(displaywin, backgroundcolor, (20, 505, 500, 40))
    errortext1 = introfont1.render("Error: Number repeated in this row", True, (200, 0, 0))
    displaywin.blit(errortext1, (55, 515))
    errortext5 = boardfont.render(str(grid[ypos][xpos]), True, (200, 0, 0))
    if grid[ypos][xpos] == 0:
        pass
    else:
        grid[ypos][xpos] = 0
    displaywin.blit(errortext5, ((xpos + 1) * 50 + 15, (ypos + 1) * 50))
    return

#Function that projects an error message when an error related to repeats in columns is found
def colrepeat_error():
    error_flags()
    py.draw.rect(displaywin, backgroundcolor, (20, 546, 500, 40))
    errortext6 = introfont1.render("Error: Number repeated in this column", True, (200, 0, 0))
    if grid[ypos][xpos] == 0:
        pass
    else:
        grid[ypos][xpos] = 0
    displaywin.blit(errortext6, (37, 546))
    return

#Function that creates a ticking timer in seconds and projects it unto the gam board
def game_timer():
    global time
    time = py.time.get_ticks() // 1000
    timer = str(time)
    timertext = controlsfont.render(timer, True, (0, 0, 0))
    py.draw.rect(displaywin, backgroundcolor, (250, 10, 80, 30))
    displaywin.blit(timertext, (265, 10))
    py.display.update()
    return timer

#Function that handles pausing the game
def pause():
    game_timer()
    time = game_timer()
    paused = True
    while paused:
        displaywin.fill(backgroundcolor)
        pausetext = introfont2.render("Paused!", True, (0, 0, 0))
        displaywin.blit(pausetext, (180, 210))
        timepaused = int(time) - py.time.get_ticks() // 1000
        py.display.update()
        for event in py.event.get():
            if event.type == py.KEYDOWN:
                if event.key == py.K_p:
                    paused = False

#Function that saves the game as well as elapsed time and date
def game_save():
    game_timer()
    timer = game_timer()
    date = datetime.now()
    data_file = open('Sudoku.txt', 'w')
    data_file.write(str(grid))
    data_file.write('\n')
    data_file.write(str(dummygrid))
    data_file.write('\n')
    data_file.write(str(oddevengrid))
    data_file.write('\n')
    data_file.write('Game saved at: ' + str(date) + '\nElapsed time (in seconds):' + str(timer))

#Function that throws a victory conition when the board is finished and appends completion time and date to a file
def finish_rule():
    timer = game_timer()
    print(timer)
    if error_flags() and all(grid) > 0 and min(grid) != 0:
        displaywin.fill(backgroundcolor)
        wintext = introfont2.render("Game Finished!", True, (0, 0, 0))
        displaywin.blit(wintext, (275, 300))
        date = datetime.now()
        data_file = open('Sudoku.txt', 'a')
        data_file.write('\n')
        data_file.write('Game completed at:' + str(date) + '\nin' + str(timer) + 'seconds!')

#Main loop function containing error checks using flags, conditionals and pygame key press events
def inputs(x, y):
    while True:
        game_timer()
        global xpos
        global ypos
        xpos = x // 50
        ypos = y // 50
        for event in py.event.get():
            exist_error_flg = False
            input_error_flg = False
            rowrepeat_error_flg = False
            colrepeat_error_flg = False
            odd_error_flg = False
            even_error_flg = False
            if event.type == py.KEYDOWN:
                existcheck = exist_rule()
                if existcheck:
                    if event.key in [py.K_1, py.K_2, py.K_3, py.K_4, py.K_5, py.K_6, py.K_7, py.K_8, py.K_9]:
                        grid[ypos][xpos] = int(py.key.name(event.key))
                        if grid[ypos][xpos] % 2 != 0 and oddevengrid[xpos][ypos] == 2:
                            odd_error_flg = True
                        if grid[ypos][xpos] % 2 == 0 and oddevengrid[xpos][ypos] == 1 and grid[ypos][xpos] != 0:
                            even_error_flg = True
                        row = [i for i in grid[ypos] if i == int(py.key.name(event.key))]
                        if len(row) > 1:
                            rowrepeat_error_flg = True
                        for z in range(9):
                            col_invert = [s[z] for s in grid]
                            col = [j for j in col_invert if j == int(py.key.name(event.key))]
                            if len(col) > 1:
                                colrepeat_error_flg = True
                    else:
                        input_error_flg = True
                else:
                    if event.key not in [py.K_UP, py.K_DOWN, py.K_LEFT, py.K_RIGHT, py.K_x, py.K_z, py.K_p, py.K_s, py.K_l]:
                        exist_error_flg = True
                if event.key == py.K_l:
                    game_load()
                if event.key in [py.K_UP, py.K_DOWN, py.K_LEFT, py.K_RIGHT, py.K_x, py.K_z, py.K_p, py.K_s, py.K_l]:
                    if event.key == py.K_UP:
                        if y >= 50:
                            y = y - 50
                    if event.key == py.K_DOWN:
                        if y <= 350:
                            y = y + 50
                    if event.key == py.K_LEFT:
                        if x >= 50:
                            x = x - 50
                    if event.key == py.K_RIGHT:
                        if x <= 350:
                            x = x + 50
                    if event.key == py.K_s:
                        if grid[ypos][xpos] != dummygrid[ypos][xpos]:
                            grid[ypos][xpos] = 0
                            input_error_flg = False
                    if event.key == py.K_z:
                        game_save()
                    if event.key == py.K_p:
                        pause()
                    if event.key == py.K_x:
                        return
                displaywin.fill(backgroundcolor)
                helper()
                redraw()
                if exist_error_flg:
                    exist_error()
                if input_error_flg:
                    if event.key not in [py.K_UP, py.K_DOWN, py.K_LEFT, py.K_RIGHT, py.K_x, py.K_s, py.K_p, py.K_z, py.K_l]:
                        input_error()
                if odd_error_flg:
                    odd_error()
                    errornum4 = boardfont.render(str(py.key.name(event.key)), True, (200, 0, 0))
                    displaywin.blit(errornum4, ((xpos + 1) * 50 + 15, (ypos + 1) * 50))
                if even_error_flg:
                    even_error()
                    errornum5 = boardfont.render(str(py.key.name(event.key)), True, (200, 0, 0))
                    displaywin.blit(errornum5, ((xpos + 1) * 50 + 15, (ypos + 1) * 50))
                if rowrepeat_error_flg:
                    rowrepeat_error()
                    errornum6 = boardfont.render(str(py.key.name(event.key)), True, (200, 0, 0))
                    displaywin.blit(errornum6, ((xpos + 1) * 50 + 15, (ypos + 1) * 50))
                if colrepeat_error_flg:
                    colrepeat_error()
                    errornum7 = boardfont.render(str(py.key.name(event.key)), True, (200, 0, 0))
                    displaywin.blit(errornum7, ((xpos + 1) * 50 + 15, (ypos + 1) * 50))
                py.draw.rect(displaywin, (255, 0, 0), (50 + x, 50 + y, 50, 50), 5)
                finish_rule()
                py.display.update()
            if event.type == py.QUIT:
                return False
intro()
inputs(x, y)
