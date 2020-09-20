
def earliest_ancestor(ancestors, starting_node):

    # create queue and add starting node
    q = []
    q.append(starting_node)

    # return length of list based on if starting node has children
    has_child = len([True for x in range(len(ancestors)) if ancestors[x][1]==starting_node])

    # if length of list is less than 1 (no siblings) then no children are present and return -1
    if has_child < 1:
        return -1

    while len(q) > 0:
        val = q.pop(0)
        starting_node = val

        # append children of parents to list to iterate through
        for x in range(len(ancestors)):
            if ancestors[x][1] == val:
                q.append(ancestors[x][0])

    # Find the parent of the last child returned to val to compare to other children and make sure lowest value child is returned
    parent = [ancestors[x][1] for x in range(len(ancestors)) if ancestors[x][0]==starting_node][0]

    # return the min value from the list of children that have the same parent
    return min([ancestors[x][0] for x in range(len(ancestors)) if ancestors[x][1] == parent])
