# Built-in Data Types

# Text Type: 	    str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	    set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview

a = "A set of words"
b = 20
c = 20.1
d = 2 * 3
e = ["apple", "banana", "cherry"]
f = ("apple", "banana", "cherry")
g = range(6)
h = {"name" : "John", "age" : 36}
i = {"apple", "banana", "cherry"}
j = frozenset({"apple", "banana", "cherry"})
k = True
l = b"Hello"
m = bytearray(5)
n = memoryview(bytes(5))

print("a", a, type (a))
print("b", b, type (b))
print("c", c, type (c))
print("d", d, type (d))
print("e", e, type (e))
print("f", f, type (f))
print("g", g, type (g))
print("h", h, type (h))
print("i", i, type (i))
print("j", j, type (j))
print("k", k, type (k))
print("l", l, type (l))
print("m", m, type(m))
print("n", n, type (n))
