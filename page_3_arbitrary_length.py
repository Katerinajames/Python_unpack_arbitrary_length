
import statistics
grades=[12,399,89,444]
print("---------------------------------------")

def drop_first_last(grades):
 
 first, *middle, last = grades
 return statistics.mean(middle)


print(" Our calculated average is ",drop_first_last(grades))
