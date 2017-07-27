#!/usr/bin/env python3
import subprocess
import display

data = subprocess.run(['df', '-h', '/mnt/backup'], stdout=subprocess.PIPE).stdout.decode('utf-8')

display.init()
display.show(data.split('\n')[1].split()[3].rjust(4), 2)
