# remove
#remove - 리스트에서 삭제
#pop - 인덱스에서 삭제


# list_a = [1,1,1,2]
# # list_a.remove(1)
# # print(list_a)

# # 1이라는 숫자를 다 지울꺼양
# # for i in list_a:
# #     list_a.remove(1)
# # print(list_a)


# # 1. solution
# # index = -1
# # for i in list_a:
# #     index += 1

# #     print(f'index : {index} i : {i} list_a : {list_a}')

# #     if i == 1:
# #         del list_a[index]
    
# # print(list_a)

# for i in list_a:
#     pass  # pass는 형식만 잡아주려고 하는거. 그냥 pass

# for i in range(len(list_a)): # 인덱스 개수만큼 순환
#     pass

# for i in range(len(list_a)-1,-1,-1): # 역순하려면 꼭 -1,-1 써야함. range(3,-1,-1)은 역순으로 / range(5) 는 0,1,2,3,4를 출력 
#     if list_a[i] == 1:
#         del list_a[i]
# print(list_a)


# # remove

# list_a = [1,1,1,2]

# for i in range(len(list_a)):
#     if 1 in list_a:
#         list_a.remove(1)
# print(list_a)


# remove

list_a = [1,1,1,1,2,2,2,2,2]
for i in range(len(list_a)):
    print('*')
    if 1 in list_a:
        list_a.remove(1)
    else:
        break
print(list_a)



numbers = [273,103,5,32,65,9,72,800,99]
for number in numbers:
    if number >= 100:
        print(number)





