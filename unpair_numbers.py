x = 0
while x<=100:
    if not(str(x).endswith('0') or str(x).endswith('2') or str(x).endswith('4') or str(x).endswith('6') or str(x).endswith('8')):
        print(x)
    x = x+1


