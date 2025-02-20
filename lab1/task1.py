
a = 2.16
Da = 0.005
da = Da / abs(a)

b = 10.163
Db = 0.001
db = Db / abs(b)

c = 50.18
Dc = 0.02
dc = Dc / abs(c)

x = ( a * b ) / ( c ** ( 1 / 2 ) )
dx = da + db + ( dc / 2 )
Dx = dx * abs(x)

print(f"X = {x}, Dx = {Dx}, dx = {dx}")