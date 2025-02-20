
a = 10.5 
Da = 0.01
da = Da / abs(a)

b = 3.5
Db = 0.04
db = Db / abs(b)

m = 4.26
Dm = 0.001
dm = Dm / abs(m)

c = 34.2
Dc = 0.01
dc = Dc / abs(c)

d = 23.723
Dd = 0.002
dd  = Dd / abs(d)

x = ( ( m ** 3 ) * (a + b) ) / (c + d)
dx = ( (3 * dm) + ( (a * da + b * db) / (a + b)  ) ) / ( ( c * dc + d * dd ) / ( d + c) )
Dx = dx * abs(x)

print(f"X = {x}, Dx = {Dx}, dx = {dx}")
