import time
import threading
 
class Philosopher(threading.Thread):
    def __init__(self, id, forks, ilosc_posilkow):
        threading.Thread.__init__(self)
        self.id = id
        self.forks = forks
        self.dishes = 0
        self.ilosc_posilkow = ilosc_posilkow
     
    def run(self):
        if self.id%2 == 0:
            self.run_even()
        else:
            self.run_odd()
         
        if self.dishes < self.ilosc_posilkow:
            time.sleep(0.1)
            self.run()
     
    def run_even(self):
        """
        Even numbered Philozophers are very greedy and a holding the left 
        until they pick up the right fork.
        """
        
        left_fork = id
        right_fork = (id + 1)%len(self.forks)
        print ("Philosopher " + str(self.id) + " waits for the left fork")
        self.forks[left_fork].acquire()
        print ("Philosopher " + str(self.id) + " takes left fork")
        print ("Philosopher " + str(self.id) + " waits for the right fork")
        self.forks[right_fork].acquire()
        print ("Philosopher " + str(self.id) + " takes right fork")        
        print ("Philosopher " + str(self.id) + " is eating")
        self.dishes += 1
        time.sleep(1)
        self.forks[right_fork].release()
        print ("Philosopher " + str(self.id) + " lays down the right fork")
        self.forks[left_fork].release()
        print ("Philosopher " + str(self.id) + " lays down the left fork")
     
    def run_odd(self):
        """
        Odd Philofophers are very generous, if the cant pick up the right fork, 
        then they will lay down the left fork and then try again. 
        """
        
        left_fork = self.id
        right_fork = (self.id + 1)%len(self.forks)        
        print ("Philosopher " + str(self.id) + " tries to pick up the left fork")
        
        if self.forks[left_fork].acquire(False): # true if the left fork is free (if the thread is free) 
            print ("Philosopher " + str(self.id) + " picks up the left fork.")
            print ("Philosopher " + str(self.id) + " tries to pick up the right fork")
            if self.forks[right_fork].acquire(False):
                print ("Philosopher " + str(self.id) + " picks up the right fork")                
                print ("Philosopher " + str(self.id) + " is eating")
                self.dishes += 1
                time.sleep(1)
                self.forks[right_fork].release()
                print ("Philosopher " + str(self.id) + " puts down the right fork")
                self.forks[left_fork].release()
                print ("Philosopher " + str(self.id) + " puts down the left fork")
            else:
                print ("Philosopher " + str(self.id) + "couldnt pick up the right fork ")
                self.forks[left_fork].release()
                time.sleep(0.1)
                self.run()
        else:
            print ("Philosopher " + str(self.id) + " couldnt pick up the left fork")
            time.sleep(0.1)
            self.run()
 
numPhilosophers = 5
forks = []
Philosophers = []
dishes = []
for i in range(numPhilosophers):
    forks.append(threading.Lock())
    dishes.append(0)
 
for id in range(numPhilosophers):
    Philosophers.append(Philosopher(id, forks, 2))
 
for Philosopher in Philosophers:
    Philosopher.start()
 
for Philosopher in Philosophers:
    Philosopher.join()
 
print(f"Everyone ate: {Philosopher.dishes} times. ")
 
print ("Finished!")