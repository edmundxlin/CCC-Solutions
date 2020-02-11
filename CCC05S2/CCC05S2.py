def moveto(x, y, screen):
    if x + y > screen:
        x = screen
    elif x + y < 0:
        x = 0
    else:
        x += y
    return x
        
screensize = input().split(" ")
x = 0
y = 0
while True:
    moves = input()
    if moves == "0 0":
        break
    else:
        move = moves.split(" ")
        x = moveto(x, int(move[0]), int(screensize[0]))
        y = moveto(y, int(move[1]), int(screensize[1]))
        print(str(x) + " " + str(y))