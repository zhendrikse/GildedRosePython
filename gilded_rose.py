class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
    def update_quality(self) -> None:
        if self.quality > 0:
            self.quality -= 1
        self.sell_in -= 1


class AgedBrieItem(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Aged Brie", sell_in, quality)

    def update_quality(self) -> None:
        if self.quality < 50:
            self.quality += 1
        self.sell_in -= 1
        if self.sell_in < 0:
            if self.quality < 50:
                self.quality += 1


class BackstagePassItem(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Backstage passes to a TAFKAL80ETC concert", sell_in,
                         quality)

    def update_quality(self) -> None:
        if self.quality < 50:
            self.quality += 1
            if self.sell_in < 11:
                if self.quality < 50:
                    self.quality += 1
            if self.sell_in < 6:
                if self.quality < 50:
                    self.quality += 1

        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality = 0


class SulfurasItem(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Sulfuras, Hand of Ragnaros", sell_in, quality)

    def update_quality(self) -> None:
        pass


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            item.update_quality()
