from ctypes import cdll

lib = cdll.LoadLibrary("./target/debug/libwasm_deno_example.so")

print(lib.square(1))
print(lib.square(2))
print(lib.square(3))
print(lib.square(4))
