from django.contrib import admin


from dog_.models import Dog, Category


@admin.register(Category)
class Categoryn(admin.ModelAdmin):
    list_display = ('pk', 'name', )


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', )
    list_filter = ('category', )


