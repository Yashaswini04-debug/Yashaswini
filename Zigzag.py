print("name:Yashaswini R \N USN:1AY24AI116\n sec:O")
import time
import sys

indent = 0
indent_increasing = True

try:
    while True:
        print(' ' * indent + 'ZIGZAG')
        time.sleep(0.1)
        
        if indent_increasing:
            indent += 1
            if indent == 20:
                indent_increasing = False
        else:
            indent -= 1
            if indent == 0:
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()
