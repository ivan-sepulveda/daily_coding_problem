input_array_a = [3, 7, 5, 6, 9]

def find_smallest_window_using_sorted_copy(input_array):
    start, end = None, None  # By Default, use none because we can check for the is None condition
    s = sorted(input_array)
    for i in range(len(input_array)):
        #print("i = {}".format(i))
        curr_elem_input = input_array[i]
        curr_elem_sorted = s[i]
        #print("\tcurrent elem input: {}".format(curr_elem_input))
        #print("\tcurrent elem sorted: {}".format(curr_elem_sorted))
        # First we need to find the start
        if curr_elem_input != curr_elem_sorted and start is None:
            #print("\t\tsetting left")
            start = i
            # Once that's found and set we can find the end
        elif curr_elem_input != curr_elem_sorted:
            #print("\t\tsetting right")
            end = i
    return start, end

print(find_smallest_window_using_sorted_copy(input_array_a))


def find_smallest_window_without_copy(input_array):
    start, end = None, None
    num_elements = len(input_array)
    max_seen = -float("inf")
    min_seen = float("inf")

    # in this manner we can either find the start or the end index first, doesn't matter
    # to prove this, let's find the max first
    for i in range(num_elements):
        max_seen = max(max_seen, input_array[i])
        if input_array[i] < max_seen:
            end = i # because we want the LAST element that UNSORTED (here, less than the max seen so far)

    #print("looking for min")

    for i in range(num_elements - 1, -1, -1): # traversing the array backwards
        #print("\tCurrent index: {}".format(i))
        #print("\tmin seen so far: {}".format(min_seen))
        #print("\tcurrent element: {}".format(input_array[i]))
        min_seen = min(min_seen, input_array[i])
        if input_array[i] > min_seen:
            start = i

    return start, end

print(find_smallest_window_without_copy(input_array_a))



def find_smallest_window_one_traversal(input_array):
    start, end = None, None
    num_elements = len(input_array)
    max_seen = -float("inf")
    min_seen = float("inf")

    # in this manner we can either find the start or the end index first, doesn't matter
    # to prove this, let's find the max first
    for i in range(num_elements):
        max_seen = max(max_seen, input_array[i])
        if input_array[i] < max_seen:
            end = i # because we want the LAST element that UNSORTED (here, less than the max seen so far)

        j = num_elements - 1 - i
        min_seen = min(min_seen, input_array[j])
        if input_array[j] > min_seen:
            start = j



    return start, end


print(find_smallest_window_one_traversal(input_array_a))



