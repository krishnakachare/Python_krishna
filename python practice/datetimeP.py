import time
epoch = time.time()
print(epoch)

t = time.localtime(epoch)
print(type(t))

print()

w = time.ctime(epoch)
print(w)
