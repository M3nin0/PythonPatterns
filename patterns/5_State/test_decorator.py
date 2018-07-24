def double_damage(soma):
	def wrapper(x, y):
		return soma(x, y) * 2
	return wrapper

@double_damage
def soma(x, y):
	return x + y

a = soma(2, 2)
print(a)
