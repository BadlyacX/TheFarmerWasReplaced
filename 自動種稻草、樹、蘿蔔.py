item_num_base = 1200
# --------------- methods ---------------
def is_even(n):
	return n % 2 == 0
def is_tree_placeble():
	if is_even(get_pos_y() + get_pos_x()):
		return True
	else:
		return False
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
# --------------- main program ---------------
while True:
	if can_harvest():
		if num_items(Items.Hay) <= item_num_base:
			for i in range(get_world_size()):
				plant_crop_and_move(Entities.Grass, Grounds.Grassland, North)	
			move(East)	
		elif num_items(Items.Wood) <= item_num_base:
			for i in range(get_world_size()):
				if is_tree_placeble():
					plant_crop_and_move(Entities.Tree, Grounds.Grassland, North)
				else:
					plant_crop_and_move(Entities.Bush, Grounds.Grassland, North)
			move(East)
		else:
			for i in range(get_world_size()):
				plant_crop_and_move(Entities.Carrot, Grounds.Soil, North)
			move(East)
