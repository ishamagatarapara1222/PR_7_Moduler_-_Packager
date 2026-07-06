import datetime
import time


def display_current_datetime():
    now = datetime.datetime.now()
    print(f"Current Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")


def calculate_difference(date1_str, date2_str):
    fmt = "%Y-%m-%d"
    d1 = datetime.datetime.strptime(date1_str, fmt)
    d2 = datetime.datetime.strptime(date2_str, fmt)
    diff = abs((d2 - d1).days)
    print(f"Difference: {diff} days")


def format_date(date_str, custom_format):
    fmt = "%Y-%m-%d"
    d = datetime.datetime.strptime(date_str, fmt)
    print(f"Formatted Date: {d.strftime(custom_format)}")


def stopwatch():
    print("Stopwatch started. Press Enter to stop...")
    start = time.time()
    input()
    end = time.time()
    elapsed = end - start
    print(f"Elapsed Time: {elapsed:.2f} seconds")


def countdown_timer(seconds):
    print(f"Countdown Timer: {seconds} seconds")
    for i in range(seconds, 0, -1):
        print(f"  {i}...", end="\r")
        time.sleep(1)
    print("Time's up!")
