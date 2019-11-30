import curses

def verify_exit(entrada):
    if entrada == "/exit" or entrada in [69, 101]:
        return True
    return False

def verify_back(entrada):
	if entrada in [66, 98]:
		return True
	return False

def verify_next(entrada):
	if entrada in [78, 110]:
		return True
	return False

def verify_giveup(entrada):
    if entrada in [71, 103]:
        return True
    return False

def verify_0_ou_1(entrada):
    if entrada == "1":
        return True
    elif entrada == "0":    
        return False
    else:
        return 'erro'

def verify_which_question(entrada):
    if entrada == 49:
        return 1

    elif entrada == 50:
        return 2

    elif entrada == 51:
        return 3

    elif entrada == 52:
        return 4

    elif entrada == 53:
        return 5

    elif entrada == 54:
        return 6

    elif entrada == 55:
        return 7

    elif entrada == 56:
        return 8

    return -1

def keyboard(entrada):
    if entrada == curses.KEY_UP:
        return 'up'

    elif entrada == curses.KEY_DOWN:
        return 'down'

    elif entrada == curses.KEY_RIGHT:
        return 'right'

    elif entrada == curses.KEY_LEFT:
        return 'left'

    elif entrada == curses.KEY_ENTER or entrada in [10,13]:
        return 'enter'