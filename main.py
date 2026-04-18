import threading
import time

def vazifa1():
    for i in range(5):
        print("Vazifa 1:", i)
        time.sleep(1)

def vazifa2():
    for i in range(5):
        print("Vazifa 2:", i)
        time.sleep(1)

def vazifa3():
    for i in range(5):
        print("Vazifa 3:", i)
        time.sleep(1)

vazifa1_thread = threading.Thread(target=vazifa1)
vazifa2_thread = threading.Thread(target=vazifa2)
vazifa3_thread = threading.Thread(target=vazifa3)

vazifa1_thread.start()
vazifa2_thread.start()
vazifa3_thread.start()

vazifa1_thread.join()
vazifa2_thread.join()
vazifa3_thread.join()