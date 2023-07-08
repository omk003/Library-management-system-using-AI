import keyboard
import threading
import time
import sys

def barcode_listener():
    barcode = ""
    last_activity_time = time.time()
    exit_event = threading.Event()

    def check_activity():
        nonlocal last_activity_time
        while not exit_event.is_set():
            if time.time() - last_activity_time > 3:
                print("No keyboard activity for 3 seconds. Terminating the program...")
                exit_event.set()
                sys.exit()
            time.sleep(0.1)

    activity_thread = threading.Thread(target=check_activity)
    activity_thread.start()

    while not exit_event.is_set():
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            last_activity_time = time.time()
            key = event.name
            if key == "enter":
                print("Barcode:", barcode)
                barcode = ""
            else:
                barcode += key

    activity_thread.join()

barcode_listener()
