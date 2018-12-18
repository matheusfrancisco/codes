from builtins import TypeError, ValueError, SystemError, hasattr, AssertionError, SystemExit
import ctypes
import inspect
from threading import Thread, Timer
import threading
import random


class watchdogTimeoutException(Exception):
    pass
       

def _async_raise(tid, exctype):
    """Raises an exception in the threads with id tid"""
    if not inspect.isclass(exctype):
        raise TypeError("Only types can be raised (not instances)")
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(tid), ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # "if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, 0)
        raise SystemError("PyThreadState_SetAsyncExc failed")


class Watchdog(object):
    def __init__(self, timeout, thread):  # timeout in seconds
        self.timeout = timeout
        self.timer = Timer(self.timeout, self.handler)
        self.thread = thread

    def start(self):
        self.timer.start()

    def reset(self):
        self.timer.cancel()
        self.timer = Timer(self.timeout, self.handler)
        self.timer.start()

    def stop(self):
        self.timer.cancel()

    def handler(self):  # é chamado caso esgote o tempo.
        self.thread.quit()




class ThreadWithExc(threading.Thread):
    def _get_my_tid(self):
        """determines this (self's) thread id"""
        if not self.isAlive():
            raise threading.ThreadError("the thread is not active")

        # do we have it cached?
        if hasattr(self, "_thread_id"):
            return self._thread_id

        # no, look for it in the _active dict
        for tid, tObj in threading._active.items():
            if tObj is self:
                self._thread_id = tid
                return tid

        raise AssertionError("could not determine the thread's id")

    def raise_exc(self, exctype):
        """raises the given exception type in the context of this thread"""
        _async_raise(self._get_my_tid(), exctype)

    def quit(self):
        """raises SystemExit in the context of the given thread, which should
        cause the thread to exit silently (unless caught)"""
        self.raise_exc(SystemExit)

    '''A thread class that supports raising exception in the thread from
       another thread.
    '''


def functionInfinita():
    while True:
        print('n')
    return '1'

def fn():
    wd.start()
    try:
        while (True):
            import time
            randomTime = random.randint(0, 2)
            print(randomTime)
            time.sleep(randomTime)
            #Da sempre erro pois a função é infinita não printa OI
            #n = functionInfinita()
            print('oi')
            wd.reset()
    except :
        print("watchdogVallueError")
        #print('Error Watchdog')
        #print(e.error)
            

if __name__ == "__main__":
    twe = ThreadWithExc(target=fn)
    wd = Watchdog(1,twe)

    twe.start()
