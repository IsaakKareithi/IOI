# Search list and target value
tour_locations = ["New York City", "Los Angeles", "Bangkok","Instanbul", "London", "New York City", 'Toronto']
target_city = 'New York City'

#Linear Search Algorithms
def linear_search(search_list, target_value):
    matches = []
    for idx in range(len(search_list)):
        if search_list[idx] == target_value:
            #if target found in the list
            #add index in matches list
            matches.append(idx)

    # If the element is not in matches list
    # Raise an error
    if not matches:
        ValueError("{} is not in the list".format(target_value))
    #Otherwise return the matches list
    # with indexes