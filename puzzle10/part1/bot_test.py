import unittest
from bot import Bot

class TestBot(unittest.TestCase):

    def test_constructor(self):
        bot = Bot(10)

        self.assertEqual(bot.bot_id, 10)

    def test_add_chip(self):
        bot = Bot(10)

        self.assertEqual(bot.get_chip_count(), 0)
        
        bot.add_chip(42)

        self.assertEqual(bot.get_chip_count(), 1)
        
        self.assertEqual(bot.get_chip_values(), [42])
       
    def test_pop_high_value_chip(self):
        bot = Bot(10)

        bot.add_chip(42)
        bot.add_chip(15)

        self.assertEqual(bot.get_chip_count(), 2)
        self.assertEqual(bot.get_chip_values(), [15, 42])

        self.assertEqual(bot.pop_high_value_chip(), 42)

        self.assertEqual(bot.get_chip_count(), 1)
        self.assertEqual(bot.get_chip_values(), [15])
    
    def test_pop_high_value_chip_with_1_value(self):
        bot = Bot(10)

        bot.add_chip(15)

        self.assertEqual(bot.pop_high_value_chip(), 15)

        self.assertEqual(bot.get_chip_count(), 0)
        self.assertEqual(bot.get_chip_values(), [])

    def test_pop_low_value_chip(self):
        bot = Bot(10)

        bot.add_chip(42)
        bot.add_chip(15)

        self.assertEqual(bot.get_chip_count(), 2)
        self.assertEqual(bot.get_chip_values(), [15, 42])

        self.assertEqual(bot.pop_low_value_chip(), 15)

        self.assertEqual(bot.get_chip_count(), 1)
        self.assertEqual(bot.get_chip_values(), [42])
    
    def test_pop_low_value_chip_with_1_value(self):
        bot = Bot(10)

        bot.add_chip(15)

        self.assertEqual(bot.pop_low_value_chip(), 15)

        self.assertEqual(bot.get_chip_count(), 0)
        self.assertEqual(bot.get_chip_values(), [])

    def test_responsible_for(self):
        bot = Bot(10)

        bot.add_chip(42)
        bot.add_chip(15)

        self.assertTrue(bot.responsible_for([15, 42]))

    def test_give_ships(self):
        bot = Bot(10)
        high_bot = Bot(20)
        low_bot = Bot(30)

        bot.set_give_high_rule(high_bot)
        bot.set_give_low_rule(low_bot)

        bot.add_chip(42)
        bot.add_chip(63)

        bot.give_chips()

        self.assertEqual(bot.get_chip_count(), 0)

        self.assertEqual(high_bot.get_chip_count(), 1)
        self.assertEqual(high_bot.get_chip_values(), [63])

        self.assertEqual(low_bot.get_chip_count(), 1)
        self.assertEqual(low_bot.get_chip_values(), [42])

if __name__ == '__main__':
    unittest.main()

