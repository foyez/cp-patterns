class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LLCurd:
    def __init__(self):
        # head: 1 -> 2
        self.head = Node(1)
        self.head.next = Node(2)

    def deleteNode(self, index):
        dummy = Node(next=self.head)
        prev, cur = dummy, self.head
        count = -1

        while cur and cur.next and count != index - 1:
            prev = cur
            cur = cur.next
            count += 1

        if count + 1 != index:
            print("Index {} doesn't exists.".format(index))
            return

        prev.next = cur.next
        self.head = dummy.next

    def deleteEndNode(self):
        dummy = Node(next=self.head)
        prev, cur = dummy, self.head

        while cur and cur.next:
            prev = cur
            cur = cur.next
        prev.next = None
        self.head = dummy.next

    def deleteFirstNode(self):
        self.head = self.head.next

    def insertAt(self, index, val):
        dummy = Node(next=self.head)
        prev, cur = dummy, self.head
        count = -1

        while cur and count != index - 1:
            prev = cur
            cur = cur.next
            count += 1

        if count + 1 != index:
            print("Index {} doesn't exists.".format(index))
            return

        newNode = Node(val=val)
        newNode.next = cur
        prev.next = newNode
        self.head = dummy.next

    def insertAtEnd(self, val):
        cur = self.head

        while cur and cur.next:
            cur = cur.next

        cur.next = Node(val)

    def insertAtBeginning(self, val):
        dummy = Node(val)
        dummy.next = self.head
        self.head = dummy

    def reverseLL(self):
        prev = None
        cur = self.head

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        self.head = prev

    def getLastNode(self):
        cur = self.head

        while cur and cur.next:
            cur = cur.next

        return cur

    def findMiddle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def initiateLoop(self):
        lastNode = self.getLastNode()
        middleNode = self.findMiddle()

        lastNode.next = middleNode

    def detectLoop(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if slow and slow == fast:
            print("Loop detected.")
            print(slow.val)
            print(fast.val)
        else:
            print("Loop doesn't exists")

    def printLL(self, node = None):
        if not self.head:
            print("Linked List is empty")

        cur = node if node else self.head

        while cur:
            print(cur.val, end=" ")
            cur = cur.next
        print()

ll = LLCurd()

ll.printLL()
ll.insertAt(1, 10)
ll.insertAtEnd(20)
ll.insertAtBeginning(-10)
ll.printLL()

# ll.deleteNode(0)
# ll.deleteEndNode()
# ll.deleteFirstNode()
# ll.printLL()

ll.reverseLL()
ll.printLL()

ll.initiateLoop()
ll.detectLoop()