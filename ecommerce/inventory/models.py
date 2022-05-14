from django.db import models
from django-utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
    """Inventory Category table implimented with MPTT."""

    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True,
        blank=False,
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

