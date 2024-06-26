import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

def find_closest_index(liste, target):
    array = np.array(liste)
    difference_array = np.abs(array - target)
    index_of_closest = np.argmin(difference_array)
    return index_of_closest

def from_step_to_route(steps : list, houses :list):
    index = np.argmin(np.abs(houses))
    route = [] 
    c = 0
    #print("Steps: ", steps )
    for step in steps:
        index_goal = find_closest_index(houses, step)
        goal = houses[index_goal]
        while index < len(houses) and houses[index] != goal:
            if houses[index] < goal:
                route.append(houses[index])
                # print("index: ", index, " houses[index]: ", houses[index], " c: ",c, "step " , goal)
                c = c + 1
                houses = np.delete(houses, index)
                if index >= len(houses):
                    break
            else:
                route.append(houses[index])
                houses = np.delete(houses, index)
                index = index - 1
                if index < 0:
                    break
    route.append(goal)
    return route

def from_step_to_route(steps : list, houses :list):
    index = np.argmin(np.abs(houses))
    route = [] 
    c = 0

    for step in steps:
        index_goal = find_closest_index(houses, step)
        goal = houses[index_goal]
        while index < len(houses) and houses[index] != goal:
        #    print("Index: ", index, " House: ", houses[index])
            if index < len(houses) and index >= 0 and houses[index] == goal:
         #       print("Append House goal: ", goal)    
                route.append(goal)
                houses = np.delete(houses, index)
            if houses[index] < goal:
         #       print("Append House: ", houses[index])
                route.append(houses[index])
                # print("index: ", index, " houses[index]: ", houses[index], " c: ",c, "step " , goal)
                #c = c + 1
                houses = np.delete(houses, index)
                if index >= len(houses):
                    break
            else:
         #       print("Append House: ", houses[index])
                route.append(houses[index])
                houses = np.delete(houses, index)
                index = index - 1
                if index < 0:
                    break
        if index < len(houses) and index >= 0 and houses[index] == goal:
         #   print("Append House goal: ", goal)    
            route.append(goal)
            houses = np.delete(houses, index)
         #   print ("c , len(steps): ", c, len(steps))
            if c >= (len(steps) -1):
                break
            if steps[c + 1] < goal and index > 0:
                index = index - 1
        c+=1
    if len(houses) > 0:
        print("Strange route building")
        if route[-1] < houses[0]:
            for h in  houses:
                route.append(houses)
        else:
            for h in  houses[::-1] :
                route.append(h)
    return route

test = from_step_to_route([-1,4],[-2,-1,0,1, 2, 3, 4, 5] )
print(test)