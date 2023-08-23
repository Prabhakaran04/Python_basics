# read
fd = open('prac.txt', 'r')
f = fd.read()
print(f)

# write
fd = open('prac.txt', 'w')
fd.write('I am a DEveloper')
fd.close

# append + read
fd = open('prac.txt', 'a+')
fd.write('\nMy name is Prabhakran')
fd.seek(0)
f = fd.read()
print(f)
fd.close()

# ----------
fd = open('prac.txt', 'a+')
fd.write('Kuss\nBuss\nKussBuss')
fd.seek(0)
f = fd.read()
print(f)
fd.close()

# write + read
fd = open('prac.txt', 'w+')
fd.write('Kuss\nBuss\nKussBuss')
fd.seek(0)
f = fd.read()
print(f)
fd.close()
