class User():
	def __init__(self, first_name, last_name, idade, telefone, cpf):
		self.first_name = first_name
		self.last_name =last_name
		self.idade = idade
		self.telefone = telefone
		self.cpf = cpf
		self.loggin_attempts = 0
	def describe_user(self):
		print(self.first_name, "Telefone:",self.telefone)
	def greet_user(self):
		print("Olá meu nome é", self.first_name)
	def increment_loggin_attempts(self):
		self.loggin_attempts += 1
	def reset_loggin_attempts(self):
		self.loggin_attempts = 0
"""nando = User(first_name = "luis", last_name= "fernando", idade = 22, telefone = 81991229366, cpf = 70325274428)
nando.describe_user()
nando.greet_user()
messias= User("messias", "batista", 35, 9192929, 70382738292)
messias.describe_user()
messias.greet_user()
sergio= User("Sergio", "thanos", 35, 9182282, 70382827372)
sergio.describe_user()
sergio.greet_user()"""
nando= User("Luis", "Fernando", 22, 819291919, 92929199)
nando.increment_loggin_attempts()
nando.increment_loggin_attempts()
nando.increment_loggin_attempts()
print(nando.loggin_attempts)
nando.reset_loggin_attempts()
print(nando.loggin_attempts)
#msksksk

