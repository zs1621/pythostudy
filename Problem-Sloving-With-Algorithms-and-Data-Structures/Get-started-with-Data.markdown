#Atomic data types

 - int
 
```
a = 9
print a
```

 - float

```
a = 1.3
print a
```

 - bool

```
a = True
print a
```

#Built-in collection Data types

 > 除了numeric 和 boolean 类, Python 有很多强大的类. Lists, strings, tuples是有序集合. Sets and dictinoaries 是无序的 
 

##**set**

### operations, `|`, `&`, `-`, `<=` 如同数学里两个集合间的操作
  - in
  - len
  - | 
  - &
  - -
  - <=

```
a = {3, 4, 'a', False}
b = {4, 5, 'b'}
'a' in b # False
```

### methods from set
 
  - union
    - aset.union(otherset) -> 返回所有的两个集合的元素
  - intersection
    - aset.intersection(otherset) -> 返回连个集合都包含的元素的集合
  - difference
    - aset.difference(otherset) -> 返回一个新的集合，第一个集合里不在第二集合的元素
  - issubset
    - aset.issubset(otherset) -> 是否所有的元素再另外一个集合里
  - add
    - aset.add(item)
  - remove
    - aset.remove(item)
  - pop
    - aset.pop()
  - clear
    - aset.clear
    
    
##**list**
### operations, 
 - `[]` - -> Access an element of a sequence
 - `+` -> Combine sequences together
 - `*` -> Concatenate a repeated number of times
 - `in` -> Ask whether an item in an sequence
 - `len` -> Ask the number of iterms in the sequence
 - `[:]` -> Extract a part of a sequence
 
### methods
 - `append`
   - alist.append(item)
 - `insert`
   - alist.insert(i, item)
 - `pop`
   - alist.pop()
   - alist.pop(i)
 - `sort`
   - alist.sort()
 - `reverse`
   - alist.reverse()
 - `del`
   - del alist[i]
 - `index`
   - alist.index(item)
 - `count`
   - alist.count(item)
 - `remove`
   - alist.remove(item)
   
##**tuple**
 - as list, can use operations decribed above
 - it's immutable,list is mutable, so tuple have no methods can change it.
 
##**string**

### operations
 - as list, can use operations decribed above they have same name sequences
 
### methods
 - strings 里的元素值不可改变, so其方法return 新的string
 - `center`
   - astring.center(w) -> 可以再命令行里试试
   
```
a = 'abce'
len(a.center(9)) // 9
```

 - `count`
   - astring.count(item)  -> 返回某个元素的数量
 - `ljust` 
   - astring.ljust(w) -> 置←
 - `lower`
   - astring.rjust(w) -> 置→
 - `lower`
   - astring.lower() 
 - `find` 
   - astring.find(item) -> 返回某个元素的位置 index   
 - `split`
   - astring.split(schar)

##**dictionaries**

###operations
 - []
   - myDict[k]
 - in
   - key in adict
 - del
   - del adict[key]
  
###methods

 - keys
   - adict.keys()
 - values
   - adict.values()
 - items
   - adict.items() -> `type(a.items())` #list
 - get
   - adict.get(k)
 - get
   - adict.get(k, alt)
