class Node:
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

class ShoppingList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while True:
            if cur.nextNode is None:
                cur.nextNode = new_node
                break
            cur = cur.nextNode

    def printshoppinglist(self):
        if self.head is None:
            print("The Shopping List is empty")
            return

        cur = self.head
        print("The Shopping List")
        counter = 1
        ittr = ''
        while cur:
            ittr += (f"{counter}. {cur.data}\n")
            cur = cur.nextNode
            counter += 1
        print(ittr)

    def lengthoflist(self):
        if self.head is None:
            print("The Shopping List is empty")
        cur = self.head
        count = 0
        while cur:
            cur = cur.nextNode
            count += 1
        return count

    def removefromlist(self, index):
        if index < 1 or index >= self.lengthoflist():
            print("Index given is out of range")

        if index == 1:
            self.head = self.head.nextNode
            return

        count = 1
        cur = self.head
        while cur:
            if count == index:
                cur.nextNode = cur.nextNode.nextNode
                break
            count += 1
            cur = cur.nextNode

    def crossoutvalue(self, index):
        if index < 1 or index >= self.lengthoflist():
            print("Index given is out of range")

        count = 1
        cur = self.head
        while cur:
            if count == index:
                first_letter = cur.data[0]
                last_letter = cur.data[-1]
                string_replaced = cur.data.replace(cur.data, '-' * (len(cur.data)-2))
                replaced_word = first_letter + string_replaced + last_letter
                cur.data = replaced_word
                break
            count += 1
            cur = cur.nextNode
