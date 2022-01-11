list = input()
list = list.strip()
# print(f"[{list}]\n({list})")
num_list = list.split(",")
print(num_list)  # ['1','2','3','4','5']
print(tuple(num_list))  # ('1','2','3','4','5')
