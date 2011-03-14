class Super(object):
	def metodo(self):
		print "BLA"


class Sub(Super):
	pass

class SubSub(Sub):
	def metodo(self):
		print "BLE"

a = Super()

a.metodo()

b = Sub()

b.metodo()

c = SubSub()

c.metodo()
