'''
Question: 
    There are a list of boxes and a list of containers. Both, the boxes and containers, are of variable
    sizes.

    Size of boxes are given in an array called box_array, of size B.
    Similarly, size of containers is given in an array called container_array, of size C.

    Boxes fit into the containers in the following manner:

        The container with the same index number of the box is checked first. For example, the box at index 4 will check the size of container at index 4.
        If it does not fit, the size of next container is checked towards right till the end of container array.
        Once a box is fit into a container, the container cannot be occupied again.

    Return the index of the box that first reaches the end of the container array
'''

def allow_move_down(array, index):

    if (len(array)-1 >= index):
        return True
    else:
        return False

def fill_container(container_array, container_index):

    container_array[container_index] = True
    return container_array

def check_container_space(container, box):

    if ( (not (container is True)) and (box <= container) ):
        return True
    else:
        return False

def check_container_array(container_array, cut_container, box):

    for container in container_array[cut_container:]:

        if (check_container_space(container,box)):

            container_index = container_array.index(container)
            return container_index

    return False 

def Solution(container_array, box_array,):
    
    valueToReturn = -1
    
    for box_index, box in enumerate(box_array, start=0):
        
        if ( allow_move_down(container_array, box_index) and check_container_space(container_array[box_index], box_array[box_index]) ):
            container_array = fill_container(container_array, box_index)

        else:

            space_in_container = check_container_array(container_array, box_index+1, box)

            if ( not (space_in_container is False) ):

                container_index = space_in_container
                container_array = fill_container(container_array, container_index)

            else:
                valueToReturn = box_index +1
                return valueToReturn
        
    return valueToReturn

#Test case 1. Expected output: 3
prueba1_box = [1, 3, 4, 5]
prueba1_container = [4, 2, 3, 2, 1]

#Test case 2. Expected output: -1
prueba2_box = [6,11]  
prueba2_container = [6,12,5,12]

#Test case 3. Expected output: 4
prueba3_box = [9,4,3,11]  
prueba3_container = [6,4,12]

#Test case 4. Expected output: 4
prueba4_box = [4,11,7,11,7]  
prueba4_container = [3,13,12,5,10]

#Test case 5. Expected output: 5
prueba5_box = [9,7,3,9,9]  
prueba5_container = [7,5,13,7,12,5]

#Test case 6. Expected output: 3
prueba6_box = [9,3,12,13,2,14]  
prueba6_container = [13,9,6,10,11,10,11]

box_array = prueba5_box
b = len(box_array)
container_array = prueba5_container
c = len(container_array)

print("R/",Solution(container_array, box_array))