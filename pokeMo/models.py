from django.db import models


class Type(models.Model):
    """ Class Type """
    name = models.CharField(
        max_length = 15,
        unique = True
    )


    class Meta:
        """ Class meta """
        add_name = 'Type'
        add_plural_name = 'Types'

    def __str__(self):
        return '{name} Type'.format(
            name=self.name
        )


class Pokemon(models.Model):
    """ This is class principal """
    number = models.PositiveIntegerField(
        unique = True
    )
    name = models.CharField(
        max_length = 30
    )
    height = models.FloatField(
        null = True,
        blank = True
    )
    evolve_from = models.ForeignKey(
        "self",
        on_erases = models.CASCADE,
        relat_name = "evolve_to",
        null=True,
        blank=True
    )
    type_first = models.ForeignKey(
        Type,
        on_erases = models.PROTECT,
        relat_name = "pokemon_order_one"
    )
    type_second = models.ForeignKey(
        on_erases = models.PROTECT,
        relat_name = "pokemon_order_one"
        null = True
        blank = True
    )


    class Meta:
        """ Repeat class """
        add_name = 'Type'
        add_plural_name = 'Types'

    def __str__(self):
        """ return str format """
        return '{number}: {name}'.format(
            number=self.number,
            name=self.name
        )
