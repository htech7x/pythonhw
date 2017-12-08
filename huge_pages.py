path = "/sys/devices/system/node/node0/meminfo"
memory = open(path)
print memory.read()
