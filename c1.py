from pynput import keyboard, mouse 
import datetime

#-----------------------Global variables--------------------------
current_x = 0
current_y = 0
ctrl_pressed= False

#references to listeners 
listener_keyboard = None
listener_mouse = None

log_file = open("activity_log.txt", "w")


#-----------------helper function-----------------
def log(message):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
    line = f"[{timestamp}] {message}\n"
    print(line, end="")
    log_file.write(line)
    log_file.flush()                

#--------------------Stop function----------------------------
def stop_all():
    log_file.flush()
    log_file.close()
    if listener_mouse:
        listener_mouse.stop()
    if listener_keyboard:
        listener_keyboard.stop()
        
#------------------------------Mouse Functions-----------------------------
def on_move(x,y):
    global current_x, current_y
    current_x = x
    current_y = y

    log('Pointer moved to {0}'.format((current_x, current_y)))      


def on_click(x, y, button, pressed):

    log('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    if not pressed:
        log('Latest live coordinates:{0}'.format((x,y)))
    
    
def on_scroll(x, y, dx, dy):                
    log('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x,y)))


#-----------------------------keyboard functions---------------------
def on_press(key):
    global ctrl_pressed

    if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
        ctrl_pressed = True

    try:
        key_name = key.char     
    except AttributeError:
        key_name = str(key)         

    log('Key pressed {0}'.format(key_name))

    #stop on ctrl+k
    if ctrl_pressed:
        try:
            if key.char == 'k':
                log('ctrl+k detected - stopping all listeners')
                stop_all()
        except AttributeError:
            pass                    

def on_release(key):
    global ctrl_pressed

    if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
        ctrl_pressed = False

    log('{0} released'.format(key))


#continuous listening 
#-----------------------Mouse Listening Threads---------------------- 
listener_mouse= mouse.Listener(
    on_move = on_move,
    on_click = on_click,
    on_scroll = on_scroll )
listener_mouse.start()

#------------------------Keyboard Listening Threads------------------
listener_keyboard = keyboard.Listener(
    on_press = on_press,
    on_release = on_release )
listener_keyboard.start()

log("Session started. Press ctrl+k to stop")

listener_keyboard.join()
listener_mouse.join()

print("Session ended. Log saved to activity_log.txt")
