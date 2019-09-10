#Aula 9.1
class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.nome = restaurant_name 
		self.cozinha = cuisine_type 
		self.number_served = 0
		
	def describe_restaurant(self):
		print("Nome:", self.nome,"\nCozinha:", self.cozinha)
	def open_restaurant(self):
		print("O restaurante esta aberto")
	def set_number_served(self):
		print(self.number_served, "Clientes atendidos")
	def increment_number_served(self, n):
		self.number_served += n
		
	
		
#AULA 9.2
"""restaurant = Restaurant("La familia", "Pizzaria")
print(restaurant.nome)
print(restaurant.cozinha)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant1 = Restaurant("Sapore","Almoço")
restaurant2 = Restaurant("Gio Bhaiano", "Pizzaria")
restaurant3 = Restaurant("Bode Grill", "Carne")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()"""

#AULA 9.4
restaurant = Restaurant("SW Nordestino", "Carnes")
restaurant.increment_number_served(8)
restaurant.set_number_served()


