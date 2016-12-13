import unittest
from world import World
from generator import Generator
from microchip import Microchip

class TestWorld(unittest.TestCase):

    def test_get_movable_permutations(self):
        generator1 = Generator('Plutonium', 1)
        generator2 = Generator('Strontium', 1)
        microchip1 = Microchip('Thorium', 1)
        microchip2 = Microchip('Curium', 1)

        world = World(
            [generator1, generator2],
            [microchip1, microchip2],
            1
        )

        movable_permutations = world.get_movable_permutations()
        
        self.assertEqual(len(movable_permutations), 10)
        self.assertTrue((generator1) in movable_permutations)
        self.assertTrue((generator2) in movable_permutations)
        self.assertTrue((microchip1) in movable_permutations)
        self.assertTrue((microchip2) in movable_permutations)
        self.assertTrue((generator1, generator2) in movable_permutations)
        self.assertTrue((generator1, microchip1) in movable_permutations)
        self.assertTrue((microchip2, generator1) in movable_permutations)
        self.assertTrue((generator2, microchip1) in movable_permutations)
        self.assertTrue((microchip2, generator2) in movable_permutations)
        self.assertTrue((microchip2, microchip1) in movable_permutations)

    def test_get_items_on_current_level(self):
        world = World(
            [Generator('Plutonium', 1), Generator('Thorium', 2), Generator('Curium', 1)],
            [Microchip('Strontium', 1), Microchip('Curium', 1), Microchip('Blahium', 2)], 
            1
        )

        self.assertEquals(
            ['CG1', 'CM1', 'PG1', 'SM1'], 
            sorted(
                [item.code() for item in world.get_items_on_current_level()]
            )
        )
        
        world.elevator_floor = 2

        self.assertEquals(
            ['BM2', 'TG2'],
            sorted(
                [item.code() for item in world.get_items_on_current_level()]
            )
        )

    def test_is_valid_when_has_different_kinds_of_generators_only_on_floor_should_return_true(self):
        world = World(
            [Generator('Plutonium', 1), Generator('Strontium', 1)], 
            [], 
            1
        )

        self.assertTrue(world.is_valid())

    def test_is_valid_when_has_different_kinds_of_microchips_only_on_floor_should_return_true(self):
        world = World(
            [],
            [Microchip('Plutonium', 1), Microchip('Strontium', 1)], 
            1
        )

        self.assertTrue(world.is_valid())

    def test_is_valid_when_generator_and_corresponding_microchip_are_only_things_on_floor_should_return_true(self):
        world = World(
            [Generator('Plutonium', 1)],
            [Microchip('Plutonium', 1)], 
            1
        )

        self.assertTrue(world.is_valid())
    
    def test_is_valid_when_generator_and_different_microchip_are_only_things_on_floor_should_return_false(self):
        world = World(
            [Generator('Plutonium', 1)],
            [Microchip('Strontium', 1)], 
            1
        )

        self.assertFalse(world.is_valid())
    
    def test_is_valid_when_generator_and_different_microchip_are_on_different_floors_should_should_return_true(self):
        world = World(
            [Generator('Plutonium', 1)],
            [Microchip('Strontium', 2)], 
            1
        )

        self.assertTrue(world.is_valid())

    def test_is_valid_when_generator_and_matching_microchip_are_present_with_different_microchip_should_return_true(self):
        world = World(
            [Generator('Plutonium', 1)],
            [Microchip('Plutonium', 1), Microchip('Strontium', 1)], 
            1
        )

        self.assertTrue(world.is_valid())

    def test_is_valid_when_generator_and_matching_microchip_are_present_with_different_generator_should_return_true(self):
        world = World(
            [Generator('Plutonium', 1), Generator('Strontium', 1)],
            [Microchip('Plutonium', 1)], 
            1
        )

    def test_is_valid_when_generator_and_matching_microchip_are_present_with_non_matching_generator_and_chip_returns_false(self):
        world = World(
            [Generator('Plutonium', 1), Generator('Strontium', 1)],
            [Microchip('Plutonium', 1), Microchip('Thorium', 1)], 
            1
        )
        self.assertFalse(world.is_valid())

if __name__ == '__main__':
    unittest.main()

