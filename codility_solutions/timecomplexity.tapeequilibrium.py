#!/usr/bin/env python
import random 
import pprint

numbers = 5 
list1 = []
dicta = {}
dictb = {}

for item in range(0,numbers):
   list1.append(random.randint(0, 100)+1)

pp = pprint.PrettyPrinter()
pp.pprint(list1)

for num in range(0,len(list1)):
    if(num < len(list1)):
       print("A ",list1[num])   
       for a_iter in range(0,num):
           if dicta.get(a_iter) is None:
              dicta[a_iter] = 0
           dicta[a_iter] = dicta[a_iter] + list1[num]       
    if(num > 0):
       print("B ",list1[num])
       for b_iter in range(num,len(list1)):
           if dictb.get(b_iter) is None:
              dictb[b_iter] = 0
           dictb[b_iter] = dictb[b_iter] + list1[num]

pp.pprint(dicta)
print("\n\n")
pp.pprint(dictb)