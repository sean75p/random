class MyStructure:
    def __init__(self, value=0, my_list=[]):
        print("this is the initiation of the MyStruct class")
        self.value = value
        self.my_list = my_list

    def my_pop(self, listo):
        #pops the last element of a list
        #you could also just do listo[-1]
        new_list=[]

        a=len(listo)
        print("length of list:", a)
        print("last value of list:" , listo[a-1])
        for i in range(len(listo)-1):

            print(listo[i])
            new_list.append(listo[i])

        print("popped value", listo[a-1])
        print("new list", new_list)
        return new_list

    def my_push(self, value, my_list=[]):

        self.value = value
        self.my_list = my_list

        self.my_list.append(self.value)
        return self.my_list
    def my_print(self):
        print("myprint ran")

if __name__ == "__main__":

    A = MyStructure()
    A.my_print()
    A.my_push(33, [0,44])
    print(A.my_list)
    A.my_push(67, A.my_list)
    print(A.my_list)

    B= MyStructure()
    B.my_push(344, [3, 4, 5])
    print(B.my_list)
    B.my_push(555, B.my_list)
    print(B.my_list)
