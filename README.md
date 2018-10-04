# leaky_bucket
leaky_bucket thread safe implementation
The below is unit test dump executed in Python 2.7.5 environment

[igor@localhost Downloads]$ python -V
Python 2.7.5
[igor@localhost Downloads]$ python lb-threaded.py
Server is running
Client #0 is running
Client #1 is running
Client #2 is running
Client #3 is running
Client #4 is running

6 tokens requested, True request status, 14 tokens remaining
5 tokens requested, True request status, 9 tokens remaining
4 tokens requested, True request status, 5 tokens remaining
5 tokens requested, True request status, 0 tokens remaining
10 tokens requested, False request status, 0 tokens remaining
2 tokens requested, False request status, 0 tokens remaining
11 tokens requested, False request status, 0 tokens remaining
2 tokens requested, False request status, 0 tokens remaining
10 tokens requested, False request status, 0 tokens remaining
10 tokens requested, False request status, 0 tokens remaining
11 tokens requested, False request status, 0 tokens remaining
4 tokens requested, False request status, 0 tokens remaining
9 tokens requested, False request status, 0 tokens remaining
5 tokens requested, False request status, 0 tokens remaining
2 tokens requested, False request status, 0 tokens remaining
9 tokens requested, False request status, 0 tokens remaining
2 tokens requested, False request status, 0 tokens remaining
9 tokens requested, False request status, 0 tokens remaining
3 tokens requested, False request status, 0 tokens remaining
5 tokens requested, False request status, 0 tokens remaining
7 tokens requested, False request status, 0 tokens remaining
8 tokens requested, False request status, 0 tokens remaining
5 tokens requested, False request status, 0 tokens remaining
9 tokens requested, False request status, 0 tokens remaining
9 tokens requested, False request status, 0 tokens remaining
1 tokens requested, False request status, 0 tokens remaining
10 tokens requested, False request status, 0 tokens remaining
2 tokens requested, False request status, 0 tokens remaining
3 tokens requested, False request status, 0 tokens remaining
9 tokens requested, False request status, 0 tokens remaining
7 tokens requested, False request status, 0 tokens remaining
7 tokens requested, False request status, 0 tokens remaining
3 tokens requested, False request status, 0 tokens remaining
5 tokens requested, True request status, 15 tokens remaining
9 tokens requested, True request status, 6 tokens remaining
8 tokens requested, False request status, 6 tokens remaining
9 tokens requested, False request status, 6 tokens remaining
11 tokens requested, False request status, 6 tokens remaining
4 tokens requested, True request status, 2 tokens remaining
3 tokens requested, False request status, 2 tokens remaining
4 tokens requested, False request status, 2 tokens remaining
10 tokens requested, False request status, 2 tokens remaining
6 tokens requested, False request status, 2 tokens remaining
7 tokens requested, False request status, 2 tokens remaining
4 tokens requested, False request status, 2 tokens remaining
9 tokens requested, False request status, 2 tokens remaining
10 tokens requested, False request status, 2 tokens remaining
6 tokens requested, False request status, 2 tokens remaining
4 tokens requested, False request status, 2 tokens remaining
11 tokens requested, False request status, 2 tokens remaining
6 tokens requested, False request status, 2 tokens remaining
9 tokens requested, False request status, 2 tokens remaining
9 tokens requested, False request status, 2 tokens remaining
9 tokens requested, True request status, 11 tokens remaining
8 tokens requested, True request status, 3 tokens remaining
1 tokens requested, True request status, 2 tokens remaining
2 tokens requested, True request status, 0 tokens remaining
7 tokens requested, False request status, 0 tokens remaining
6 tokens requested, False request status, 0 tokens remaining
9 tokens requested, False request status, 0 tokens remaining
3 tokens requested, False request status, 0 tokens remaining
10 tokens requested, False request status, 0 tokens remaining
