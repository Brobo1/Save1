def planter(plantType):
    if (get_ground_type() != Grounds.Soil 
    and (plantType == Entities.Carrot
         or plantType == Entities.Pumpkin)):
        till()

    if (get_ground_type() != Grounds.Grassland 
    and plantType == Entities.Grass):
        till()

    if can_harvest():
        harvest()

    if get_entity_type() != plantType:
        plant(plantType)