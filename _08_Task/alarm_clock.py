from pygame import mixer
import time
import datetime

mixer.init()
print("Welcome to Alarm Clock")
print("""Select your alarm tone
1. mtarek_naat
2. tab tabi tab""")
alarm_tone = input("Enter (1/2): ")
if alarm_tone == '1':
    tone = "mtarek_naat.mp3"
elif alarm_tone == '2':
    tone = "tab_tabi_tab.mp3"
else:
    print("Invalid input")

mixer.music.load(tone)
mixer.music.set_volume(0.7)

def play_alarm():
    hours = int(input("Enter the hours: "))
    minutes = int(input("Enter the minutes: "))
    alarm_time = datetime.datetime.now().replace(hour=hours, minute=minutes, second=0, microsecond=0)
    # Get the current time and set the alarm time
    
    print("Waiting...")
    while True:
        current_time = datetime.datetime.now()
        # Get the current time
        
        if current_time >= alarm_time:
            # Check if the current time is greater than or equal to the alarm time
            mixer.music.play()
            print("Wake up!")  # Print "Wake up!" to the console

            time.sleep(10)  # Wait for 10 seconds

            print("Press 's' to snooze after 1 minute")
            print("Press 'e' to exit the program")
            query = input(" ")

            if query == 's':
                mixer.music.stop()
                alarm_time = alarm_time + datetime.timedelta(minutes=1)
                print("Snoozed after 1 minute of set timer")
            elif query == 'e':
                mixer.music.stop()
                break
        
        else:
            time.sleep(1)  # Wait for 1 second before checking the time again

play_alarm()  # Call the play_alarm() function to start the alarm clock

print(datetime.datetime.now())