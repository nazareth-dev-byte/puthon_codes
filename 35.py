# We're going to create a working alarm in python.

import time  # To update our clock every second
import datetime
# To work with sound effects, we have to
import pygame


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "alarmsound.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)

        if current_time == alarm_time:
            print("Wake up!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            # Mixer is a module in pygame that allows us to play sound effects

            is_running = False

        time.sleep(1)
    # Replace with the path to your alarm sound file


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time(HH:MM:SS): ")
    set_alarm(alarm_time)
