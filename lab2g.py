#!/usr/bin/env python3
# Author: sarjina
# Author ID: skarki28
# Date Created: 2024/09/27

import sys

# Default timer value
timer = 3

# Check if an argument was provided
if len(sys.argv) > 1:
    timer = int(sys.argv[1])

# While loop to countdown
while timer > 0:
    print(timer)
    timer -= 1

print('blast off!')

