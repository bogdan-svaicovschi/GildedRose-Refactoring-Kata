# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

NORMAL = "cheese"
BRIE = "Aged Brie"
CONCERT = "Backstage passes to a TAFKAL80ETC concert"
SULFUR = "Sulfuras, Hand of Ragnaros"
CONJURED = "Conjured"

class GildedRoseTest(unittest.TestCase):
    def test_name(self):
        items = [Item(NORMAL, 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(NORMAL, items[0].name)

    def test_update_normal_item(self):
        items = items = [Item(NORMAL, 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)

    def test_update_normal_item_after_sellin_expired(self):
        items = items = [Item(NORMAL, 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)

    def test_update_check_if_it_maxes_at_50(self):
        items = items = [Item(BRIE, 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_update_brie(self):
        items = items = [Item(BRIE, 10, 24)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(25, items[0].quality)

    def test_brie_quality_increases_by_two_after_sellin(self):
        items = items = [Item(BRIE, 0, 46)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(48, items[0].quality)

    def test_sulfuras(self):
        items = [Item(SULFUR, 10, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(49, items[0].quality)
        self.assertEqual(10, items[0].sell_in)

    def test_ticket(self):
        items = [Item(CONCERT, 20, 38)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(39, items[0].quality)
    
    def test_ticket_sellin1(self):
        items = [Item(CONCERT, 10, 36)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(38, items[0].quality)

    def test_ticket_sellin2(self):
        items = [Item(CONCERT, 5, 24)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(27, items[0].quality)

    def test_ticket_sellin0(self):
        items = [Item(CONCERT, 0, 24)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_repr(self):
        items = [Item(NORMAL, 10, 10)]
        self.assertEqual("cheese, 10, 10", items[0].__repr__())

    def test_conjured_before_sellin(self):
        items = [Item(CONJURED, 1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)

    def test_conjured_after_sellin(self):
        items = [Item(CONJURED, 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(16, items[0].quality)
    
    

        
if __name__ == '__main__':
    unittest.main()
