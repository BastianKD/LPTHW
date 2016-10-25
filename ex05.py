name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
kg = weight * 0.454
cm = height * 2.540

print "Let's talk about %s." % name
print "He's %d iches tall." % height
print "That's", cm, "cm."
print "He's %d pounds heavy." % weight
print "That's", kg, "kg."
print "Actually that's not that heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending in the coffee." % teeth

# this line is tricky, try to get it exaclty right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
