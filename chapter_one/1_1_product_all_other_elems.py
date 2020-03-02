input_array_a = [1, 2, 3, 4, 5]
expected_output_a = [120, 60, 40, 30, 24]

input_array_b = [3, 2, 1]
expected_output_b = [2, 3, 6]


def products(input_array):
    # Using division
    # First iteration
    whole_array_product = 1
    for elem in input_array:
        whole_array_product = whole_array_product*elem

    output = []

    for elem in input_array:
        output.append(int(whole_array_product/elem))

    return output

def products_no_div(input_array):
    # NOT using division
    # First iteration
    # This solution is out of the book. I do not lay claim to any credit whatsoever.
    # By coding it myself, I better understood the logic.
    prefix_products = []
    for elem in input_array:
        print(elem)
        """
        On the first element, the for loop will go to the else statement and append this element to prefix_products
        For all other elements, the for loop will go to the if statement and append the product of the last element
            in the list to the current element. 
            
        For example, given input_array_b = [3, 2, 1], so this for loop will iterate from i = 0 to i = 2
        
        i=0: First, the for loop will add 3 to prefix_products.
            Start: Current element: 3
            
        i=1: Second, the for loop will add 3*2 to prefix_products.
            Start: prefix_products = [3], current element: 2
            End:   prefix_products = [3, 6]
            
        i=2: Second, the for loop will add  to prefix_products.
            Start: prefix_products = [3, 6], current element: 1
            End:   prefix_products = [3, 6, 6]
        """

        if len(prefix_products) > 0:
            prefix_products.append(prefix_products[-1] * elem)
        else:
            prefix_products.append(elem)

    print(prefix_products)

    """
    No we iterated over the reversed input array. So below, when I say "first element", that really means
    input_array[-1]. I don't refer to a 'last element', but if I did that would refer to input_array[0].
    
    On the first element, the for loop will go to the else statement and append this element to prefix_products
    For all other elements, the for loop will go to the if statement and append the product of the last element
        in the list to the current element. 

    For example, given input_array_b = [3, 2, 1], so this for loop will iterate from i = 0 to i = 2

    i=0: First, the for loop will add 3 to prefix_products.
        Start: Current element: 3

    i=1: Second, the for loop will add 3*2 to prefix_products.
        Start: prefix_products = [3], current element: 2
        End:   prefix_products = [3, 6]

    i=2: Second, the for loop will add  to prefix_products.
        Start: prefix_products = [3, 6], current element: 1
        End:   prefix_products = [3, 6, 6]
    """
    suffix_products = []
    for elem in reversed(input_array):
        if len(suffix_products) > 0:
            suffix_products.append(suffix_products[-1] * elem)
        else:
            suffix_products.append(elem)
    suffix_products = list(reversed(suffix_products))
    print(suffix_products)
    result = []
    for i in range(len(input_array)):
        if i == 0:
            result.append(suffix_products[i+1])
        elif i == len(input_array) - 1:
            result.append(prefix_products[i-1])
        else:
            result.append(prefix_products[i-1] * suffix_products[i+1])

    return result



print(products_no_div(input_array_a))
