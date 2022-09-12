from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinLengthValidator

class ProductList(models.Model):
    title = models.CharField(max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    file = models.FileField(upload_to='product_lists')
    column_names = ArrayField(
       models.CharField(max_length=512), blank=True, null=True
    )
    def __str__(self):
        return self.title

class PriceList(models.Model):
    title = models.CharField(max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    file = models.FileField(upload_to='price_lists')
    column_names = ArrayField(
       models.CharField(max_length=512), blank=True, null=True
    )
    def __str__(self):
        return self.title

class OutputCsv(models.Model):
    title = models.CharField(max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    file = models.FileField(upload_to='output_csvs', null=True, blank=True)
    product_list = models.ForeignKey(ProductList, on_delete=models.CASCADE)
    price_list = models.ForeignKey(PriceList, on_delete=models.CASCADE)
    product_list_search_field = models.CharField(max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    product_list_replace_field = models.CharField(max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    price_list_search_field = models.CharField(max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    price_list_replace_field = models.CharField(max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    def __str__(self):
        return self.title

class DiscountCode(models.Model):
    title = models.CharField(max_length=200,
            validators=[MinLengthValidator(1, "Title must be greater than 1 characters")]
    )
    amount = models.CharField(max_length=20,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")], blank=True, null=True
    )
    cost = ArrayField(
       models.FloatField(), blank=True, null=True
    )
    tier3_only = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class PriceDiscount(models.Model):
    title = models.CharField(max_length=200,
            validators=[MinLengthValidator(1, "Title must be greater than 1 characters")]
    )

    tier3_amount = ArrayField(
       models.FloatField(), blank=True, null=True
    )
    tier2_amount = ArrayField(
       models.FloatField(), blank=True, null=True
    )
    tier1_amount = ArrayField(
       models.FloatField(), blank=True, null=True
    )
    def __str__(self):
        return self.title