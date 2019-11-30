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