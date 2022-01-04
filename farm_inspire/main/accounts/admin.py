from django.contrib import admin
from .models import User, Customer, Employee,AddProducts,category

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(AddProducts)
admin.site.register(category)

