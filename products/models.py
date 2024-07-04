from django.db import models


class CategoryModel(models.Model):
    category_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class ProductModel(models.Model):
    product_name = models.CharField(max_length=80)
    price = models.FloatField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(default=0)
    description = models.TextField()
    image = models.FileField(upload_to='product_image')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


# HW
class NewsCategoryModel(models.Model):
    category_name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "NewCategory"
        verbose_name_plural = "NewCategories"

class NewsModel(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    category = models.ForeignKey(NewsCategoryModel, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    news_image = models.FileField(upload_to="product_image", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"

class CartModel(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True)
    user_product_quantity = models.IntegerField(default=0)
    user_add_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user_product})"

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
