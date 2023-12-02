import random

TAB_MULTIPLIER = 15
chars = ['%', '$', '#', '@', '&', '*']
tab = "\t"
backspace = "\b"

backspace_count = 0
tabs = TAB_MULTIPLIER * "\t"

print("\n\n\n")
print("{}{}".format(tabs, "★"))

for i in range(1, 51, 2):
    bs = ''
    tree_line = ''
    for b in range(0, backspace_count):
        bs += '\b'
    for c in range(0, i):
        bs += chars[random.randint(0,5)]
    backspace_count+=1
    print("{}{}{}".format(tabs, bs, tree_line))

for i in range (0,6):
    print("{}\b\b\b\b{}".format(tabs, "||||||||||"))

print("{}{}{}".format(tabs, backspace * TAB_MULTIPLIER * 3, "*_*" * TAB_MULTIPLIER * 2))
print("{}{}{}".format(tabs, backspace * TAB_MULTIPLIER, 'BTW! Follow me on X: @georgemff1 😇'))
print("\n\n\n")
