from django.contrib import admin
from .models import Produto
admin.site.register(Produto)
from .models import Marca
admin.site.register(Marca)
# Register your models here.
