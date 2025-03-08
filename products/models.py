from django.db import models
from gettext import gettext as _

class Product(models.Model):
    name = models.CharField(_("Persian Name"),max_length=200)
    en_name  = models.CharField(_("English Name"), max_length=200)
    description = models.TextField(_("Description"))
    category = models.ForeignKey("Category",
                                 verbose_name=_("Category"),
                                 on_delete=models.RESTRICT
                                 )
    def __str__(self):
        return f"{self.id},{self.name}"

class Category(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    slug = models.SlugField(_("Slug"),unique=True,db_index=True)
    description = models.TextField(_("Description"))
    icon = models.ImageField(_("Icon"),upload_to='category_images',null=True,blank=True)
    image= models.ImageField(_("Image"),upload_to='category_images',null=True,blank=True)
    parent = models.ForeignKey("self",
                               verbose_name=_("Parent Category"),
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True,
                               )
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return f"{self.slug}"

class Comments(models.Model):
    title = models.CharField(_("Title"),max_length=150)
    text = models.TextField(_("Text"))
    product = models.ForeignKey("Product",
                                verbose_name=_("Product"),
                                on_delete=models.CASCADE
                                )

    rate = models.PositiveIntegerField(_("Rate"))
    user_email = models.EmailField(_("Email"), max_length=254)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return f"comment on{self.product.name}"

class Image(models.Model):

    name = models.CharField(_("Image Name"), max_length=50)
    alt = models.CharField(_("Alternative Text"), max_length=100)
    product = models.ForeignKey("Product",
                                verbose_name=_("Product"),
                                on_delete=models.CASCADE)
    image = models.ImageField(_("Image"),upload_to="products")
    is_default = models.BooleanField(_("Is default image?"), default=False)
    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __str__(self):
        return f"{self.name}"

class Question(models.Model):
    text = models.TextField(_("Question"))
    user_email = models.EmailField(_("Email"), max_length=254)
    product = models.ForeignKey("Product",
                                verbose_name=_("Product"),
                                on_delete=models.CASCADE
                                )

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __str__(self):
        return  self.text

class Answer(models.Model):
    text = models.TextField(_("Answer"))
    question = models.ForeignKey("Question",
                                verbose_name=_("Question"),
                                on_delete=models.CASCADE
                                )


    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")

    def __str__(self):
        return self.text


class ProductsOption(models.Model):
    product = models.ForeignKey("Product",
                                verbose_name=_("Product"),
                                on_delete=models.CASCADE
                                )
    name = models.CharField(_("Attribute"), max_length=100)
    value = models.CharField(_("Value"), max_length=200)



    class Meta:
        verbose_name = _("ProductsOption")
        verbose_name_plural = _("ProductsOptions")

    def __str__(self):
        return f"{self.product.name} {self.name}"


class ProductPrice(models.Model):
    product = models.ForeignKey("Product",
                                verbose_name=_("Product"),
                                on_delete=models.CASCADE
                                    )
    price = models.PositiveSmallIntegerField(_("Price"))
    create_at = models.DateTimeField(_("Datetime create"), auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(_("Datetime Update"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _("ProductPrice")
        verbose_name_plural = _("ProductPrices")
