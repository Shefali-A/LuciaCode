#print "I am most excited to learn how to pictures out of symbols"
#print "5" + "days"
#print "          @ @ @ @"
#print "       @           @"
#print "     @               @"
#print "   @                   @"
#print "  @                     @"
#print " @                       @"
#print " @                       @"
#print " @                       @"
#print " @                       @"
#print "  @                     @"
#print "   @                   @"
#print "     @               @"
#print "       @           @"
#print "          @ @ @ @"


# 1.Eat breakfeast
# 2.Make a protein shake
# 2.Brush your teeth
# 3.Change into your clothes
# 4.Put on your shoes
# 5.Walk out the door

#
# width = 5
# length = 4
# area = width * length
# #print area
#
# name = "lila"
# numberOfJeans = 5
# priceOfJeans = 10
# taxRate = 0.10
# #print name, "will spend $", numberOfJeans * priceOfJeans * (taxRate+ 1), "on", str(numberOfJeans), "pairs of jeans"
#
#
# Me = 17 - 15 + 12
# Jenny = 7 * 3
# print str(Jenny + Me)
#
# inputIsDivisible = 10
# if inputIsDivisible % 5 == 0 and inputIsDivisible % 3 == 0:
#     print "Divisible by both"
# elif inputIsDivisible % 5 == 0:
#     print "Divisible by 5"
# elif inputIsDivisible % 3 == 0:
#     print "Divisible by 3"
# else:
#     print "Divisible by neither"


# start = 10
# end = 20
#
# for i in range(start, end, 2):
#     print i
#
# i = start
# while i < end:
#     print i
#     i = i + 2

start = 2
end = 100
for i in range(start, end, 2):
    print i

# The current year is (a)
# The year I was born is (b)
# My current age is (c)
# The age I am turning this year is (result)

def age(a, b, c):
    result = a - b
    print "The current year is " + str(a) + "\nThe year I was born is " + str(b) + "\nMy current age is " + str(c) + "\nThe age I am turning this year is " + str(result)

age(2018, 2004, 13)

age(2022, 2000, 21)