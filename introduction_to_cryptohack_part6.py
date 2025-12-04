
given_string = "label"

new_string = "".join(chr(ord(x) ^ 13 ) for x in given_string)

print(f"crypto{{{new_string}}}")