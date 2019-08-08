def cost_of_ground(weight):
  if 2 >= weight:
    cost = 20 + (weight * 1.5)
    return cost
  elif 6 >= weight:
    cost = 20 + (weight * 3)
    return cost
  elif 10 >= weight:
    cost = 20 + (weight * 4)
    return cost
  else:
    cost = 20 + (weight * 4.75)
    return cost
  
cost_of_premium_ground = 125.00

def cost_of_drone(weight):
  if 2 >= weight:
    cost = weight * 4.5
    return cost
  elif 6 >= weight:
    cost = weight * 9
    return cost
  elif 10 >= weight:
    cost = weight * 12
    return cost
  else:
    cost = weight * 14.25
    return cost

def cost(weight):
  if cost_of_ground(weight) < cost_of_premium_ground and cost_of_ground(weight) < cost_of_drone(weight):
    print("The cheapest shipping method is ground for {}".format(cost_of_ground(weight)))
  elif cost_of_drone(weight) < cost_of_ground(weight) and cost_of_drone(weight) < cost_of_premium_ground:
    print("The cheapest shipping method is drone for {}".format(cost_of_drone(weight)))
  else:
    print("The cheapest shipping method is premium for {}".format(125))
    
cost(4.8)
cost(41.5)