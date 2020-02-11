def moveto(current, x, y, screenx, screeny):

    if current[0] + x > screenx or current[0] + x < 0 or current[1] +y > screeny or current[1]+y < 0:

        if current[0] + x > screenx:
            current[0] += screenx-current[0]
            if current[1] + y > screeny:
                current[1] += screeny-current[1]
                return current
            elif current[1] +y < 0:
                current[1]-=current[1]
                return current
            else:
                current[1] += y
                return current
        elif current[0] +x < 0:
            current[0] -= current[0]
            if current[1] + y > screeny:
                current[1] += screeny-current[1]
                return current
            elif current[1] +y < 0:
                current[1]-=current[1]
                return current
            else:
                current[1] += y
                return current

        if current[1] + y > screeny:
            current[1] += screeny-current[1]
            if current[0] + x > screenx:
                current[0] += screenx-current[0]
                return current
            elif current[0] +x < 0:
                current[0]-=current[0]
                return current
            else:
                current[0] += x
                return current
        elif current[1] +y< 0:
            current[1] -= current[1]
            if current[0] + x > screenx:
                current[0] += screenx-current[0]
                return current
            elif current[0] +x < 0:
                current[0]-=current[0]
                return current
            else:
                current[0] += y
                return current
    else:
        current[0] += x
        current[1] += y

    return current
        
screensize = input().split(" ")
mousepos = [0,0]
while True:
    moves = input()
    if moves == "0 0":
        break
    else:
        move = moves.split(" ")
        mousepos = moveto(mousepos, int(move[0]), int(move[1]), int(screensize[0]), int(screensize[1]))
        print(str(mousepos[0]) + " " + str(mousepos[1]))