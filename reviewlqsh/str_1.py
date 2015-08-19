__author__ = 'qiusheng'
import time
s = ('select *'
     'from atable')

print(s)
print isinstance(s,str)
print isinstance(s,unicode)
# unicode
us = u'unicode'
print isinstance(us,basestring) # str and unicode are inherited basestring
print isinstance(us,unicode)

# methods build-in str or unicode

print s.startswith('select')
print s.capitalize()
s = 's'
s1 = '   '
print s.isspace() #  and there is least one character in S, False otherwise.
print s1.isspace() #  return True if all characters in S are whitespace
# split()

# join()

# partition()
'''
   Search for the separator sep in S, and return the part before it,
   the separator itself, and the part after it.  If the separator is not
   found, return S and two empty strings
'''
# end to  learn to string that build_in python
# sort and sorted
'''
Python lists have a built-in sort() method that modifies the list in-place
and a sorted() built-in function that builds a new sorted list from an interabel.
'''
# A simple ascending sort is very easy -- just call the sorted function. It returns a new sorted list
before_a = [1,32,-1,0]
after_a = sorted(before_a)
print after_a,id(after_a),id(before_a)
# If you don't need the original list, it's slightly more efficient.
before_a.sort()
print(before_a)
# Another difference is that the list.sort() method is only defined for lists. In contrast, the sorted() function
# accepts any iterable.
student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]
print sorted(student_tuples,key= lambda student: student[2],reverse=True) # reverse is default False.sort by age.
# key parameter to specify a function to be called on each list element prior to making comparisons.
# Same technique works for objects with named attributes.
class Student:
        def __init__(self, name, grade, age):
                self.name = name
                self.grade = grade
                self.age = age
        def __repr__(self):
                return repr((self.name, self.grade, self.age))
        def weighted_grade(self):
                return 'CBA'.index(self.grade) / float(self.age)
student_objects = [
    Student('join0','A',20),
    Student('join1','A',13),
    Student('join2','A',23),
]
#sorted(interable,cmp,key,reverse)
print sorted(student_objects,key=lambda student: student.age,reverse=True) # key is more faster than cmp
'''
The key-function patterns shown above are very common, so Python provides convenience functions
to make accessor functions easier and faster. The operator module has itemgetter,attrgetter,
and staring in Python 1.6 a methodcaller function.
Using those functions, the obove examples become simpler and faster.
'''
from operator import itemgetter, attrgetter ,methodcaller
print('for example, to sort by age ')
print('built-in function')
print sorted(student_tuples,key=itemgetter(2))
print sorted(student_objects,key=attrgetter('age'))
print('end built-in function')
print('for example, to sort by grade and age ')
print('built-in function')
print sorted(student_tuples,key=itemgetter(1,2))
print sorted(student_objects,key=attrgetter('grade','age'))
print('end built-in function') # for example test data is useful to testing  itemgeter, attrgetter,and methodcaller.

print('the third function from the operator module.')
print [(student.name,student.weighted_grade()) for student in student_objects] # before for is an item
print(sorted(student_objects,key=methodcaller('weighted_grade')))
# end sort and sorted
# some functions.
rag= False # tag is used to select funciton.
# we use and and or to select lambda function. If rag is True, we select first lambda function,otherwise
# we select the second lambda function.
process_fun = rag and(lambda s: ' '.join(s.split())) or (lambda s:s)
print(process_fun)
print(process_fun('hello   world'))
# There are some functions (e.g. lambda,filer,reduce,map) built_in
# lambda, for only one
g = lambda x: x*2
print g(10)
# step 2: for an interable
t_list = [1,2,3]
print map(g,t_list)
print [g(i) for i in t_list ]
print [x*2 for x in t_list]  # before for is an  expression,(function expression is OK)
# filter
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print filter(lambda x:x % 3 ==0,foo) # lambda is function and foo is sequence, it use time is 2.79601037685e-05
print [x for x in foo if x % 3 == 0] # It use time is 2.55287903973e-05. By contrary  filter and lambda with []
# [] is more faster that filter and lambda functions

# map function
#  first method is implemented
print [len(x) for x in 'It is raining cats and dogs'.split()].__len__() #
#  second method is implemented
print map(lambda x: len(x),'It is raining cats and dogs'.split()).__len__() # the global function map return a
# list sequence.



















