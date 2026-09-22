item_num_base = 200000
current_crop = Entities.Grass
if num_items(Items.Hay) >= num_items(Items.Wood):
	current_crop = Entities.Tree
elif num_items(Items.Wood) >= num_items(Items.Carrot):
	current_crop = Entities.Carrot
elif num_items(Items.Carrot) >= num_items(Items.Pumpkin):
	current_crop = Entities.Pumpkin
	
ground_types_of_plants = {
							Entities.Grass:Grounds.Grassland, 
							Entities.Bush:Grounds.Grassland,
							Entities.Tree:Grounds.Grassland, 
							Entities.Carrot:Grounds.Soil, 
							Entities.Pumpkin:Grounds.Soil
						 }
# --------------- methods ---------------
def is_even(n):
	return n % 2 == 0
def is_tree_placeble():
	if is_even(get_pos_y() + get_pos_x()):
		return True
	else:
		return False
def home():
	x, y = get_pos_x(), get_pos_y()
	for i in range(x):
		move(West)
	for i in range(y):
		move(South)
def pour_water(level):
	if get_water() <= level:
		use_item(Items.Water)
def plant_crop(entities, ground_type):
		pour_water(0.5)
		use_item(Items.Weird_Substance)
		harvest()
		current_crop = entities
		if get_ground_type() != ground_type:
			till()
		if current_crop == Entities.Tree and is_tree_placeble() == False:
			plant(Entities.Bush)
			return
		plant(entities)
		if entities == Entities.Pumpkin:
			use_item(Items.Fertilizer)
def check_pumpkin_is_healthy(direction):
	while True:
		if get_entity_type() == Entities.Dead_Pumpkin:
			plant(Entities.Pumpkin)
		elif can_harvest() and get_entity_type() == Entities.Pumpkin:
			move(direction)
			break
def plant_crop_and_move(entities, direction):
	plant_crop(entities, ground_types_of_plants[entities])
	if get_entity_type() != Entities.Pumpkin:
		move(direction)
	else:
		check_pumpkin_is_healthy(direction)
# --------------- main program ---------------
home()
while True:
	if can_harvest() and num_items(Items.Hay) <= item_num_base:
		for i in range(get_world_size()):
			plant_crop_and_move(Entities.Grass, North)	
		move(East)	
	elif can_harvest() and num_items(Items.Wood) <= item_num_base:
		for i in range(get_world_size()):
			plant_crop_and_move(Entities.Tree, North)
		move(East)
	elif can_harvest() and num_items(Items.Carrot) <= item_num_base:
		for i in range(get_world_size()):
			plant_crop_and_move(Entities.Carrot, North)
		move(East)
	elif can_harvest() and num_items(Items.Pumpkin) != item_num_base:
		for i in range(get_world_size()):
			plant_crop_and_move(Entities.Pumpkin, North)
		move(East)
	else:
		plant_crop_and_move(current_crop, North)
