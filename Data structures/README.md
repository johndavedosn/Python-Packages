# DSA directory
This is for my implementation of certain data structures and algorithms.

# Basic_queue_ds.py

This is the basic implementation of a queue (FIFO) : 
- **class :** ``queue()``
- **methods :** ``queue.add()`` for adding an element to the queue, if the queue is at it's max capacity it will delete 
the first element of the queue **Example :** 
```py
q = queue(2).add(1).add(2).add(3)
```
Here the queue will delete the first number which is 1 in order to add the third one 3, so the list must be 
```py
[2, 3]
```
``queue.is_full()`` for checking if the queue is true, basically returns either True or False depending on if the queue's length is equal to the fixed length parameter.

``queue.get_list()`` to get the queue's values

# weirdest_algo.py

I know...I know, the algorithm may look weird or overly not optimized but it's a fresh idea that popped in my mind and I couldn't resist the urge to turn it to reality

**Note** : The algorithm might've been already made so take what I say with the giant grain of salt
(if it was already made than please open an issue)
