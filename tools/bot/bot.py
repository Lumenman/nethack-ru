"""Drive console NetHack.exe through ConPTY and read the screen as text.

Usage as a library:
    b = Bot(play_dir, args=['-D'])
    b.send('i'); print(b.screen())
Each send() waits for output to settle.  log() appends screens to a file."""
import os, time, re, threading
import winpty, pyte

ESC = '\x1b'


class Bot:
    def __init__(self, play, args=(), cols=80, rows=24, logfile=None):
        self.cols, self.rows = cols, rows
        self.scr = pyte.Screen(cols, rows)
        self.stream = pyte.Stream(self.scr)
        exe = os.path.join(play, 'NetHack.exe')
        self.p = winpty.PtyProcess.spawn([exe, *args], cwd=play,
                                         dimensions=(rows, cols))
        self.lock = threading.Lock()
        self.last = time.time()
        self.raw = []
        self.log_f = open(logfile, 'a', encoding='utf-8') if logfile else None
        self.t = threading.Thread(target=self._reader, daemon=True)
        self.t.start()
        self.settle(3.0)

    def _reader(self):
        while True:
            try:
                data = self.p.read(4096)
            except EOFError:
                break
            except Exception:
                break
            if data:
                with self.lock:
                    self.stream.feed(data)
                    self.raw.append(data)
                    self.last = time.time()

    def settle(self, quiet=0.4, maxwait=8.0):
        t0 = time.time()
        time.sleep(0.05)
        while time.time() - t0 < maxwait:
            if time.time() - self.last >= quiet:
                return
            time.sleep(0.05)

    def send(self, keys, quiet=0.4):
        for k in keys:
            self.p.write(k)
            time.sleep(0.03)
        self.settle(quiet)
        return self.screen()

    def line(self, text, quiet=0.4):
        return self.send(text + '\r', quiet)

    def screen(self):
        with self.lock:
            return '\n'.join(l.rstrip() for l in self.scr.display)

    def top(self):
        return self.screen().split('\n')[0]

    def log(self, title):
        s = self.screen()
        if self.log_f:
            self.log_f.write(f'===== {title}\n{s}\n')
            self.log_f.flush()
        return s

    def more(self, limit=20):
        """Dismiss --More-- prompts, logging every message line seen."""
        seen = []
        for _ in range(limit):
            s = self.screen()
            seen.append(s.split('\n')[0])
            if '--More--' in s or '--Дальше--' in s or 'Дальше' in s.split('\n')[0]:
                self.send('\r')
            else:
                break
        return seen

    def alive(self):
        return self.p.isalive()

    def close(self):
        try:
            self.p.terminate(force=True)
        except Exception:
            pass
