import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print("Starting %s \n" % name)
    time.sleep(3)
    print("Exiting %s \n" % name)


if __name__ == '__main__':
    background_process = multiprocessing.Process \
        (name='background_process', \
         target=foo)
    background_process.daemon = True

    NO_background_process = multiprocessing.Process \
        (name='NO_background_process', \
         target=foo)
    time.sleep(10)
    NO_background_process.daemon = False

    background_process.start()
    NO_background_process.start()