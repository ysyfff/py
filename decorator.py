# def increase(f):
#     def pack_f(a, b):
#         return int(f(a, b))+2
#     return pack_f
    

# @increase
# def plus(a, b):
#     return a+b

# print plus(1, 2)

def increase(tpl=None, auth=False):
    def func(f):
        def pack_f(a, b):
            return int(f(a, b))+2
        return pack_f

    if callable(tpl):
        return func(tpl)
    else:
        return func
    

@increase(auth=True)
def plus(a, b):
    return a+b

print plus(1, 2)