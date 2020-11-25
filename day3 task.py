Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a1={'a':1,'b':2}
>>> a2={'c':3,'d':4}
>>> x=a1.copy()
>>> x.update(a2)
>>> print(x)
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> a1={'a':1,'b':2}
>>> del a1['a']
>>> print(a1)
{'b': 2}
>>> a1=['a','b','c']
>>> a2=['1','2','3']
>>> x=dict(zip(a1,a2))
>>> print(x)
{'a': '1', 'b': '2', 'c': '3'}
>>> a=set([1,2,3,4,5])
>>> print(len(a))
5
>>> a1={1,2,3}
>>> a2={4,5,6}
>>> print(a1-a2)
{1, 2, 3}
>>> 