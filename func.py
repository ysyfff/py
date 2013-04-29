#!usr/bin/evn python
#coding:utf8
# #1
# def f1():
#     def f2():
#         def f3():
#             print "33"
#         return f3()
#         print "22"
#     return f2()
#     print "11"

# f=f1()
# print f

# #2
# def f1():
#     def f2():
#         def f3():
#             print "33"
#         #return f3()
#         print "22"
#     return f2()
#     print "11"


# print f1()

# #3
# def f1():
#     def f2():
#         def f3():
#             print "33"
#         #return f3()
#         print "22"
#     #return f2()
#     print "11"


# print f1()
def max(a, b):
    if a>b:
        return a
    else:
        return b

def lrender(tpl=None, auth=False, staff=False):
    print "1------> ",tpl, auth, staff

    def func(f):
        print "2------> ", tpl, auth, staff, f

        def infunc(req, *args, **kwargs):
            print "3------> ", tpl, auth, staff, f
            print req, args, kwargs, func

            if auth:
                print 'You are a man'
            r = f(req, *args, **kwargs) #这里他就会去执行被装饰的函数,
                                        #执行的结果是被修饰的函数的return函数的返回值
            print "r = ",r
        return infunc
    return func

@lrender("index.html",auth=True)
def test(request):
    print "I am the decoratored function!"
    return max(1,2)

request="'I am test'"
test(request)
# def public(arg):
#     print "hello"
#     print arg#由此可以看到arg是一个函数啊，也就是修饰符下面的那个函数传递到这里来了
#     return arg()

# @public
# def test1():
#     print "test1"

# @public
# def test2():
#     print "test2"