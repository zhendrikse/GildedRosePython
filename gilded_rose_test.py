import unittest
from approvaltests.approvals import verify
from gilded_rose import Item, GildedRose

class GettingStartedTest(unittest.TestCase):
  def test_main(self):
      items = [
        Item(name='+5 Dexterity Vest', sell_in=10, quality=20),
        #Item(name='Aged Brie', sell_in=2, quality=0),
      ]
      GildedRose(items).update_quality()
      result = items
      verify(result)

if __name__ == "__main__":
    unittest.main()


# 
# S O L U T I O N
#
# def main():
#     items = [
#         Item(name='+5 Dexterity Vest', sell_in=10, quality=20),
#         Item(name='Aged Brie', sell_in=2, quality=0),
#         Item(name='Elixir of the Mongoose', sell_in=5, quality=7),
#         Item(name='Sulfuras, Hand of Ragnaros', sell_in=0, quality=80),
#         Item(name='Sulfuras, Hand of Ragnaros', sell_in=-1, quality=80),
#         Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=15, quality=20),
#         Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=10, quality=49),
#         Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=5, quality=49),
#         Item(name='Conjured Mana Cake', sell_in=3, quality=6),  # <-- :O
#     ]

#     days = 30
#     for day in range(days+1):
#         print('-------- day {} --------'.format(day))
#         print('name, sellIn, quality')
#         for item in items:
#             print(item)
#         print('')
#         GildedRose(items).update_quality()