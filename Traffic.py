import time

RED_TIME = 30
YELLOW_TIME = 5
GREEN_TIME = 30


def countdown(duration, message):
    for i in range(duration, 0, -1):
        print(f"{message} | Time Remaining: {i} seconds", end="\r")
        time.sleep(1)
    print("\n") 


def traffic_light_system(start_light):
    start_light = start_light.lower()

    while True:
        if start_light == "red":
            countdown(RED_TIME, "🔴 Red Light is ON. Must not move!")
            start_light = "green"

        elif start_light == "green":
            countdown(GREEN_TIME, "🟢 Green Light is ON. You can move now!")
            start_light = "yellow"

        elif start_light == "yellow":
            countdown(YELLOW_TIME, "🟡 Yellow Light is ON. Ready to move!")
            start_light = "red"

        else:
            print("❌ Invalid input! Please enter red, yellow, or green.")
            break


user_input = input("Enter starting light (red / yellow / green): ")
traffic_light_system(user_input)