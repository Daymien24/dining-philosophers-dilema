# Dining Philosophers Problem
The problem was designed to illustrate the challenges of avoiding deadlock, a system state in which no progress is possible. To see that a proper solution to this problem is not obvious, consider a proposal in which each philosopher is instructed to behave as follows:

 - think until the left fork is available; when it is, pick it up;
 - think until the right fork is available; when it is, pick it up;
 - when both forks are held, eat for a fixed amount of time;
 - then, put the right fork down;
 - then, put the left fork down;
 - repeat from the beginning.

 The problem is solved using python's threads based on tutorial from geeksforgeeks.org.
