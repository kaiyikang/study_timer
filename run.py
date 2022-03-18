#!/opt/homebrew/Caskroom/miniforge/base/envs/myenv/bin/python
from datetime import datetime, timedelta

from pynput import keyboard 

def on_press(key):
    global STATE
    global study_time
    global begin_time

    # get key
    try:
        k = key.char
    except:
        k = key.name

    # make up today file
    today = datetime.now().strftime("%Y-%b-%d")

    if k == "enter":
        with open(today+'.txt', 'a+') as f:
            # Get now
            time_now = datetime.now()
            now = time_now.strftime("%H:%M:%S")
            
            if not STATE:
                flag = '>>> '
                print("(%s) Begin..."%(now))
                STATE = True
                begin_time = time_now
            else:
                flag = ''
                print("(%s) End!"%(now))
                STATE = False
                # calculate total time
                study_time += (time_now - begin_time)

            # Write to file
            f.write(flag + now+'\n')
    
    # stop the listener
    if key == keyboard.Key.esc:
        print("Close the timer now")
        
        with open(today+'.txt', 'a+') as f:
            if not STATE: # If the task is done, save it
                f.write("==================\n")
                f.write("Total study time: \n"+ str(study_time))
            else: # Make sure task is done
                # Get end time
                time_now = datetime.now()
                now = time_now.strftime("%H:%M:%S")
                f.write("" + now+'\n')
                study_time += (time_now - begin_time)
                f.write("==================\n")
                f.write("Total study time: \n"+ str(study_time))
                

        return False

if __name__ == "__main__":

    # inital 
    STATE = False
    study_time = timedelta()
    listener = keyboard.Listener(on_press=on_press)
    
    # start
    listener.start()
    listener.join() # remove

