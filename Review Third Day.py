#!/usr/bin/env python
# coding: utf-8

# # Python 으로 구현한 stack 과 queue
# 
# - Python 의 class 를 이용하여 stack 과 queue 구현  
# - Stack class 의 method 는 pop (꺼내기), push (추가), size (stack 의 길이) 세가지로 한다.  
# - Queue class 의 method 는 enqueue(queue 에 추가), dequeue (queue 에 꺼내기), size (queue 의 길이) 세가지로 한다.

# In[4]:


class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

# And a queue that only has enqueue and dequeue operations
class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue) 


# In[5]:


stack = Stack()
stack.push('a')
stack.push('b')
stack.push('c')
stack.pop()


# In[6]:


q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
q.dequeue()


# # Pet 공원
# 
# - 공원에서 놀고있는 강아지와 고양이들을 object 로 구현. 강아지와 고양이들은 이름과 나이 두개의 attribute 로 구성  
# 
# 
# - 고양이들의 행동 (behavior) 은 뛰기 (running), 둘러보기(watching), 기지개 켜기(stretching) 으로 구성된다.  
# 
# 
# - 강아지들의 행동 (behavior) 은 뛰기 (running), 둘러보기(watching), 짖기(barking) 으로 구성된다.
# 
# 
# - running method 의 출력 : "{} 이 뛰고 있다"  --> 부모 class 의 method
# 
# 
# - watching methd 의 출력 : "강아지가 두리번거리며 보고 있다", "고양이가 조용히 보고 있다" --> oarent class method override  
# 
# 
# - streching method 의 출력 : "고양이가 기지개 켜고 있다"  --> 고양이 class 의 method  
# 
# 
# - barking method 의 출력 : "강아지가 짖고 있다"  --> 강아지 class 의 method
# 

# In[7]:


class Pet:
        
    def __init__(self, name, age, kind):
        self.name = name
        self.age = age
        self.kind = kind
        
    def running(self):
        print("{}이 뛰고 있다".format(self.kind))
    
    def watching(self):
        pass
    
class Dog(Pet):
    def watching(self):
        print("강아지가 두리번거리며 보고있다".format(self.kind))
              
    def barking(self):
        print("강아지가 짖고 있다")
        
class Cat(Pet):
    def watching(self):
        print("고양이가 조용히 보고있다".format(self.kind))
        
    def stretching(self):
        print("고양이가 기지개 키고 있다")


# In[8]:


dog = Dog('Doggy', 5, 'dog')
dog.running()
dog.watching()
dog.barking()


# In[9]:


cat = Cat('Mio', 1, 'cat')
cat.running()
cat.watching()
cat.stretching()


# # 비밀번호 알아맞추기
# 
# - 비밀번호 입력 허용 횟수 (ex, 10 회) 초과하면 "비밀번호 입력횟수 초과 입니다" 메시지 출력하고 종료 
# 
# - while 문을 이용하여 사전에 정해 놓은 비밀번호와 입력 받은 비밀번호가 같은지 비교 

# In[13]:


GUESSES_ALLOWED = 3
PASSWORD = "caribou"

input_left = GUESSES_ALLOWED
input_password = None

while input_password != PASSWORD and input_left:
    input_password = input("Guess a word: ")

    if input_password == PASSWORD:
        print(input_password)
        print("축하합니다. 성공입니다.")
    else:
        print(input_password)
        input_left -= 1
        print("비밀번호 오류! {} 회 남았습니다.".format(input_left))


# # try / except 응용
# 
# - input 을 이용하여 숫자를 입력 받음
# 
# - 숫자가 입력되면 입력받은 숫자 출력
# 
# - 알파벳이 입력되면 error message 출력
# 
# - except ValueError 이용

# In[18]:


try:
    number = int(input("숫자를 입력하시오: "))
    print(number)
except ValueError:
    print("숫자가 아닙니다")


# # Singly Linked List
# 
# <img src="Linkedlist.png" width="600">
# 
# - next pointer 로만 node 간에 연결된 자료구조
# 
# - random access 는 안되고 순차적 검색만 가능  
# 
# - 두개의 class 로 구성 
# 
#     1) node class --> value, next_node 로 구성
#     
#     2) singlyLinkedList class : 전체 list 구조 관리 --> head, tail, length
#     
#         - head : linked list 의 시작 node  
#         - tail : linked list 의 마지막 node  
#         - length : linkded list 의 길이
# 
# - 다음의 method 들을 추가 
# 
#     1) append method - list 에 새로운 node 추가
#     
#         - value 를 input 으로 받아 new node 를 생성  
#         - head 가 null 이면 첫번째 node 이므로 head 와 tail 에 모두 new node 를 assign 한다.
#         - head 가 null 이 아니면 현재의 tail 다음 (self.tail.next_node) 에 new node 를 assign 하고 현재의 tail 을 new node 로 update 
# 
#     2) pop method - list 의 마지막에서 node 제거 
#         - last node 의 이전 node 가 last 로 바뀌어야 하므로 tail 을 발견할 때까지 linked list 를 loop through 한다.
#         - tail 에 도달하면 tail node 의 이전 node 의 next_node 를 null 로 바꾸고 tail 을 새로운 tail node 로 update 
#         - length = length - 1
#         - remove 된 node 의 value 를 return 한다
#     

# In[77]:


class Node:

    def __init__(self, value):
        self.value = value
        self.next_node = None

    def get_data(self):
        return self.value

    def get_next(self):
        return self.next_node


# In[92]:


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        newNode = Node(value)
        
        if self.head:
            self.tail.next_node = newNode
            self.tail = newNode
        else:
            self.head = self.tail = newNode
            
        self.length += 1
        
    def pop(self):
        if not self.length:
            return
        current_node = self.head
        new_tail = current_node
        while (current_node.next_node):
            new_tail = current_node
            current_node = current_node.next_node
        new_tail.next_node = None
        self.tail = new_tail
        if self.length == 0:
            self.head = None
            self.tail = None
        return current_node.value
    
    def get_list(self):
        return print("head node = {}, tail node= {}, length = {} "
                     .format(self.head.get_data(), self.tail.get_data(), self.length))


# In[93]:


lnk = LinkedList()
lnk.append(7)
lnk.get_list()


# In[94]:


lnk.append(9)


# In[95]:


lnk.tail.get_data()


# In[96]:


lnk.get_list()


# In[97]:


lnk.pop()


# In[98]:


lnk.get_list()


# In[ ]:




