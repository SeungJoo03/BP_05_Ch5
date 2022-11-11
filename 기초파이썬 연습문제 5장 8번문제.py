Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Turtle()
>>> t. shape("turtle")
>>> 
>>> x1 = int(input(" 큰원의 중심좌표 x1: "):
	 
SyntaxError: invalid syntax
>>> x1 = int(input("큰 원의 중심좌표 x1: "))
큰 원의 중심좌표 x1: 0
>>> y1 = int(input("큰 원의 중심좌표 y1: "))
큰 원의 중심좌표 y1: 0
>>> r1 = int(input("큰 원의 반지름 r1: "))
큰 원의 반지름 r1: 100
>>> x2 = int(input("큰 원의 중심좌표 x2: "))
큰 원의 중심좌표 x2: 10
>>> y2 = int(input("큰 원의 중심좌표 y2: "))
큰 원의 중심좌표 y2: 10
>>> r2 = int(input("큰 원의 반지름 r2: "))
큰 원의 반지름 r2: 50
>>> 
>>> t.up()
>>> t.goto(x1, y1-r1)
>>> t.down()
>>> t.up()
>>> t.goto(x2, y2-r2)
>>> t.down()
>>> t.circle(r2)
>>> z=((x1-x2)**2+(y1-y2)**2)**0.5
>>> if z <= r1-r2:
	t.write("두 번째 원이 첫 번째 원의 내부에 있습니다.")
elif z >= r1+r2:
	t.write("두 번째 원이 첫 번째 원의 외부에 있습니다.")
else:
	t.wirte("두 번째 원과 첫 번째 원이 서로 겹쳐있습니다.")
	
