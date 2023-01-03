def canUnlockAll(boxes):
    unlocked_boxes = set([0]) 
 # Set of unlocked boxes
    keys_to_check = boxes[0]  
# Keys to check in the current iteration
    while keys_to_check:
  # While there are keys to check
        key = keys_to_check.pop()
  # Get a key
        if key < len(boxes) and key not in unlocked_boxes:  # If the key corresponds to a valid box and the box is not yet unlocked
            unlocked_boxes.add(key) 
 # Unlock the box
            keys_to_check += boxes[key] 
 # Add the keys in the newly unlocked box to the keys to check
    return len(unlocked_boxes) == len(boxes)  # Return True if all boxes are unlocked, False otherwise
