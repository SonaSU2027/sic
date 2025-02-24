import sys
class Queue:
    def __init__(self):
        self.queue=[]
        print('enter 1.enque 2. dequeue 3. display 4.exit')
        
    def enque(self,data):
        self.queue.append(data)
    def dequeue(self):
        if len(self.queue)!= 0:
            dequeued = self.queue.pop(0)
            return dequeued
    def display(self):
        for i in range(len(self.queue)):
            print(self.queue[i])
    def match_user_choice(self, choice):
        match choice:
            case 1 :
                data = int(input('Enter the elem to be inserted:'))
                self.enque(data)
            case 2:
                print('the dequeued elem is:',self.dequeue())
            case 3:
                self.display()
            case 4:
                sys.exit()
            case _:
                print('invalid choice')
                
    
q = Queue()
while True:
    choice=int(input('enter the choice'))
    q.match_user_choice(choice)