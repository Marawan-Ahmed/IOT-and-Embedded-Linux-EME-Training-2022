list=[['19016600','ahmed','100'],['19016601','mohamed','66'],['19016602','marawan','76']]
while (True):
    choice = input('choose a number from 1 to 4 ')
    if choice == '1':
        id = input('Enter the ID please ')
        name = input('Enter the name please ')
        grade = input('Enter the grade please ')
        student = [id,name,grade]
        list.append(student)
    elif choice == '2':
        id = input('Enter the ID please ')
        for i in range(len(list)):
            if id == list[i][0]:
                print('id is '+list[i][0]+' name is '+list[i][1]+' grade is '+list[i][2])
    elif choice == '3':
        name = input('Enter the name please ')
        for i in range(len(list)):
            if id == list[i][1]:
                print('id is '+list[i][0]+' name is '+list[i][1]+' grade is '+list[i][2])
    elif choice == '4':
        from operator import itemgetter
        list = sorted(list, key=itemgetter(1))
        print(list)
        with open("outfile.txt", 'w') as file:
            file.writelines('\t'.join(str(j) for j in i) + '\n' for i in list)
            
