"""Run a scenario: python -X utf8 tools/bot/run.py tools/bot/sc/scenario.py [logname]
Needs: pip install pywinpty pyte; a Release|x64 build; ~/NetHack/.nethackrc
(name:wizard for -D).
The scenario is executed with `b` (a Bot started in wizard mode), and helpers:
  S(title)            log the current screen under title
  K(keys, title=None) send keys, optionally log
  M()                 dismiss --More-- / Enter prompts (logging each top line)
  wish(text)          ^W wish for text
  ext(cmd)            #extended command
Logs go to logs/<logname>.txt"""
import sys, os, time, runpy
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from bot import Bot
ROOT = HERE
# the freshly built game: its nhdat500 is current, the one inside the zip may not be
PLAY = os.path.join(HERE, '..', '..', 'binary', 'Release', 'x64')
scen = sys.argv[1]
name = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(os.path.basename(scen))[0]
os.makedirs(os.path.join(ROOT, 'logs'), exist_ok=True)
logf = os.path.join(ROOT, 'logs', name + '.txt')
if os.path.exists(logf):
    os.remove(logf)
LEV = os.path.join(os.environ['LOCALAPPDATA'], 'NetHack', '5.0')
def clean():
    import glob
    for f in glob.glob(os.path.join(LEV, 'wizard.*')) + glob.glob(os.path.join(LEV, 'Tester.*')) + glob.glob(os.path.join(LEV, 'bon*')):
        os.remove(f)
    lk = os.path.join(os.environ['PROGRAMDATA'], 'NetHack', '5.0', 'NHPERM_lock')
    if os.path.exists(lk):
        os.remove(lk)
clean()
b = Bot(PLAY, os.environ.get('NHARGS', '-D').split(), logfile=logf)
msgs = []
CR = chr(13)
PAUSES = ('Hit <Enter>', 'Нажмите <Enter>', 'Нажмите Enter')
MORES = ('--More--', 'Дальше')


def S(title):
    return b.log(title)


def is_pause(s):
    return any(p in s for p in PAUSES)


def is_more(s):
    return any(p in s for p in MORES)


def M(limit=30):
    for _ in range(limit):
        s = b.screen()
        msgs.append(s.split('\n')[0])
        if is_pause(s):
            S('pause')
            b.send(CR, 0.8)
        elif is_more(s):
            b.send(CR)
        else:
            return s
    return b.screen()


def boot(maxwait=25):
    t0 = time.time()
    while time.time() - t0 < maxwait:
        s = b.screen()
        if is_pause(s):
            S('boot pause')
            b.send(CR, 1.0)
        elif is_more(s):
            msgs.append(s.split('\n')[0])
            b.send(CR)
        elif 'Восстановить?' in s or 'Get bones?' in s:
            b.send('n', 1.0)
        elif 'Ур.:' in s or 'Dlvl' in s:
            return S('boot done')
        else:
            time.sleep(0.5)
    return S('boot timeout')


def K(keys, title=None, quiet=0.4):
    if keys is None:  # e.g. a wish that did not report an inventory letter
        return b.screen()
    b.send(keys, quiet)
    if title:
        S(title)
    return b.screen()


def wish(text):
    K('\x17')
    K(text + CR, quiet=0.8)
    S('wish ' + text)
    M()
    return b.screen()


def ext(cmd):
    K('#')
    K(cmd + CR, quiet=0.8)
    return b.screen()


g = dict(boot=boot, b=b, S=S, K=K, M=M, wish=wish, ext=ext, msgs=msgs,
         time=time, CR=CR, is_pause=is_pause)
try:
    boot()
    runpy.run_path(scen, init_globals=g)
finally:
    S('FINAL')
    with open(logf, 'a', encoding='utf-8') as f:
        f.write('===== MESSAGE TOPLINES\n' + '\n'.join(m for m in msgs if m.strip()) + '\n')
    b.close()
    time.sleep(0.5)
    clean()
print('log:', logf)
