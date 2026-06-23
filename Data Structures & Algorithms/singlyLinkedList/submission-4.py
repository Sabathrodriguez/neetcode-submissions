class LinkedList:
    class Node:
        def __init__(self, val=-1, next=None):
            self.val = val
            self.next = next
    
    def __init__(self):
        self.head = self.Node()        
        self.tail = self.head
    
    def get(self, index: int) -> int:
        current = self.head.next
        i = 0

        while current:
            if i == index:
                # print("get:", current.val)
                return current.val
            
            i += 1

            current = current.next
        
        return -1

    def insertTail(self, val: int) -> None:
        self.tail.next = self.Node(val)
        self.tail = self.tail.next
        
        # print("linked list vals after insert tail:", self.getValues())


    def insertHead(self, val: int) -> None:
        newNode = self.Node(val)

        newNode.next = self.head.next
        self.head.next = newNode
        
        if not newNode.next:
            self.tail = newNode

        # print("linked list vals after insert head:", self.getValues())

    def remove(self, index: int) -> bool:
        current = self.head
        i = 0

        # for i in range(self.length):
        while i < index and current:
            i += 1
            current = current.next
            
        if current and current.next:
            if current.next == self.tail:
                self.tail = current
        
            current.next = current.next.next
            return True
        
        return False

    def getValues(self) -> List[int]:
        cur = self.head.next
        res = []

        # for i in range(self.length):
        while cur:
            res.append(cur.val)

            cur = cur.next
        
        return res
        
