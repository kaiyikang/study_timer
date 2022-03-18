#!/opt/homebrew/Caskroom/miniforge/base/envs/myenv/bin/python
from datetime import datetime, timedelta
from turtle import st


def main():
    # initial
    state = False
    total_time = timedelta()
    today_file = datetime.now().strftime("%Y-%b-%d")
    file = open('%s.txt'%(today_file), 'a+')

    print("Hello, This is study timer.\nPlease enter 'return' to start, or any key to stop!\n")

    # Start to loop
    while True:

        # Timer start
        userInput = input(">>> Do you want to start? ")
        if userInput == "":
            state = True
            begin_time = datetime.now()
            begin_time_str = begin_time.strftime("%H:%M:%S")

            # write to file
            print("(%s) Begin......"%(begin_time_str),end=" ")
            file.write(">>> %s \n"%(begin_time_str))
        else:
            break

        # Time end
        userInput = input()
        if userInput == "":
            
            state = False
            end_time = datetime.now()
            end_time_str = end_time.strftime("%H:%M:%S")

            # write to file
            print("(%s) End!\n"%(end_time_str))
            file.write( "<<< %s\n"%(end_time_str))

            total_time += ( end_time - begin_time )
        else:
            break

    # summary
    # if state is still on, need to calculate the final total time
    if state: 
        # do the rest 
        end_time = datetime.now()
        end_time_str = end_time.strftime("%H:%M:%S")

        # write to file
        print("(%s) End!"%(end_time_str))
        file.write( "%s\n"%(end_time_str))

        total_time += ( end_time - begin_time )

    # summary
    file.write("==========\nTotal_time:")
    file.write(str(total_time)[0:-7] + '\n')
    file.close()
    
if __name__ == "__main__":
    main()

