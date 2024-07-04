import time

def show_loading_screen(duration):
    print("Loading", end="")
    for _ in range(duration):
        print(".", end="")
        time.sleep(1)
    print(" Done.")
