s1 = {"alma", "orik", "shie"}
s2 = {"barma", "tastama", "alma"}
s1.symmetric_difference_update(s2)
print(s1)
#***********************************
s1 = {"alma", "orik", "shie"}
s2 = {"barma", "tastama", "alma"}
s3 = s1.symmetric_difference(s2)
print(s3)