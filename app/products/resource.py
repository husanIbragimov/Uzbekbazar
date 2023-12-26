from django.db import transaction
from import_export import resources
from .models import ProductSize


class ProductSizeResource(resources.ModelResource):
    class Meta:
        model = ProductSize
        fields = ('id', 'product__title', 'color__name',  'size__name', 'availability', 'price')

    def after_import(self, dataset, result, using_transactions, dry_run, **kwargs):
        """
        Override to add additional logic. Does nothing by default.
        Manually removing commit hooks for intermediate savepoints of atomic transaction
        """
        
        for data in dataset:
            model = ProductSize.objects.get(id=data[0])
            model.availability = data[1]
            model.price = data[2]
            model.save()