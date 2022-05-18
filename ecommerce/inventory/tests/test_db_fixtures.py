import pytest
from ecommerce.inventory import models


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (1, "fashion", "fashion", 1),
        (18, "trainers", "trainers", 1),
        (35, "baseball", "baseball", 1),
    ],
)
def test_inventory_category_dbfixture(
    db, db_fixture_setup, id, name, slug, is_active
):
    result = models.Category.objects.get(id=id)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.parametrize(
    "slug, is_active",
    [
        ("fashion1", 1),
        ("trainers1", 1),
        ("baseball1", 1),
    ],
)
def test_inventory_db_category_insert_data(
    db, category_factory, slug, is_active
):
    result = category_factory.create(slug=slug, is_active=is_active)
    print(result.name)

    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, web_id, name, slug, description, is_active, created_at, updated_at",
    [
        (11111, 12323232, "Fashion", "fashion", "Fashion", 1, "2020-01-01 00:00:00", "2020-01-01 00:00:00"),
        (123238, 54687828, "Trainers", "trainers", "Trainers", 1, "2020-01-01 00:00:00", "2020-01-01 00:00:00"),
        (46876835, 546455468735, "Baseball", "baseball", "Baseball", 1, "2020-01-01 00:00:00", "2020-01-01 00:00:00"),
    ],
)
def test_inventory_product_dbfixture(
    db,
    db_fixture_setup,
    id, web_id,
    name,
    slug,
    description,
    is_active,
    created_at,
    updated_at
):
    result = models.Product.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    assert result.web_id == web_id
    assert result.name == name
    assert result.slug == slug
    assert result.description == description
    assert result.is_active == is_active
    assert result_created_at == created_at
    assert result_updated_at == updated_at

def test_inventroy_db_product_uniqueness_integrity(db, product_factory):
    new_web_id = product_factory.create(web_id=12345)
    with pytest.raises(IntegrityError):
        new_web_id = product_factory.create(web_id=12345)

def test_inventory_db_product_insert_data(db, category_factory, product_factory):
    new_category = category_factory.create()
    new_product = product_factory.create(category=(1, 35))
    result_product_category = new_product.category.all().count()
    assert "web_id_" in new_product.web_id
    assert result_product_category == 2