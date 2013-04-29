#! /usr/bin/env python
# -*-coding:utf-8-*-
class A:
    member = "this is a test."
    def __init__(self):
        pass
 
    @classmethod
    def Print1(cls):
        #杩欎釜鏄被鏂规硶
        print "print 1: ", cls.member
         
    def Print2(self):
        print "print 2: ", self.member
            
         
    @classmethod    
    def Print3(paraTest):
        print "print 3: ", paraTest.member
 
a = A()
A.Print1()   #相当于Print1(A)
a.Print2()   #相当于Print2(a)， 请注意@classmethod
A.Print3()   