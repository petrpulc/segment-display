import subprocess
from threading import Thread

import display


def rsync_thread():
    global text
    tty = open('/dev/tty1', 'w')

    with subprocess.Popen(['rsync', '-a', '--info=progress2,flist0', '/home/pulc/CSOB_projekce', '/home/pulc/test_rsync/'],
                          stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
            tty.write(line)
            out = line.split()
            if len(out) > 2:
                text = out[1].rjust(4)
    if p.returncode == 0:
        text = 'done'
    else:
        text = 'FAIL'


def print_thread():
    global text
    while True:
        display.show(text, 1)
        if text == 'done' or text == 'FAIL':
            display.show(text, 5)
            break


text = 'init'
thread1 = Thread(target=print_thread)
thread2 = Thread(target=rsync_thread)
thread1.start()
thread2.start()
thread2.join()
thread1.join()
