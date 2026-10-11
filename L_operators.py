if 5 > 3 and 6 <= 10:
    print("Condition 1 satisfies")
else:
    print("Condtition 2 satisfies")

print("------------------------Students grades---------------------------------")

top_score = 100
average = 75
distinction = 60
passed = 35
fail = 25

if ( average <= top_score and distinction <= top_score or passed < top_score and fail < passed):
    print(" Congrats! you passed the exam")
else:
    print("Better luck next time")


print("---------------------------------------------------------------------------")

A = 256
B = 253
if ( not(A == B)):
    print("yes")
else:
    print("no")
    