from mamba import description, it, context, before
from expects import expect, equal, raise_error
from gilded_rose import GildedRose, SulfurasItem, Item

def do_update(item: Item):
    app = GildedRose([item])
    app.update_quality()

with description(GildedRose) as self:

  with description("Given a sulfuras item"):
    with description("with quality and sell in 1"):
      with description("when updating it"):
        with it("should have left sell in and quality unchanged"):
          item = SulfurasItem(1, 1)
          do_update(item)
          expect(item.sell_in).to(equal(1))
          expect(item.quality.value).to(equal(1))

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

