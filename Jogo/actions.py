def verify_exit(entrada):
    if entrada == "/exit":
        return True
    return False

def verify_back(entrada):
	if entrada ==  "/back":
		return True
	return False

def verify_next(entrada):
	if entreada == "/next":
		return True
	return False

def keyboard_actions(entrada):
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