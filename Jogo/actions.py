import curses

def verify_exit(entrada):
    if entrada == "/exit":
        return True
    return False

def verify_back(entrada):
	if entrada ==  "/back":
		return True
	return False

def verify_next(entrada):
	if entrada == "/next":
		return True
	return False

def verify_giveup(entrada):
    if entrada in [71, 103]:
        return True
    return False

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