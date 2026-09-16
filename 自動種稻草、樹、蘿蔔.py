def pour_water(level):
	if get_water() <= level:
		use_item(Items.Water)

while True:
	if can_harvest():
		if num_items(Items.Hay) <= 500:
			for i in range(get_world_size()):
				
				pour_water(0.5)
				
				harvest()
				if get_ground_type() != Grounds.Grassland:
					till()
				move(North)
			move(East)
			
		elif num_items(Items.Wood) <= 500:
			for i in range(get_world_size()):
					
				pour_water(0.5)
				
				harvest()
				if get_ground_type() != Grounds.Grassland:
					till()
				plant(Entities.Bush)
				move(North)
			move(East)

		else:
			for i in range(get_world_size()):
				
				pour_water(0.5)
				
				harvest()
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Carrot)
				move(North)
			move(East)
			
