class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.size = 0 # Keep track of size of list
        # Keep reference so we dont have to iterate over again
        self.head = ListNode(0)
        self.tail = ListNode(0)

        # Connect the two
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1 
        # Create current to find indexth node
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val
                                   
    def addAtHead(self, val: int) -> None:
        new_head_node = ListNode(val)
        old_first = self.head.next # Old first head

        new_head_node.next = old_first
        new_head_node.prev = self.head
        old_first.prev = new_head_node
        self.head.next = new_head_node

        self.size += 1 
        
    def addAtTail(self, val: int) -> None:
        new_tail_node = ListNode(val)
        old_last = self.tail.prev

        new_tail_node.next = self.tail
        new_tail_node.prev = old_last
        old_last.next = new_tail_node
        self.tail.prev = new_tail_node

        self.size += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return
        elif index == self.size:
            self.addAtTail(val)
        else:
            new_node = ListNode(val) # create node
            curr = self.head.next
            for _ in range(index):
                curr = curr.next 
            
            # Put our node one before our current
            prior_node = curr.prev

            new_node.next = curr
            new_node.prev = curr.prev
            prior_node.next = new_node
            curr.prev = new_node

            self.size += 1      

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0: 
            return
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        
        node_before = curr.prev
        node_after = curr.next
        
        node_before.next = node_after
        node_after.prev = node_before

        self.size -= 1 
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)