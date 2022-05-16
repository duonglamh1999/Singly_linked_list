class Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next= next
class Linked_list:
    def __init__(self):
        self.head=None
    def insert_at_begining(self,data):
        self.head= Node(data, self.head)
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next=Node(data,None)
    def print(self):
        if self.head is None:
            print("LL is empty")
            return
        itr = self.head
        llstr=''
        while itr:
            llstr += str(itr.data)+'->'
            itr =itr.next
        print(llstr)
    def insert_list (self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count
    def remove_at (self,index):
        if index<0 or index >= self.get_length():
            raise Exception("Invalid Input")
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr = self.head
        while itr:

            if count == index-1:
                itr.next= itr.next.next
                break
            itr = itr.next
            count += 1
    def insert_at (self, index,data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid input")
        if index==0:
            self.insert_at_begining(data)
        count=0
        itr=self.head
        while itr:
            if count== index-1:
                itr.next=Node(data,itr.next)
                break
            itr = itr.next
            count += 1
    def remove_value(self,data):
        count=0
        itr=self.head
        while itr:
            if itr.next.data==data:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
        if count==self.get_length():
            raise Exception("Value does not exist")
    def insert_after_value(self,data_before,data_after):
        count = 0
        itr = self.head
        while itr:
            if itr.data == data_before:
                itr.next = Node(data_after,itr.next)
                break
            itr = itr.next
            count += 1
        if count == self.get_length():
            raise Exception(print("Value does not exist"))
link= Linked_list()
link.insert_list([1,2,4,4,6,7,8,9,0,10])
link.insert_at(8,20)
link.insert_at(8,22)
print(link.get_length())
link.insert_after_value(4,2)
link.remove_value(2)
link.print()