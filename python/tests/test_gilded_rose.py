# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_name(self):
        items = [Item("foo", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_update_normal_item(self):
        items = items = [Item("foo", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)

    def test_update_normal_item_sellin_expired(self):
        items = items = [Item("foo", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)

    def test_update_brie(self):
        items = items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_update_brie_50(self):
        items = items = [Item("Aged Brie", 10, 24)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(26, items[0].quality)

    def test_brie_quality(self):
        items = items = [Item("Aged Brie", 1, 46)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(49, items[0].quality)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(49, items[0].quality)
        self.assertEqual(10, items[0].sell_in)

    def test_ticket(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 20, 38)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(40, items[0].quality)
    
    def test_ticket_sellin1(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 36)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(40, items[0].quality)

    def test_ticket_sellin2(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 24)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(30, items[0].quality)

    def test_ticket_sellin0(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 24)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_repr(self):
        items = [Item("foo", 10, 10)]
        self.assertEqual("foo, 10, 10", items[0].__repr__())
    
    

        
if __name__ == '__main__':
    unittest.main()
