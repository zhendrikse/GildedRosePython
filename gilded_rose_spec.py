from mamba import description, it, context, before
from expects import expect, equal, raise_error
from gilded_rose import GildedRose, SulfurasItem, Item

def do_update(item: Item):
    app = GildedRose([item])
    app.update_quality()

with description(GildedRose) as self:

  with description("Given a generic item"):
    with context("with quality and sell in 0"):
      with before.each:
          self.item = Item("Foo", 0, 0)
          do_update(self.item)
        
      with context("when updating it"):
        with it("should have decreased the sell by 1"):
          expect(self.item.sell_in).to(equal(-1))
        with it("should have left the quality unchanged"):
          expect(self.item.quality.value).to(equal(0))
  
    with context("with quality and sell in 1"):
      with before.each:
          self.item = Item("Foo", 1, 1)
          do_update(self.item)
        
      with context("when updating it"):
        with it("should have decreased the sell by 1"):
          expect(self.item.sell_in).to(equal(0))
        with it("should have decreased the quality by 1"):
          expect(self.item.quality.value).to(equal(0))

  with context("Given a Sulfuras item"):
    with before.each:
        self.item = SulfurasItem(11, 47)
        do_update(self.item)
      
    with context("when updating it"):
      with it("should have left the sell in unchanged"):
        expect(self.item.sell_in).to(equal(11))
      with it("should have left the quality unchanged"):
        expect(self.item.quality.value).to(equal(47))
