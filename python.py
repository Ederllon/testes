array_ = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
req_ = int(input("Escolha um número: "))
if req_ >= 27:
    print("Tente novamente com número abaixo de 27")
else:
    def func():
        new_list = []
        c = 0
        while c < req_:
            new_list.append(array_[c])
            c = c +1
        print(new_list)
    func()    
    

