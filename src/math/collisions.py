def is_box_collision(a, b):
    """
    Checks if 2 2d-boxes a and b collide. Have to be in form y1, x1, y2, x2. Point 1 in bottom left. Point 2 is top right
    """
    ax1 = a[0]
    ay1 = a[1]
    ax2 = a[2]
    ay2 = a[3]

    bx1 = b[0]
    by1 = b[1]
    bx2 = b[2]
    by2 = b[3]

    if is_line_collision((ax1, ax2), (bx1, bx2)) and is_line_collision((ay1, ay2), (by1, by2)):
        return True
    return False



def is_line_collision(a, b):
    """
    Checks if 2 1d-lines a and b collide. Have to be in form a1 a2. Point 1 in bottom left. Point 2 is top right
    """
    a1 = a[0]
    a2 = a[1]

    b1 = b[0]
    b2 = b[1]

    if a1 < b1 and a1 < b2 and a2 < b1 and a2 < b2:
        return False
    if a1 > b1 and a1 > b2 and a2 > b1 and a2 > b2:
        return False

    """
    if a2 >= b1 and a1 <= b2:
        return True
    if b2 >= a1 and b1 <= a2:
        return True
    """
    return True