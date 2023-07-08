#!/usr/bin/env/python3

from collections import deque

def canUnlockAll(boxes):
    num_boxes = len(boxes)
    visited = set()
    queue = deque([0])  # Start with the first box (index 0)

    while queue:
        box = queue.popleft()
        visited.add(box)

        # Check all the keys in the current box
        for key in boxes[box]:
            if key not in visited and key < num_boxes:
                queue.append(key)

    # Check if all boxes have been visited
    return len(visited) == num_boxes
