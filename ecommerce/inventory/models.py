from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
    """Inventory Category table implimented with MPTT."""

    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_('Category Name'),
        help_text=_("format: required, max-100")
    )
    slug = models.SlugField(
        max_length=150,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_('Category safe URL'),
        help_text=_("format: required, letters, numbers, hyphens, underscores")
    )
    is_active = models.BooleanField(
        default=False,
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.PROTECT,
        related_name='children',
        null=True,
        blank=True,
        unique=False,
        verbose_name=_('Parent of Category'),
        help_text=_("format: not required")
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _('Product Category')
        verbose_name_plural = _('Product Categories')

    def __str__(self):
        return self.name


class Product(models.Model):
    """Inventory Product table implimented with MPTT."""

    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_('Product Name'),
        help_text=_("format: required, max-100")
    )
    web_id = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_('Product Web ID'),
        help_text=_("format: required, max-50, unique")
    )
    slug = models.SlugField(
        max_length=150,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_('Product safe URL'),
        help_text=_("format: required, letters, numbers, hyphens, underscores")
    )
    is_active = models.BooleanField(
        default=False,
        unique=False,
        blank=False,
        verbose_name=_('Product visibility'),
        help_text=_("format: required, boolean, true=product is visible, false=product is hidden")
    )
    category = TreeManyToManyField(
        Category,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at'),
        help_text=_("format: required")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated at'),
        help_text=_("format: required")
    )

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name