#!/usr/bin/python3
'''LockBoxes Challenge'''
def canUnlockAll(boxes):
    '''determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    '''

    unlocked = [0]
    if (type(boxes) is not list):
        return False
    for i in range(len(boxes)):
        if (type(boxes[i]) is not list):
            return False
        for j in boxes[i]:
            if (j == i):
                continue
            if j not in unlocked:
                unlocked.append(j)
    
    if (len(unlocked) != len(boxes)):
       return False
        
    
    
     
    return True