#  *******************************************************************************************************************************************************************************************************************************************************************************************************************************
#  *                                                                        YOUR MISSION HERE IS TO CREATE A FUNCTION THAT GETS A TUPLE AND RETURNS A TUPLE WITH ONLY 3 ELEMENTS - THE FIRST, THIRD AND SECOND ELEMENT FROM THE LAST FOR THE GIVEN TUPLE.                                                                        *
#  * ONE IMPORTANT THING WORTH POINTING OUT IS THAT YOU NEED TO USE INDEX IN ORDER TO EXTRACT ELEMENTS FROM THE TUPLE. PAY ATTENTION, INDEX COUNTING STARTS FROM 0, NOT FROM 1. WHICH MEANS THAT IF YOU NEED TO GET THE FIRST ELEMENT FROM THE TUPLE ELEMENTS, YOU SHOULD DO ELEMENTS[0], AND THE SECOND ELEMENT IS ELEMENTS[1]. *
#  *                                                                                                                                         DEF EASY_UNPACK(ELEMENTS: TUPLE) -> TUPLE:                                                                                                                                          *
#  *******************************************************************************************************************************************************************************************************************************************************************************************************************************/
    # your code here
def easy_unpack(elements: tuple) -> tuple:
    # Extract the first, third, and second elements from the last. 
    first, third, second = elements[0], elements[2], elements[-1]
    unpacked = (first, third, second) 
    
    return unpacked

