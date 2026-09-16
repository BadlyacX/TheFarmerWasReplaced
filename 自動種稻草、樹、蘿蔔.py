while True:
	if can_harvest():
		if num_items(Items.Hay) <= 500:
			for i in range(get_world_size()):
				
				if get_water() <= 0.50:
					use_item(Items.Water)
				
				harvest()
				if get_ground_type() != Grounds.Grassland:
					till()
				move(North)
			move(East)
			
		elif num_items(Items.Wood) <= 500:
			for i in range(get_world_size()):
					
				if get_water() <= 0.50:
					use_item(Items.Water)
				
				harvest()
				if get_ground_type() != Grounds.Grassland:
					till()
				plant(Entities.Bush)
				move(North)
			move(East)

		else:
			for i in range(get_world_size()):
				
				if get_water() <= 0.50:
					use_item(Items.Water)
				
				harvest()
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Carrot)
				move(North)
			move(East)
			
			
