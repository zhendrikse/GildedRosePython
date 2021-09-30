class Quality:
    def __init__(self, quality: int):
        self.value = quality

    def increase(self):
        if self.value < 50:
            self.value += 1

    def decrease(self):
        if self.value > 0:
            self.value -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = Quality(quality)

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality.value)

    def update_quality(self) -> None:
        self.quality.decrease()
        self.sell_in -= 1


class AgedBrieItem(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Aged Brie", sell_in, quality)

    def update_quality(self) -> None:
        self.quality.increase()
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality.increase()


class BackstagePassItem(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Backstage passes to a TAFKAL80ETC concert", sell_in,
                         quality)

    def update_quality(self) -> None:
        self.quality.increase()
        if self.sell_in < 11:
            self.quality.increase()
        if self.sell_in < 6:
            self.quality.increase()

        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality = Quality(0)


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
