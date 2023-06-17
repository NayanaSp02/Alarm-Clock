import datetime
import random
import winsound
import threading

stop_alarm_flag = threading.Event()  # Event to stop the alarm sound

def generate_question():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*','/'])
    question = f"What is {num1} {operator} {num2}? "
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        answer=num1/num2
    return question, answer

def stop_alarm():
    question, answer = generate_question()
    user_answer = int(input(question))
    if user_answer == answer:
        print("Congratulations! You solved the math question correctly.")
        stop_alarm_flag.set()  # Set the event to stop the alarm
        return True
    else:
        print("Oops! That's incorrect. Try again.")
        return False

def play_alarm_sound():
    frequency = 4500  # Set frequency (Hz)
    duration = 1000  # Set duration (ms)
    while not stop_alarm_flag.is_set():  # Check if the event is set
        winsound.Beep(frequency, duration)

def set_alarm():
    alarm_time = input("Enter the alarm time in HH:MM format: ")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("Time to wake up!")
            alarm_thread = threading.Thread(target=play_alarm_sound)
            alarm_thread.start()
            if stop_alarm():
                break

# Main program
set_alarm()
