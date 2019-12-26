items = [
    ('p1','p2',3),
    ('p3','p4',6),
    ('p5','p6',9),
    ('p7','p8',10),
]

######Maps
# num = list(map(lambda i: i[2],items))
# print(num)


#####Filters
# num = list(filter(lambda i: i[2]%3 == 0,items ))
# print(num)



#####List comprehensions
##instead of map
num = [i[2] for i in items]
print(num)
##instead of filter
num1 = [ i for i in items if i[2]%3 == 0]
print(num1)







