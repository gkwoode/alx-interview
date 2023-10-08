#!/usr/bin/python3
"""Lock boxes code"""


def canUnlockAll(boxes):
    """Lock boxes function"""

    if not boxes:
        return False

    # Create a list to track the state of each box (locked or unlocked)
    # Initialize all boxes as locked (False)
    unlocked_boxes = [False] * len(boxes)
    unlocked_boxes[0] = True  # The first box is initially unlocked

    # Create a list to store the keys found
    keys = [0]  # Start with the keys in the first box

    # Use a while loop to explore and unlock boxes
    while keys:
        current_box = keys.pop()  # Get the current box
        for key in boxes[current_box]:

            if key >= 0 and key < len(boxes) and not unlocked_boxes[key]:
                unlocked_boxes[key] = True  # Unlock the box
                keys.append(key)

    # Check if all boxes are unlocked
    return all(unlocked_boxes)
