a=eval(input("coloca el primer lado: "))

b=eval(input("coloca el segundo lado: "))

c=eval(input("coloca el tercer lado: "))

d=eval(input("coloca el cuarto lado: "))

if (a==b and c==d and a!=d and c!=b) or (a==c and b==d and a!=b and c!=d) or (a==d and b==c and a!=c and b!=d):
    print("es rectangulo")
elif a==b and a==d and a==c:
    print("es un cuadrado")
else:
    print("es otro cuadrilatero")
    