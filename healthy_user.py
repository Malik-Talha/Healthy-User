"""
every 45 minutes, an alarm should ring to go and drink the water
    and move your body
every 15 minutes, an alarm should ring to do eyes movement

"""
import time
import os

def clrscr():
    """ clear console screen """
    os.system('cls')


def ring_the_alarm(string, file):
    """ To play the given audio file name and print the given string """
    # using "mixer" module from "pygame"
    from pygame import mixer
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(10)
    # clear mixer credit output
    clrscr()
    print(string)
    while True:
        music = input("Enter 's' to stop the alarm or 'q' to quit: ")
        if music == 's' or music == 'S':
            mixer.music.stop()
            break
        elif music == 'q' or music == 'Q':
            print("Thanks for coming!")
            time.sleep(2.0)
            exit()
        else:
            print("Invalid input!")

def start_alarm(water_time, eyes_time, water_alarm_file, eyes_alarm_file):
    import time
    # starting time
    init_water_time = time.time()
    init_eyes_time = time.time()

    # To continue this process forever, enclosing the whole process in loop
    while True:
        # calculating and storing time for use in conditions
        water_time_up = int(time.time() - init_water_time)
        eyes_time_up = int(time.time() - init_eyes_time)

        clrscr()
        # print time remaining
        print(f"Drink Water after:\t\t{(water_time-water_time_up)//60}:{60 - (int(water_time_up)%60)} minutes")
        print(f"Move eyes after:\t\t{(eyes_time-eyes_time_up)//60}:{60 - (int(eyes_time_up)%60)} minutes")
        
        # stope program for 1 sec to for better console output
        time.sleep(1)

        # if the calculated time is up than required time to start, then ringing the alarm
        if water_time_up > water_time:
            string = "Time to drink a glass of water and do some body movement!"
            init_water_time = time.time()
            ring_the_alarm(string, water_alarm_file)
            

        if eyes_time_up > eyes_time:
            string = "Time to do eye movement!"
            init_eyes_time = time.time()
            ring_the_alarm(string, eyes_alarm_file)
            


if __name__ == '__main__':

    print("Welcome to the healthy programmer system created by Talha Murtaza.")
    print("\nThe alarm for water will ring after every 45 minutes")
    print("The alarm for eye movement will ring after every 15 minutes\n\noptions:")
    # default total time (in seconds) after the alarm should ring
    water_time = 45 * 60  # 45 minutes
    eyes_time = 15 * 60  # 15 minutes

    # default ringtone file names
    water_alarm_file = "file1.mp3"
    eyes_alarm_file = "file2.mp3"
    while True:
        print("1. To start. ")
        print("2. To change water alarm time. ")
        print("3. To change eyes-movement alarm time. ")
        print("4. To change the water alarm ringtone. ")
        print("5. To change the eyes movement alarm ringtone. ")
        print("6. To exit. ")
        choice = int(input())

        if choice == 1:
            if water_alarm_file in os.listdir() and eyes_alarm_file in os.listdir():
                start_alarm(water_time, eyes_time, water_alarm_file, eyes_alarm_file)
            else:
                clrscr()
                print("No ringtone file(s)\nPlease change the ringtones from menu.")
                input()
        elif choice == 2:
            clrscr()
            time = int(input("Enter the new time in minutes: "))
            water_time = time * 60
            print("The new alarm time has been set successfully!\n")
            input()

        elif choice == 3:
            clrscr()
            time = int(input("Enter the new time in minutes: "))
            eyes_time = time * 60
            print("The new alarm time has been set successfully!\n")
            input()

        elif choice == 4:
            clrscr()
            print("Warning! Before entering the name of file including"
                  "its extension, please make sure that the file is available in "
                  "the healthy programmer system's directory.")
            print("\n")
            name = input("Enter the name of audio file including extension: ")
            if name in os.listdir():
                water_alarm_file = name
                print("Alarm ringtone has been changed successfully!")
                input()
            else:
                print("No such file exists in the directory!")
                input()
        elif choice == 5:
            clrscr()
            print("Warning! Before entering the name of file with include"
                  "its extension, please make sure that the file is available in "
                  "the healthy programmer system's directory.")
            print("\n")
            name = input("Enter the name of audio file including extension: ")
            if name in os.listdir():
                eyes_alarm_file = name
                print("Alarm ringtone has been changed successfully!")
                input()
            else:
                print("No such file exists in the directory!")
                input()
        elif choice == 6:
            exit()
        clrscr()
        