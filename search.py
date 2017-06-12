#!/usr/bin/env python
#coding=utf-8
#广度优先
from collections import deque

def person_is_seller(person):
    if "thom" in person:
        return True
    else:
        return False

def search(tup,id):
    search_queue = deque()
    search_queue += tup[id]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print person + " is a mango seller "
                return True
            else:
                search_queue += tup[person]
                searched.append(person)
    return False



if __name__ == '__main__':

    graph = {\
    'you':["alice", "bob", "claire"],\
    'bob':["anuj", "peggy"],\
    'alice':["peggy"],\
    'claire':["thom", "jonny"],\
    'anuj':[],'peggy':[],'thom':[],'jonny':[]
    }

    search(graph,'you')
