from vigur import Vector
from sys import stdout, stdin
n = "\n"
s = str
write = stdout.write

v1 = Vector(1, 3)
v1.print()
write("Length: " + s(v1.lengd) + n)
write("?Halli?: " + s(v1.halli) + n)
vþ = v1.þvervigur()
write("Þvervigur: " + s(vþ) + n)
write("stefnuhorn: " + s(v1.stefnuhorn) + n)
v2 = Vector(-3, 1)
write("Horn milli vigra: " + s(v2.horn(v1)) + n)
v3 = v1 + v2
write("Summa: " + s(v3) + n)

