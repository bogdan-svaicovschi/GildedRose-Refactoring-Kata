# -*- coding: utf-8 -*-

class GildedRose(object):
    BRIE = "Aged Brie"
    CONCERT = "Backstage passes to a TAFKAL80ETC concert"
    SULFUR = "Sulfuras, Hand of Ragnaros"
    CONJURED = "Conjured"
    UNIT = 1
    DOUBLE_UNIT = 2
    LOWER_BOUND = 0
    UPPER_BOUND = 50
    FIRST_THRESHOLD = 10
    SECOND_THRESHOLD = 5

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != self.SULFUR:
                if item.name != self.CONCERT and item.name != self.BRIE:
                    item.quality = max(self.LOWER_BOUND, item.quality - self.UNIT)
                    if item.name == self.CONJURED:
                        item.quality = max(self.LOWER_BOUND, item.quality - self.UNIT)
                else:
                    additional = self.UNIT
                    if item.name == self.CONCERT:
                        if item.sell_in <= self.FIRST_THRESHOLD:
                            if item.sell_in <= self.SECOND_THRESHOLD:
                                additional += self.DOUBLE_UNIT
                            else:
                                additional += self.UNIT
                    item.quality = min(self.UPPER_BOUND, item.quality + additional)

                item.sell_in -= self.UNIT

                if item.sell_in < self.LOWER_BOUND:
                    if item.name == self.CONCERT:
                        item.quality = self.LOWER_BOUND
                    elif item.name == self.BRIE:
                        item.quality = min(self.UPPER_BOUND, item.quality + self.UNIT)
                    else:
                        item.quality = max(self.LOWER_BOUND, item.quality - self.UNIT)
                        if item.name == self.CONJURED:
                            item.quality = max(self.LOWER_BOUND, item.quality - self.UNIT)


                    



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
