from django.test import TestCase
from .models import Tag, Category, Inventory


class TagModelTest(TestCase):
    def setUp(self):
        Tag.objects.create(name="Tag1")

    def test_name_label(self):
        tag = Tag.objects.get(name="Tag1")
        field_label = tag._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_object_name_is_name_field(self):
        tag = Tag.objects.get(name="Tag1")
        expected_object_name = "Tag1"
        self.assertEqual(expected_object_name, str(tag))


class CategoryModelTest(TestCase):
    def setUp(self):
        Category.objects.create(name='Test Category')

    def test_name_label(self):
        category = Category.objects.get(name='Test Category')
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_object_name_is_name_field(self):
        category = Category.objects.get(name='Test Category')
        expected_object_name = 'Test Category'
        self.assertEqual(expected_object_name, str(category))


class InventoryModelTest(TestCase):
    def setUp(self):
        test_category = Category.objects.create(name='Test Category')
        Inventory.objects.create(
            SKU='SKU001',
            name='Test Inventory Item',
            category=test_category,
            author='Test Author',
            in_stock=10,
            available_stock=5
        )

    def test_sku_label(self):
        inventory = Inventory.objects.get(SKU='SKU001')
        field_label = inventory._meta.get_field('SKU').verbose_name
        self.assertEqual(field_label, 'SKU')

    def test_tags_blank(self):
        inventory = Inventory.objects.get(SKU='SKU001')
        self.assertEqual(inventory.tags.count(), 0)

    def test_category_relationship(self):
        inventory = Inventory.objects.get(SKU='SKU001')
        self.assertEqual(inventory.category.name, 'Test Category')

