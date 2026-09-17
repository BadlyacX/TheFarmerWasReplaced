item_num_base = 1000

def is_even(n):
	return n % 2 == 0

def pour_water(level):
	if get_water() <= level:
		use_item(Items.Water)
		
def plant_crop_and_move(entities, ground_type, direction):
		pour_water(0.5)
		harvest()
		if get_ground_type() != ground_type:
			till()
		plant(entities)
		move(direction)

while True:
	if can_harvest():
		if num_items(Items.Hay) <= item_num_base:
			for i in range(get_world_size()):
				plant_crop_and_move(Entities.Grass, Grounds.Grassland, North)	
			move(East)
			
		elif num_items(Items.Wood) <= item_num_base:
			for i in range(get_world_size()):
				plant_crop_and_move(Entities.Bush, Grounds.Grassland, North)
			move(East)
		else:
			for i in range(get_world_size()):
				plant_crop_and_move(Entities.Carrot, Grounds.Soil, North)
			move(East)
