# making a list of "the_count"
the_count = [ 1, 2, 3, 4, 5]
# making a list of "fruits"
fruits = ['apples', 'oranges', 'pears', 'apricots']
# making a list of "change"
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list.
# For ... in ... is the function to make circular representation, while how can python detect "number"?
for number in the_count:
    print ("This is count %d" % number)
    
# same as above
for heihei in fruits:
    print ("A fruit of type: %s" % heihei) 
### Python cannot detect the nature of the elements inside the [], while we can put any "element" in place to make the function run!
    
# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print (" I got %r" % i)
    
# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 20 counts
for i in range (0, 6):
    print ("Adding %d to the list." % i)
    # append is a function that lists understand
    elements.append(i)
    
# now we can print them out too
for i in elements:
    print ("Element was: %d" %i )
    
