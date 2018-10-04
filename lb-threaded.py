# -*- coding: utf-8 -*-
import random
import time
import threading
from threading import Thread
from multiprocessing import Queue

# **************************************************************************
# Leacky Bucket class

class leakyBucket(object):
  """Canonical LB implementation with bound queue instance for multithread support, no blocking"""
  def __init__(self, max_amount, refill_time, refill_amount, q):
    self.max_amount = max_amount
    self.refill_time = refill_time
    self.refill_amount = refill_amount
    self.q = q
    self.reset()

  def _refill_count(self):
    return int(((time.time() - self.last_update) / self.refill_time))

  def reset(self):
    self.value = self.max_amount
    self.last_update = time.time()

  def get(self):
    return min(
      self.max_amount,
      self.value + self._refill_count() * self.refill_amount
    )

  def reduce(self, tokens):
    refill_count = self._refill_count()
    self.value += refill_count * self.refill_amount
    self.last_update += refill_count * self.refill_time

    if self.value >= self.max_amount:
      self.reset()
    if tokens > self.value:
      return False

# placeholder for an inbound interface, shared resource
    self.value -= tokens
    return True

# **************************************************************************
# Queue put interface for a client task
  def q_put_request(self, tokens):
    if self.q.full() == True:
      return 

    self.q.put(tokens, True)

# **************************************************************************
# Queue get interface for a server task
  def q_get_request(self):
    if self.q.empty() == True:
      return None

    return self.q.get(True)

# **************************************************************************
# Server
class leakyBucketServer(Thread):
    def __init__(self, name, lb):
        """Server task created with bound LB"""
        Thread.__init__(self)
        self.name = name
        self.lb = lb
    
    def run(self):
        print "%s is running" % self.name
        time.sleep(3)

        while True:
          tokens = self.lb.q_get_request()
 
          if tokens is None:
              continue

          lb_status = self.lb.reduce(tokens)
          print "%s tokens requested, %s request status, %s tokens remaining" % (tokens, lb_status, self.lb.get() )


# **************************************************************************
# Client

class leakyBucketClient(Thread):
    def __init__(self, name, lb):
        """Client task created with bound LB"""
        Thread.__init__(self)
        self.name = name
        self.lb = lb
    
    def run(self):
        print "%s is running" % self.name

        while True:
          time.sleep(random.randint(1, 2))

          tokens = random.randint(1, 11)
          self.lb.q_put_request(tokens)

    
if __name__ == "__main__":

# create LB instance, bind a queue
    lb = leakyBucket(20, 7, 20, Queue())

# create and start server task
    leakyBucketServer("Server", lb).start()

# create and start client tasks
    for i in range(5):
        leakyBucketClient("Client #%s" % (i), lb).start()




