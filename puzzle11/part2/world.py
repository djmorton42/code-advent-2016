from generator import Generator
from microchip import Microchip

class World:
    def __init__(self, generators, microchips, elevator_floor):
        self.generators = generators
        self.microchips = microchips
        self.elevator_floor = elevator_floor
        
        self.item_map_by_abbreviation = {item.abbreviation: item for item in (self.generators + self.microchips)}

    def validate_move(self, item):
        item_to_move = self.item_map_by_abbreviation[item.abbreviation]
        if item_to_move is None:
            raise ValueError('Item ' + item.abbreviation + ' does not exist!')
       
        if item_to_move.floor != self.elevator_floor:
            raise ValueError(
                'Item ' + item.abbreviation + 
                'can not be moved because it is on floor ' + item_to_move.floor + 
                ' and the elevator is on floor ' + self.elevator_floor)

    def move_up(self, item):
        self.validate_move(item)
       
        self.item_map_by_abbreviation[item.abbreviation].move_up()        

    def move_down(self, item):
        self.validate_move(item)
        
        self.item_map_by_abbreviation[item.abbreviation].move_down()

    def clone(self):
        return World(
            [generator.clone() for generator in self.generators],
            [microchip.clone() for microchip in self.microchips],
            self.elevator_floor
        )
    
    def material_agnostic_code(self):
        material_map = {}

        material_map = { 
            generator.material[0]: [generator.floor]
            for generator 
            in self.generators 
        }

        for microchip in self.microchips:
            material_map[microchip.material[0]].append(microchip.floor)

        pairs = [item_pair for item_pair in material_map.values()]

        return str(self.elevator_floor) + ''.join(
            sorted(
                [str(item_pair[0]) + str(item_pair[1]) for item_pair in pairs]
            )
        )

    def get_items(self):
        return self.generators + self.microchips

    def get_items_on_level(self, level):
        return {
            item for item in (self.generators + self.microchips)
                if item.floor == level
        }

    def get_items_on_current_level(self):
        return {
            item for item in (self.generators + self.microchips) 
                if item.floor == self.elevator_floor
        }

    def get_movable_permutations(self):
        movable_items = self.get_items_on_current_level()
        
        permutations = {(movable_item,) for movable_item in movable_items}

        for movable_item in movable_items:
            for other_movable_item in movable_items:
                if movable_item != other_movable_item:
                    if movable_item.code() < other_movable_item.code():
                        permutations.add((movable_item, other_movable_item))
                    else:
                        permutations.add((other_movable_item, movable_item))

        return permutations

    def is_valid(self):
        for floor in range(4):
            generator_materials = {
                generator.material 
                for generator 
                in self.generators 
                if generator.floor == floor
            }

            microchip_materials = {
                microchip.material 
                for microchip 
                in self.microchips 
                if microchip.floor == floor
            }

            generator_materials_without_microchips = (
                generator_materials.difference(microchip_materials)
            )
            microchip_materials_without_generators = (
                microchip_materials.difference(generator_materials)
            )

            if (len(generator_materials_without_microchips) > 0 
                and len(microchip_materials_without_generators) > 0):
                return False

        return True
