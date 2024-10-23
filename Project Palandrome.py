#Q Write a program to check that the given code is palandrome or not
list = [1, 2, 3, 2, 1]
copy_list =list.copy()
copy_list.reverse()
if(copy_list == list):
    print("This is palendrome")
else:
    print("this is not palendrome")
    