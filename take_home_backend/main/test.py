from django.test import TestCase
from .models import Tag, Category, Inventory

class TagTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(name="Tag1")
    
    def test_tag(self):
        tag = Tag.objects.get(name="Tag1")
        self.assertEqual(tag.name,"Tag1")

class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="Category1")
    
    def test_tag(self):
        tag = Category.objects.get(name="Category1")
        self.assertEqual(tag.name,"Category1")

class InventoryTestCase(TestCase):
    def setUp(self):
        tr = Tag.objects.create(name="Tag1")
        cr = Category.objects.create(name="Category1")

        ir = Inventory.objects.create(SKU="Entry1",name="Entry1", author="abc",in_stock=0,available_stock=0,category=cr)#,tags=Tag.set(tr), category=cr,)
        ir.tags.set([tr.id])
        ir.save()

    def test_item(self):
        record = Inventory.objects.get(name="Entry1")
        self.assertEqual(record.name,"Entry1")
        # for t in record.tags:
        #     print(t.name)
        self.assertIsNotNone(record.tags)
        self.assertEqual(record.tags.id, [1])
        
        self.assertEqual(record.category.name, "Category1")