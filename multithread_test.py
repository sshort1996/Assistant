import functools
import threading

def run_in_threads(*functions):
    threads = []

    for function in functions:
        thread = threading.Thread(target = function)
        thread.daemon = True
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

def __print_infinite_loop(value, event):
    while not event.is_set():
        print(value)

def __print_my_value_n_times(value, n, event):
    for i in range(n):
        print(value)
    event.set()

if __name__ == "__main__":
    event = threading.Event()
    infinite_loop = functools.partial(__print_infinite_loop, "xyz", event)
    my_values = functools.partial(__print_my_value_n_times, "123", 5, event)
    run_in_threads(infinite_loop, my_values)