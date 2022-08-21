import ctypes

lib = ctypes.CDLL('./lib.so')

main = lib.main
main.restype = ctypes.c_int

print('Start')
main()
print('End')
