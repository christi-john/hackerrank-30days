# https://www.hackerrank.com/challenges/30-linked-list/problem

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        nodenew=Node(data)    #creating a new node object
        if head==None:
            return nodenew
        else:
            pointer=head
            while(pointer.next!=None):
                pointer=pointer.next
            pointer.next=nodenew  #creating pointer (link b/w nodes)
            return head
                
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  