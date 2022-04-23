from config.wsgi import *
from core.erp.models import Type

#Listar
# SELEC * FROM TABLA

query = Type.objects.all()

print(query)

#insercion

#t = Type(name = 'prueba').save()


#edicion

#t = Type.objects.get(id=1)
#t.name = 'accionista322'
#t.save()

#eliminacion

#t = Type.objects.get(pk=1)
#t.delete()

