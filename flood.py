import time
import pyautogui as pg

i = 0
n = int(input("Enter the number of times you want to spam: "))
msg = input("Enter the message you want to spam: ")
print("Starting in 5 seconds...")
time.sleep(5)


while i < n:
    pg.typewrite(msg)
    pg.press("enter")
    i += 1
    print(f"Message sent `{i}` times")
