class DLLNode(object):

    def __init__(self, value, nxt, prev):
        # Value is another way to refer to the name or label of the node.
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"V: [{self.value}], N: [{repr(nval)}], P: [{repr(pval)}]"

class DoubleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""
        if self.begin == None and self.end == None:
            print("Pushing node onto empty list...")

            push_node = DLLNode(obj, self.end, None)
            self.begin = push_node
            self.end = push_node

            print("There's nothing in the list, but now there is:")
            print("First node:", self.begin)
            print("Second node:", self.begin.next)
            print("Last node:", self.end)

        elif self.begin != None and self.begin == self.end:
            print("One node exists:",  self.begin, " pushing node to final position...")

            push_node = DLLNode(obj, self.end, None)
            self.end = push_node
            self.begin.next = push_node
            push_node.prev = self.begin
            self.end.next = None

            print("Theres one item in the list, now there's two:")
            print("First node:", self.begin)
            print("Second node:", self.begin.next)
            print("Last node:", self.end)

        elif self.begin != None and self.begin != self.end:
            print("There are 1> nodes, start and end:", self.begin, self.end,
                  " pushing node to end...")

            push_node = DLLNode(obj, None, self.end)
            self.end.next = push_node
            push_node.prev = self.end
            self.end = push_node

            print("There's a few items in the list, now there's more:")
            print("First node:", self.begin)
            print("Second node:", self.begin.next)
            print("Last node:", self.end)


    def pop(self):
        """Removes the last item and returns it."""

        if self.end == None and self.begin == None:
            print("There's nothing to pop.")


        elif self.begin != None and self.end == None:
            print("There is only one node:", self.begin, " attempting pop it...")

            pop_node = self.begin
            self.begin = None

            print("There was one item, now there's nothing.")
            print(self.begin)
            print(self.end)

            return pop_node.value
            self.end = None


        elif self.begin != None and self.end != None:
            print("There are nodes at both start and end:", self.begin, self.end, " attempting pop...")

            if self.begin != self.end.prev:
                # Checks if the first node is not the same as the second last node.
                # i.e. there are >2 nodes.
                print("There should be more than 2 nodes...")
                print("Attempting to pop:", self.end.value ,"...")

                pop_node = self.end

                self.end.prev.next = None
                self.end = self.end.prev

                print("There was some items, and you popped off one.")
                print("First node:", self.begin)
                print("Second node:", self.begin.next)
                print("Last node:", self.end)

                return pop_node.value


            else:
                # If the first node is the second last node, then there are 2 nodes

                print("The first node is the second last node; there should only be 2 nodes...")
                print("Attempting to pop:", self.end.value ,"...")

                pop_node = self.end
                self.end.prev.next = None
                self.end = None

                print("There was some items, and you popped off the last one.")
                print("First node:", self.begin)
                print("Second node:", self.begin.next)
                print("Last node:", self.end)

                return pop_node.value


    def shift(self, obj):
        """Same operation as push except it adds to the beginning of the list."""
        if self.begin == None and self.end == None:
            # This is the same operation as push as the list is empty.
            print("Shifting node onto empty list...")

            shift_node = DLLNode(obj, self.end, None)
            self.begin = shift_node
            self.end = shift_node

            print("There's nothing in the list, but now there is:")
            print("First node:", self.begin)
            print("First node:", self.begin.next)
            print("Last node:", self.end)

        elif self.begin != None and self.begin == self.end:
            print("One node exists:",  self.begin, " shifting node to first position...")

            shift_node = DLLNode(obj, self.begin, None)
            self.begin = shift_node
            self.end.prev = shift_node

            print("Theres one item in the list, now there's two:")
            print("First node:", self.begin)
            print("Second node:", self.begin.next)
            print("Last node:", self.end)

        elif self.begin != None and self.begin != self.end:
            print("There are 1> nodes - start and end:", self.begin, self.end,
                  " shifting node to first position...")

            shift_node = DLLNode(obj, self.begin, None)
            self.begin.prev = shift_node
            self.begin = shift_node

            print("There's a few items in the list, now there's more:")
            print("First node:", self.begin)
            print("Second node:", self.begin.next)
            print("Last node:", self.end)


    def unshift(self):
        """Removes the first item and returns it."""
        # This is essentially the same as pop, but with the first node.

        if self.end == None and self.begin == None:
            print("There's nothing to unshift.")


        elif self.begin != None and self.end == None:
            print("There is only one node:", self.begin, " attempting unshift it...")

            unshift_node = self.begin
            self.begin = None

            print("There was one item, now there's nothing.")
            print(self.begin)
            print(self.end)

            return unshift_node.value
            self.end = None


        elif self.begin != None and self.end != None:
            print("There are nodes at both start and end:", self.begin, self.end,
                  " attempting unshift...")

            if self.begin != self.end.prev:
                # Checks if the first node is not the same as the second last node.
                # i.e. there are >2 nodes.
                print("There should be more than 2 nodes...")
                print("Attempting to unshift:", self.begin.value ,"...")

                second_node = self.begin.next
                self.begin = second_node

                print("There was some items, and you unshifted the first.")
                print("First node:", self.begin)
                print("Second node:", self.begin.next)
                print("Last node:", self.end)

                return self.begin.prev.value
                second_node.prev = None


            else:
                # If the first node is the second last node, then there are 2 nodes

                print("The first node is the second last node; there should only be 2 nodes...")
                print("Attempting to unshift:", self.begin.value ,"...")

                unshift_node = self.begin
                self.begin.next.prev = None
                self.begin = self.end
                self.end = None

                print("There was some items, and you unshifted the last one.")
                print("First node:", self.begin)
                print("Second node:", self.begin.next)
                print("Last node:", self.end)

                return unshift_node.value



    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        # The SLL is not constructed with an index, so we need to give it one.
        # This loops through the nodes, starting at the beginning, with each
        # node increasing the index by one, then stopping once it gets to the
        # search term object. Not the most efficient algorithm, but it works.

        # THe index only created per instance of this operation. This saves time
        # having to reconstruct the index whenever any other operation happens.
        # A better way to do this might be to have an automatically updating index
        # that refreshes everytime an operation happens.
        index = -1
        node = self.begin
        while node:
            index += 1
            print("Currently at index:", index, " ...")

            if node.value == obj:
                break

            node = node.next

        if node == None:
            print("Node \"", obj, "\" not found.")
            return None

        print("Identified node:", node.value, ", equal to search node:", obj)
        print("The index of the identified node is:", index)

        # when it removes, it pushes the whole stack down, so node n becomes
        # node n-1
        print("Now removing: ", node.value)

        if node == self.begin and node != self.end:
            nextnode = node.next
            self.begin = nextnode
            node.next = None

            print("--- RESULT ---")
            print("First node:", self.begin)
            try:
                print("Second node:", self.begin.next)
            except AttributeError:
                print("Second node:", None)
            print("Last node:", self.end)

        elif node == self.begin and node == self.end:
            nextnode = node.next
            self.begin = nextnode
            node.next = None
            self.end = None

            print("--- RESULT ---")
            print("First node:", self.begin)
            try:
                print("Second node:", self.begin.next)
            except AttributeError:
                print("Second node:", None)
            print("Last node:", self.end)

        elif node != self.begin and node == self.end:
            prevnode = node.prev
            self.end = prevnode
            self.end.next = None
            node.prev = None

            print("--- RESULT ---")
            print("First node:", self.begin)
            try:
                print("Second node:", self.begin.next)
            except AttributeError:
                print("Second node:", None)
            print("Last node:", self.end)

        # if the input node is not the first node,
        # set node - 1 next as node + 1
        # set input node next and prev as none
        else:
            node.prev.next = node.next
            node.next = None
            node.prev = None

            print("--- RESULT ---")
            print("First node:", self.begin)
            try:
                print("Second node:", self.begin.next)
            except AttributeError:
                print("Second node:", None)
            print("Last node:", self.end)
        return index

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        # Reference is returning the value.
        print("The first node is: ", self.begin.value)
        return self.begin.value

    def last(self):
        """Returns a *reference* to the last item, does not remove."""
        # Reference is returning the value.
        print("The last node is: ", self.end.value)
        return self.end.value

    def count(self):
        """Counts the number of elements in the list."""
        #NOTE: This is copied from Zed's code. It could be less naive and not
        # iterate through the full list.Could make this an automatic function
        # that executes whenever a new node is added, to update the index.

        node = self.begin
        count = 0
        while node:
            count += 1
            print("Counting... N =", count)
            if node.next != node:
                node = node.next
            else:
                break
        print("Count complete.")
        return count


    def get(self, index):
        """Get the value at the index."""
        # The SLL is not constructed with an index, so we need to give it one.
        # This loops through the nodes, starting at the beginning, with each
        # node increasing the index by one, then stopping once it gets to the
        # search term object. Not the most efficient algorithm, but it works.

        # THe index only created per instance of this operation. This saves time
        # having to reconstruct the index whenever any other operation happens.
        index_count = -1
        node = self.begin
        print("Initiating get operation for node at index: ", index)
        while node:
            index_count += 1
            print("Currently at index:", index_count, " ...")

            if index_count == index:
                break

            node = node.next

        if node == None:
            print("Index \"", index, "\" not found.")
            return None

        print("Identified node:", node.value, ", at index:", index_count)
        return node.value


    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        # Dump refers to printing the list.

        position,target_node = mark.split()

        # TODO: Case insensitive match using regex
        #iterate through the list and find the target node.
        node = self.begin
        print("Finding target node for dump operation: ", target_node)
        while node:
            if target_node.casefold() == node.value.casefold():
                print("Target node identified.")
                break

            node = node.next

        if node == None:
            print("Target node \"", target_node, "\" not found.")
            return None

        # TODO: Case insensitive match using regex
        if position == 'before':
            print("Proceeding to dump all nodes previous to: ", target_node)
            dump_node = node.prev
            while dump_node:
                print(dump_node)
                try:
                    dump_node = dump_node.prev

                except AttributeError:
                    break

            print("--- END OF LIST ---")

        elif position == 'after':
            print("Proceeding to dump all nodes after: ", target_node)
            dump_node = node.next
            while dump_node:
                print(dump_node)
                try:
                    dump_node = dump_node.next

                except AttributeError:
                    break

            print("--- END OF LIST ---")

        else:
            print("invalid position")
