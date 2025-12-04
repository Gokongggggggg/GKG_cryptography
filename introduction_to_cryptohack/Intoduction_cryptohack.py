#!/usr/bin/env python3 -- This line tell OS (Like Linux/macOS) to run this script using python 3 interpreter

import sys

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

print("Here is your flag:")
print("".join(chr(o ^ 0x32) for o in ords))

# chr -> change integer to ASCII Character
# ^ -> XOR operation
# The "0x" prefix in hexadecimal numbers indicates that the number that follows is in base-16, which is hexadecimal.






