# main
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde


def plot_kde_and_derivative(liste, std_dev, n_points):
    # Calculate the KDE
    kde = gaussian_kde(liste, bw_method=1)
    
    # Set the range for x based on the standard deviation
    range_factor = 3  # This determines how many standard deviations to consider
    x_min = min(liste) 
    x_max = max(liste) 
    x = np.linspace(x_min, x_max, n_points)
    
    kde_values = kde(x)
    
    # Calculate the derivative of the KDE
    kde_derivative = np.gradient(kde_values, x)

    min_derivative = np.min(kde_derivative)
    max_derivative = np.max(kde_derivative)
    kde_derivative_min = np.min(kde_derivative)
    kde_derivative_max = np.max(kde_derivative)
    x_min_derivative = x[np.argmin(kde_derivative)]
    x_max_derivative = x[np.argmax(kde_derivative)]

    #get x value of min and max derivative
    min_derivative_x = x[np.argmin(kde_derivative)]
    max_derivative_x = x[np.argmax(kde_derivative)]
    print("min_derivative_x: ", min_derivative_x , " min_derivative: ", min_derivative)    
    print("max_derivative_x: ", max_derivative_x , " max_derivative: ", max_derivative)
    # Plot the KDE
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.kdeplot(liste, bw_adjust=1)
    plt.title('KDE Plot of House Positions')
    plt.xlabel('Position')
    plt.ylabel('Density')
    plt.tight_layout()
    #plt.legend()
    
    # Plot the derivative of the KDE
    plt.subplot(1, 2, 2)
    plt.plot(x, kde_derivative, label='KDE Derivative', color='red')
    plt.title('Derivative of KDE')
    plt.scatter([x_min_derivative, x_max_derivative], [kde_derivative_min, kde_derivative_max], color='blue', zorder=5)
    plt.text(x_min_derivative, kde_derivative_min, f'{x_min_derivative:.2f}', ha='center', va='top')
    plt.text(x_max_derivative, kde_derivative_max, f'{x_max_derivative:.2f}', ha='center', va='bottom')
    plt.xlabel('Position')
    plt.ylabel('Density Derivative')
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    
def calculate_average_time(houses : list, n_points : int):
    time = []
    time_spend = 0
    houses.insert(0, 0)
    for i in range(1, len(houses)):
        time_ret = abs(houses[i] - houses[i-1])
        if time_ret > 0:
            time_spend = time_spend + time_ret
            time.append(time_spend)
    mean =np.mean(time)
    print ( "mean time of this route :", mean)
    return mean


def find_closest_index(liste, target):
    array = np.array(liste)
    difference_array = np.abs(array - target)
    index_of_closest = np.argmin(difference_array)
    return index_of_closest

def get_kde(liste, std_dev, n_points):
    kde = gaussian_kde(liste, bw_method=1)
    range_factor = 3  # This determines how many standard deviations to consider
    x_min = min(liste) 
    x_max = max(liste) 
    x = np.linspace(x_min, x_max, n_points)
    kde_values = kde(x)
    # Calculate the derivative of the KDE
    kde_derivative = np.gradient(kde_values, x)
    min_derivative_x = x[np.argmin(kde_derivative)]
    max_derivative_x = x[np.argmax(kde_derivative)]
    return kde_derivative, kde_values, x, min_derivative_x, max_derivative_x


def from_step_to_route(steps : list, houses :list):
    index = np.argmin(np.abs(houses))
    route = [] 
    c = 0
    print("Steps: ", steps )
    for step in steps:
        index_goal = find_closest_index(houses, step)
        goal = houses[index_goal]
        while houses[index] != goal:
            if houses[index] < goal:
                route.append(houses[index])
                # print("index: ", index, " houses[index]: ", houses[index], " c: ",c, "step " , goal)
                c = c + 1
                houses = np.delete(houses, index)
                 #index = index + 1
            else:
                route.append(houses[index])
                houses = np.delete(houses, index)
                index = index - 1
        #route.append(goal)
    return route

def make_simple_route_derivitive(houses : list, std_dev, n_points):
    if len(houses) < 3:
        return "Not enough houses" 
    kde_derivative, kde_values, x, min_derivative_x, max_derivative_x = get_kde(houses, std_dev, n_points)
    value_max = np.max(houses)
    value_min = np.min(houses)
    steps = []
    print("min_derivative_x: ", min_derivative_x)
    print("max_derivative_x: ", max_derivative_x)
    print("value_max: ", value_max)
    print("value_min: ", value_min)
    if abs(min_derivative_x) > max_derivative_x:
        steps.append(min_derivative_x)
        steps.append(value_min)
        steps.append(value_max)
    else:
        steps.append(max_derivative_x)
        steps.append(kde_value_max)
        steps.append(kde_value_min)
    return from_step_to_route(steps, houses)

def frst_refference(houses : list):
    if len(houses) < 3:
        return "Not enough houses" 
    #houses =  np.sort(houses)
    route = []
    i = np.argmin(np.abs(houses))    
    while len(houses) >= 3:
        if i <= 0:
            for j in range(0, len(houses)):
                route.append(houses[j])
            return route
        if i >= len(houses) - 1:
            for j in range(len(houses) - 1, -1, -1):
                route.append(houses[j])
            return route
        if len(houses) > 3:
            route.append(houses[i])
            if (houses[i] - houses[i-1]) > (houses[i + 1] - houses[i]):
                houses = np.delete(houses, i)
                #i = i + 1
            else:
                houses = np.delete(houses, i)
                i = i - 1
        if len(houses) == 3:
            if i == 0:
                route.append(houses[0])
                route.append(houses[1])
                route.append(houses[2])
            elif i == 2:
                route.append(houses[2])
                route.append(houses[1])
                route.append(houses[0])
            else:
                if (houses[i] - houses[i-1]) > (houses[i + 1] - houses[i]):
                    route.append(houses[i])
                    route.append(houses[i+1])
                    route.append(houses[i-1])
                else:
                    route.append(houses[i])
                    route.append(houses[i-1])
                    route.append(houses[i+1])    
            return route

def create_liste(mean=0, std_dev=100, n_points=100):
    liste = np.random.normal(mean, std_dev, n_points)
    liste = np.sort(liste) 
    print(liste)   
    return liste

if __name__ == "__main__":
    mean = 0
    std_dev = 100
    n_points = 100
    range_factor = 3
    resolution = 1000
    
    for i in range(0, 20):
        h = create_liste( mean, std_dev, n_points)
        print(h)
        #plot_kde_and_derivative(h, std_dev, resolution)
        route = frst_refference(h)
        route_s = make_simple_route_derivitive(h, std_dev, n_points)
        print(len(route_s))
        print(len(route))
        print(route_s)
        calculate_average_time(route, n_points)
        calculate_average_time(route_s, n_points)
        #print(get_kde(route, std_dev, n_points))
    #print(route)
