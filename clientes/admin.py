from django.contrib import admin
from .models import Person, Document, Venda, Produto

# Register your models here.
admin.site.register(Person)
admin.site.register(Document)
admin.site.register(Venda)
admin.site.register(Produto)