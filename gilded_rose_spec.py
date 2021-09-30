from mamba import description, it, context, before
from expects import expect, equal, raise_error
from gilded_rose import GildedRose, SulfurasItem, BackstagePassItem, AgedBrieItem, Item

def do_update(item: Item):
    app = GildedRose([item])
    app.update_quality()

with description(GildedRose) as self:

  with description("Given an aged brie item"):
    with description("with quality and sell in 1"):
      with description("when updating it"):
        with it("should have decreased sell in and added 1 to quality"):
          item = AgedBrieItem(1, 1)
          do_update(item)
          expect(item.sell_in).to(equal(0))
          expect(item.quality.value).to(equal(2))
    with description("with quality and sell in 0"):
      with description("when updating it"):
        with it("should have decreased sell in and added 2 to quality"):
          item = AgedBrieItem(0, 0)
          do_update(item)
          expect(item.sell_in).to(equal(-1))
          expect(item.quality.value).to(equal(2))
    with description("with quality 50 and sell in 1"):
      with description("when updating it"):
        with it("should have decremented sell in and incremented quality"):
          item = Item("Foo", 1, 52)
          do_update(item)
          expect(item.sell_in).to(equal(0))
          expect(item.quality.value).to(equal(51))

  with description("Given a sulfuras item"):
    with description("with quality and sell in 1"):
      with description("when updating it"):
        with it("should have left sell in and quality unchanged"):
          item = SulfurasItem(1, 1)
          do_update(item)
          expect(item.sell_in).to(equal(1))
          expect(item.quality.value).to(equal(1))

  with description("Given a backstage pass item"):
    with description("with quality and sell in 0"):
      with description("when updating it"):
        with it("should have decremented sell in and left quality unchanged"):
          item = BackstagePassItem(0, 0)
          do_update(item)
          expect(item.sell_in).to(equal(-1))
          expect(item.quality.value).to(equal(0))

  with description("Given a generic item"):
    with description("with quality and sell in 0"):
      with description("when updating it"):
        with it("should have decremented sell in and left quality unchanged"):
          item = Item("Foo", 0, 0)
          do_update(item)
          expect(item.sell_in).to(equal(-1))
          expect(item.quality.value).to(equal(0))
    with description("with quality and sell in 1"):
      with description("when updating it"):
        with it("should have decremented sell in and quality"):
          item = Item("Foo", 1, 1)
          do_update(item)
          expect(item.sell_in).to(equal(0))
          expect(item.quality.value).to(equal(0))

