import time
import threading

class Timer:
    def __init__(self, duration, callback):
        self.duration = duration
        self.callback = callback
        self.running = False
        self.paused = False
        self.time_left = duration
        self._thread = None
        self._lock = threading.Lock()

    def start(self):
        if not self.running:
            self.running = True
            self.paused = False
            self._thread = threading.Thread(target=self._countdown)
            self._thread.daemon = True
            self._thread.start()
        elif self.paused:
            self.paused = False

    def stop(self):
        self.paused = True

    def reset(self):
        with self._lock:
            self.running = False
            self.paused = False
            self.time_left = self.duration

    def _countdown(self):
        while self.running and self.time_left > 0:
            if self.paused:
                time.sleep(0.5)
                continue
            time.sleep(1)
            with self._lock:
                self.time_left -= 1
        if self.running and self.time_left == 0:
            self.running = False
            self.callback()
