import sys

a = []
b = a
c = b

# [] is referenced by a, b, c and getrefcount's argument
print(f"a has {sys.getrefcount(a)} ref(s)")

c = None

# [] is referenced by a, b and getrefcount's argument
print(f"a has {sys.getrefcount(a)} ref(s)")