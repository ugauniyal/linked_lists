class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_llist(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
            new_node.next = None

    def prepend(self, data):
        new_node = Node(data)
        temp = self.head
        self.head = new_node
        new_node.next = temp

    def list_length(self):
        curr = self.head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        return count

    def delete_node(self, key):

        curr = self.head
        if curr and curr.data == key:
            self.head = curr.next
            curr = None
            return

        prev = None
        
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if curr is None:
            return

        prev.next = curr.next
        curr = None

    def delete_node_at_pos(self, pos):
        if self.head == None:
            return

        curr = self.head
        count = 0

        if pos == 0:
            self.head = curr.next
            curr = None
            return

        while curr and count != pos:
            prev = curr
            curr = curr.next
            count += 1

        if curr is None:
            return

        prev.next = curr.next
        curr = None

    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return
        
        curr1 = self.head
        prev1 = None

        curr2 = self.head
        prev2 = None

        while curr1 and curr1.data != key_1:
            prev1 = curr1
            curr1 = curr1.next

        while curr2 and curr2.data != key_2:
            prev2 = curr2
            curr2 = curr2.next
        
        if not curr1 or not curr2:
            return
        
        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2

        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1
        
        curr1.next, curr2.next = curr2.next, curr1.next

        

    def is_palindrome(self):
        string = ""
        curr = self.head
        while curr:
            string += curr.data
            curr = curr.next
        return string == string[::-1]

    def count_occurences_iterative(self, data):
        curr = self.head
        count = 0
        while curr:
            if curr.data == data:
                count += 1
            curr = curr.next
        return count

    def remove_duplicates(self):
        curr = self.head
        prev = None
        duplicate = dict()
        
        while curr:
            if curr.data in duplicate:
                prev.next = curr.next
            else:
                prev = curr
                duplicate[curr.data] = 1
                
            curr = curr.next

    def reverse_list(self):
        prev = None 
        curr = self.head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def print_nth_from_last(self, n):
        total_len = self.list_length()
        curr = self.head

        while curr:
            if total_len == n:
                print(curr.data)
                return curr.data
            total_len -= 1 
            curr = curr.next
            if curr is None:
                return

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        if not p:
            return q
        if not q:
            return p

        merged_list = LinkedList()
        
        while p and q:
            if p.data <= q.data:
                merged_list.append(p.data)
                p = p.next
            else:
                merged_list.append(q.data)
                q = q.next

        if not p:
            while q:
                merged_list.append(q.data)
                q = q.next

        if not q:
            while p:
                merged_list.append(p.data)
                p = p.next

        merged_list.print_llist()

    def rotate(self, k):
        if not self.head and not self.head.next:
            return
        p = self.head
        q = self.head
        prev = None
        count = 0

        while p.next != None and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1
        
        p = prev

        while q.next != None:
            q = q.next

        q.next = self.head
        self.head = p.next
        p.next = None



llist = LinkedList()

llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend("A")
llist.delete_node("D")
llist.delete_node_at_pos(0)
llist.delete_node_at_pos(1)

llist.print_llist()
print(llist.list_length())


llist_2 = LinkedList()
llist_2.append("A")
llist_2.append("B")
llist_2.append("B")
llist_2.append("A")

print(llist_2.is_palindrome())
print(llist_2.count_occurences_iterative('A'))

llist_3 = LinkedList()
llist_3.append(1)
llist_3.append(6)
llist_3.append(1)
llist_3.append(4)
llist_3.append(2)
llist_3.append(2)
llist_3.append(4)

print("Original Linked List")
llist_3.print_llist()
print("Linked List After Removing Duplicates")
llist_3.remove_duplicates()
llist_3.print_llist()

llist_4 = LinkedList()
llist_4.append("A")
llist_4.append("B")
llist_4.append("C")
llist_4.append("D")
print("Original Linked List")
llist_4.print_llist()
print("Nth to last element")
llist_4.print_nth_from_last(3)
print("Reversed Linked List")
llist_4.reverse_list()
llist_4.print_llist()


llist_5 = LinkedList()
llist_5.append("A")
llist_5.append("B")
llist_5.append("C")
llist_5.append("D")
print("Original Linked List")
llist_5.print_llist()
print("After Swap node")
llist_5.swap_nodes("B", "C")
llist_5.print_llist()

llist_6 = LinkedList()
llist_6.append(1)
llist_6.append(2)
llist_6.append(3)
llist_6.append(4)
llist_6.append(8)
llist_6.append(9)
llist_6.append(10)

llist_7 = LinkedList()
llist_7.append(2)
llist_7.append(3)
llist_7.append(4)
llist_7.append(6)
llist_7.append(8)

print("Sorted List")
llist_6.merge_sorted(llist_7)


llist_8 = LinkedList()
llist_8.append(1)
llist_8.append(2)
llist_8.append(3)
llist_8.append(4)
llist_8.append(5)

llist_8.rotate(2)
llist_8.print_llist()