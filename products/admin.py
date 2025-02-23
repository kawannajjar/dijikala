from django.contrib import admin

from .models import Product, ProductPrice,ProductsOption,\
    Question,Answer,Image,Category,Comments


class ImageInline(admin.TabularInline):
    model = Image
    extra = 2

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['en_name', 'name', 'short_description', 'category']
    search_fields = ['name', 'en_name']
    list_filter = ['category']
    inlines = [ImageInline]
    @admin.display(description='Description')
    def short_description(self, obj):
        return obj.description[:50] + "..." if len(obj.description) > 50 else obj.description

    fieldsets = [
        ('Details', {
            'fields': [
                'name', 'en_name', 'description',
            ],
        }),
        ('Category', {
            'fields': [
                'category'
            ],
        }),
    ]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image','alt']

@admin.register(ProductPrice)
class ProductPriceAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductsOption)
class ProductsOptionAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug','parent']
    search_fields = ["name",'description']
    list_filter = ['parent']
    fieldsets = [
        ('Details', {
            'fields': [
                'name','slug','description'
            ],
        }),
        ('Category', {
            'fields': [
                'parent'
            ],
        }),
        ('Images', {
            'fields': [
                'icon','image'
            ],
        }),
    ]
@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    pass