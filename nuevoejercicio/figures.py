class figura():
	def CalculateArea(self):
		area=self.b*self.h
		return area
	def calculatePerimeter(self):
		perimeter=self.sides*self.b
		return perimeter

class cuadrado(figura):
	def __init__(self,b,h,sides=4):
		self.b=b
		self.h=h
		self.sides=4

class triangulo(figura):
	def __init__(self,b,h,sides=3):
		self.b=b
		self.h=h
		self.sides=3
	def CalculateArea(self):
		area=super().CalculateArea()/2
		return area

cuadrado1=cuadrado(2,2)
print(cuadrado1.CalculateArea())
print(cuadrado1.calculatePerimeter())

triangulo1=triangulo(4,3)
print(triangulo1.CalculateArea())
