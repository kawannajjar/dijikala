from django.contrib import admin

from .models import Product, ProductPrice,ProductsOption,\
    Question,Answer,Image,Category,Comments


class ImageInline(admin.TabularInline):
    model = Image
    extra = 2


@admin.register(ProductPrice)
class ProductPriceAdmin(admin.ModelAdmin):
    list_filter = ['price',('create_at', admin.DateFieldListFilter),'product']
    list_display = ['product','price','create_at','update_at']
    fieldsets = [
        ('Details', {
            'fields': [
                'product', 'price',
            ],
        }),
    ]


@admin.register(ProductsOption)
class ProductsOptionAdmin(admin.ModelAdmin):
    list_filter = ['product']
    list_display = ['product','name','value']

class ProductPriceInline(admin.TabularInline):
    model = ProductPrice
    extra = 1

class ProductsOptionInline(admin.TabularInline):
    model = ProductsOption
    extra = 1

class ProductAdminMixin:
    @admin.display(description='Description')
    def short_description(self, obj):
        return obj.description[:50] + "..." if len(obj.description) > 50 else obj.description

    @admin.display(description="Number of Images")
    def image_count(self, obj):
        return obj.image_set.count()

    @admin.display(description="Number of Comments")
    def comment_count(self, obj):
        return obj.comments_set.count()

    @admin.display(description="Latest Price")
    def latest_price(self, obj):
        last_price = obj.productprice_set.order_by('-create_at').first()
        return last_price.price if last_price else "No Price"

    @admin.display(description="Short English Name")
    def short_en_name(self,obj):
        return obj.en_name[:40] + "..." if len(obj.en_name) > 40 else obj.en_name
    @admin.display(description="Short Persian Name")
    def short_persian_name(self,obj):
        return obj.name[:40] + "..." if len(obj.name) > 40 else obj.en_name


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin,ProductAdminMixin):
    list_display = ['short_en_name', 'short_persian_name', 'short_description', 'category', 'image_count', 'comment_count', 'latest_price']
    search_fields = ['name', 'en_name']
    list_filter = ['category']
    inlines = [ImageInline,ProductsOptionInline,ProductPriceInline]
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
    fieldsets = [
        ('Details', {
            'fields': [
                'name', 'product',
            ],
        }),
        ('Upload Image', {
            'fields': [
                 'image', 'alt',
            ],
        }),
    ]
class AnswerInline(admin.TabularInline):
    model = Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['product']
    list_display = ['product','text','user_email']
    inlines = [AnswerInline]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['text','question']
    list_filter = ['question']



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
    @admin.display(description='text')
    def short_text(self, obj):
        return obj.text[:40] + "..." if len(obj.text) > 40 else obj.text
    list_filter = ['title','rate']
    list_display = ['title','short_text','rate','product','user_email']