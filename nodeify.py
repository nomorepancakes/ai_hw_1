# nodeify.py
# AI HW 1: Cross the river without anyone being eaten.
# Tests OK on both python3.5 and python2.7
# Also you know you're doing it right when the documentation is longer than the code.

import random, sys
DEBUG = False


class State:
    """
        The heart, and the soul.

        They have children, they have parents,
        The numbers are real, boats are abstract.
        They are all fragile, like a glass,
        We welcome you, to the state class.

        (seriously fragile though if you change one character it breaks)

    """

    def __init__(self, left_cans=3, left_miss=3, boat_pos=True):
        """
            :params: Used to create children. When creating the parent node, default values are used.
        """
        self.no_of_cans = 3
        self.no_of_miss = 3
        self.left_cans = left_cans
        self.left_miss = left_miss
        self.moved_cans = 0
        self.moved_miss = 0
        self.illegal = False
        self.final_node = False
        self.parent = None
        self.children = []
        self.boat_position = boat_pos # True: Left

    def can_move_cans(self):
        """
            :return: Number of cannibals available.
                Context-Sensitive, automatically considers boat position.
        """
        return self.left_cans if self.boat_position else self.no_of_cans - self.left_cans

    def can_move_miss(self):
        """
            :return: Number of missionaries available.
        """
        return self.left_miss if self.boat_position else self.no_of_miss - self.left_miss

    def is_identical(self, input_node):
        """
            (A bit obvious, but for the sake of COMPLETE documentation...)
            Compares a node with itself.

            :input_node: Node to be compared with.
            :return: Are you me?
        """
        if input_node.left_cans == self.left_cans and \
                input_node.left_miss == self.left_miss and \
                input_node.boat_position == self.boat_position:
            return True
        else:
            return False

    def available_moves(self):
        """
            Exploration.

            :return: Array of tuple-d moves that could be performed to generate children.
                Directly returns the functions to be called.
        """
        all_moves = []
        if self.can_move_cans() > 0:
            all_moves.append((move_cans, None))
            if self.can_move_cans() > 1:
                all_moves.append((move_cans, move_cans))

            if self.can_move_miss() > 0:
                all_moves.append((move_miss, move_cans))

        if self.can_move_miss() > 0:
            all_moves.append((move_miss, None))
            if self.can_move_miss() > 1:
                all_moves.append((move_miss, move_miss))
        return all_moves

    def check_and_mark_illegal(self):
        """
            Node condition checking. Instead of returning values, sets the flags of itself.
            Also detects if the node is a goal or not.
        """
        if self.parent: # Check if we're at the root node. Parent is None if we are.
            if 0 < self.left_miss < self.left_cans:
                self.illegal = True
                if DEBUG:
                    print("ILLEGAL: Reason: Missionaries got bent. (len(miss) < len(cans))")
            if self.left_cans + self.left_miss == self.no_of_cans + self.no_of_miss:
                # This is actually being checked twice, one here and one with loop checking (this is the root node)
                # It's being kept for debugging.
                self.illegal = True
                if DEBUG:
                    print("ILLEGAL: Reason: Nothing is left on the right.")
            if 0 < self.no_of_miss - self.left_miss < self.no_of_cans - self.left_cans:
                if DEBUG:
                    print("ILLEGAL: Reason: Missionaries got bent on the right.")
                self.illegal = True
            if self.left_miss + self.left_cans == 0:
                self.final_node = True
                #print("This is a goal node.")

    def print_state_status(self):
        """
            Prints the current status of the state.
            Only used with DEBUG=True.
        """
        illegal_children_count = 0
        legal_children_count = 0
        for child in self.children:
            if child.illegal:
                #print("Call da police!")
                illegal_children_count += 1
            else:
                legal_children_count += 1
        pstr = "Cannibals on left: %s, \nMissionaries on left: %d, \nBoat: %s, \nIllegal: %s, \n" \
               "Children: %d legal, %d illegal" %\
               (self.left_cans, self.left_miss, "Left" if self.boat_position else "Right",
                self.illegal, legal_children_count, illegal_children_count)
        if DEBUG:
            print(pstr)


def move_miss(state):
    """
        Move exactly one missionary left or right.
    """
    state.left_miss += -1 if state.boat_position else 1
    state.moved_miss += 1
    #print("Miss moved.")


def move_cans(state):
    """
        Move exactly one cannibal left or right.
    """
    state.left_cans += -1 if state.boat_position else 1
    state.moved_cans += 1
    #print("Cans moved.")


def move_boat(state):
    """
        I gotta move the boat the otherside...
        Move the boat the otherside...
        Move the booaat...
        Move the booaat...
        How loong how loooong will I sli- (enough)
    """
    state.boat_position = not state.boat_position


def how_did_i_get_here(state, entry=True):
    """
        Beautify the way of getting to the result using recursion/back-traversing.
        :param state: (Hopefully) A goal node.
        :param entry: Used internally to see if this is the first node.
        :return: A beautiful string.
    """
    parent = state.parent
    template = "%s, \n\t%d m's and %d c's moved %s"
    if parent is not None:
        parents_explanation = how_did_i_get_here(parent, False)
        return template % (parents_explanation, state.moved_miss, state.moved_cans, "left" if state.boat_position else "right")
    else:
        return "Root node"

def compare_with_parents(starting_node, parent_node=None):
    """
        Loop detection.
        Back-traverses the tree and compares the starting node with each parent, until:
            -An identical node has been found
            -A node with a parent None was reached (root node)

        If the node is identical with any of its parents, it will be marked illegal.
        :param starting_node: Node to compare with its own parents.
        :param parent_node: Only used in recursion, pass the node to be compared manually.
            
        :return: (bool, State) True: Unique, None; False: Identical, State (identical node).
    """
    parent = starting_node.parent if parent_node is None else parent_node.parent
    resultset = True
    if parent is not None:
        is_the_same = starting_node.is_identical(parent)
        if not is_the_same:
            resultset = compare_with_parents(starting_node, parent)
        else:
            return False
    else:
        return True
    if not resultset:
        if DEBUG:
            print("ILLEGAL: Reason: Identical to a parent.")
        starting_node.illegal = True
    return resultset


def main_func(parent_node):
    """
        Exploration function.
        First, check if the node that is being expanded is allowable.
        Then,  detect loops.
        Later, use available moves to create child states.

        :param parent_node: The node to expand.
        :return: A tuple (bool, State). False, None if the node is not allowable; True, None if just allowable; True, State if goal.
    """
    parent_node.check_and_mark_illegal()
    is_unique = compare_with_parents(parent_node)

    if not parent_node.illegal:
        if not parent_node.final_node:
            if len(parent_node.children) == 0:
                for move_funcs in parent_node.available_moves():
                    new_child_state = State(parent_node.left_cans, parent_node.left_miss, parent_node.boat_position)
                    move_funcs[0](new_child_state)
                    if move_funcs[1]:
                        move_funcs[1](new_child_state)
                    #else:
                        #print("None moved.")
                    move_boat(new_child_state)
                    new_child_state.parent = parent_node
                    parent_node.children.append(new_child_state)
            if DEBUG:
                print("Parent node:")
                parent_node.print_state_status() 
            return True, None
            
        else:
            if DEBUG:
                print("\n\nGoal node:")
                parent_node.print_state_status()
            return True, parent_node
    else:
        if DEBUG:
            print("Dead end.")
        return False, None


def find_a_solution(entry_node, tabs=""):
    """
        First, expand the entry node.
        Then...
            -Pick a random child.
            -Iterate over the child.
            If, down the line, any child fails, try another child if possible.
            If not, announce failure to the caller so it can move on.
            On the goal node, announce success so all callers can terminate peacefully.
    """
    solution_result = (False, None)
    expansion_status = main_func(entry_node) # Expansion
    if expansion_status[0]:
        entries_children = [child for child in entry_node.children] # Copy

        while len(entries_children) > 0 and not solution_result[0]:
            random_child = random.choice(entries_children)
            solution_result = find_a_solution(random_child)
            entries_children.remove(random_child)
    else:
        if DEBUG:
            print("Welp.")
        return False, None

    if expansion_status[1]:
        if DEBUG:
            print("Is that a goal?!")
        return True, entry_node    

    return solution_result   


def mainish():
    """
        Main loop of the program.
        Run for <MAX_ITERATIONS>, then print the findings.
    """
    iterations = 0
    all_found_results = {}
    MAX_ITERATIONS = 1000
    while iterations < MAX_ITERATIONS:
        root_node_state = State()
        resultset = find_a_solution(root_node_state)
        ways_of_life = how_did_i_get_here(resultset[1])
        if DEBUG:
            print(ways_of_life)

        if ways_of_life in all_found_results.keys():
            all_found_results[ways_of_life] += 1
        else:
            all_found_results[ways_of_life] = 1
        iterations += 1
    for major_key in all_found_results.keys():
        print("\n\n%d times, \n\t%s \nwas the way." % (all_found_results[major_key], major_key))


def main_tests():
    """
        Disregard, only a test function.
        Manually reaches a goal to test that everything until the main loop performs OK.
    """
    root_node = State()
    main_func(root_node)
    main_func(root_node.children[1])
    main_func(root_node.children[1].children[0])
    main_func(root_node.children[1].children[0].children[1])
    main_func(root_node.children[1].children[0].children[1].children[0])
    main_func(root_node.children[1].children[0].children[1].children[0].children[3])
    main_func(root_node.children[1].children[0].children[1].children[0].children[3].children[2])
    main_func(root_node.children[1].children[0].children[1].children[0].children[3].children[2].children[4])
    main_func(root_node.children[1].children[0].children[1].children[0].children[3].children[2].children[4].children[0])
    main_func(root_node.children[1].children[0].children[1].children[0].children[3].children[2].children[4].children[0].children[1])
    main_func(root_node.children[1].children[0].children[1].children[0].children[3].children[2].children[4].children[0].children[1].children[0])
    main_func(root_node.children[1].children[0].children[1].children[0].children[3].children[2].children[4].children[0].children[1].children[0].children[1])
    how_did_i_get_here(root_node.children[1].children[0].children[1].children[0].children[3].children[2].children[4].children[0].children[1].children[0].children[1])

    
if __name__ == "__main__":
    print("Run with -d to see individual steps.")
    print("Calculating...")
    DEBUG = True if "-d" in sys.argv else False
    mainish()
