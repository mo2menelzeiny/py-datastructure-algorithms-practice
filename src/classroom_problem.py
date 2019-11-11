

classes = {
    "ART": (9, 10),
    "ENG": (9.5, 10.5),
    "MATH": (10, 11),
    "CS": (10.5, 11.5),
    "MUSIC": (11, 12)
}


# GREEDY ALGORITHM SOLUTION
def schedule(classes, start, end):
    marker = start
    slots = []
    processed = []
    while marker < end:
        soonest_end = float('inf')
        soonest_class = None
        #  Find soonest ending class
        for class_key in classes.keys():
            if (classes[class_key][1] < soonest_end) and class_key not in processed:
                soonest_class = class_key
                soonest_end = classes[class_key][1]
        #  Check if selected class can start after the end of the last class
        if classes[soonest_class][0] == marker:
            slots.append(soonest_class)
            marker = classes[soonest_class][1]
        processed.append(soonest_class)
    return slots


print(schedule(classes, 9, 12))
