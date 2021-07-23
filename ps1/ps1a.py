###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    cow_data = open("ps1_cow_data.txt")
    cows = {}
    for line in cow_data:
        line = line.replace("\n","")
        cow = line.split(",")
        cows[cow[0]] = int(cow[1])
    return cows


# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    trip = 0
    weight = 0
    trip_list = []
    sorted_cows = sorted(cows.items(), key=lambda x:x[1] ,reverse=True)
    cows_copy = sorted_cows.copy()
    transport_list = []
    while len(cows_copy) > 0:
        for cow in sorted_cows:
            if cow in cows_copy:
                if weight + (cow[1]) <= limit:
                    transport_list.append(cow[0])
                    weight += (cow[1])
                    cows_copy.remove(cow)
        weight = 0
        trip += 1
        trip_list.append(transport_list)
        transport_list = []
    return trip_list



# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # cow_set = []
    # for cow in cows:
    #   cow_data = (cow,cows[cow])
    #    cow_set.append(cow_data)
    accepted_trip = []
    best_trip = []
    overweight = False
    min_len = 10
    for partition in get_partitions(cows):
        for cow_list in partition:
            weight = 0
            for cow in cow_list:
                if cows[cow] + weight > limit:
                    overweight = True
                    break
                else:
                    weight += cows[cow]
        if not overweight:
            accepted_trip.append(partition)
        else:
            overweight = False
    for trip in accepted_trip:
        curr_len = len(trip)
        if curr_len < min_len:
            min_len = curr_len
            best_trip = trip
    return best_trip

        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.time()
    trip_num = len(brute_force_cow_transport(cows))
    end = time.time()
    time_taken1 = end - start
    start2 = time.time()
    trip_num2 = len(greedy_cow_transport(cows))
    end2 = time.time()
    time_taken2 = end2 - start2
    print(f"Greedy cow transport took {time_taken2}s long,the amount of trip made is {trip_num2} ")
    print(f"Bruteforce cow transport took {time_taken1}s long,the amount of trip made is {trip_num} ")


if __name__ == '__main__':
    filename = "ps1_cow_data.txt"
    cows = load_cows(filename)
    compare_cow_transport_algorithms()
