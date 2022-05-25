

# class vik:


#     def __init__(self,timespent):
#         self.timespent=timespent
    
#     def manu(self):
#         print('somtin')
#         return self.get_time()*100
    

#     @property
#     def timespent(self):
#         print('getting values----')
#         return self._timespent



#     @timespent.setter
#     def timespent(self,x):
#         print('setting values--------')
#         if x>5:
#             x=10

        
#         self._timespent=x

#     @timespent.deleter
#     def timespent(self):
#         print('inside delete fun')
#         return None
    
# obj=vik(45)


# print(obj.timespent)

# del obj.timespent
# print(obj.timespent)


class A(object):
    print('A')
    pass
class B(A):
    print('B')
    pass
class C(A):
    print('C')
    pass
class D_0(B, C):
    print('D_0')

    pass
class D_1(B, C):
    print('D_1')

    pass
class E_0(D_0,D_1):
    print('E_0')

    pass
class E_1(D_1):
    print('E_1')

    pass
class F(E_0, E_1):
    print('F')

    pass
f = F()
print(F.mro())

# [<class '__main__.F'>, 

# <class '__main__.E_0'>,
# 
#  <class '__main__.D_0'>,
# 
#  <class '__main__.E_1'>, 
# 
# <class '__main__.D_1'>,
# 
#  <class '__main__.B'>,
# 
#  <class '__main__.C'>,
# 
#  <class '__main__.A'>,
# 
#  <class 'object'>]