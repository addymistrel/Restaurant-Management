import time
def orderlist():
    print("\n\n{} >> ORDER LIST << {}\n".format("-"*23,"-"*23))
    with open("orderslist.txt","r") as ol:
        data = ol.readlines()
        if len(data) == 0:
            print(" --- Empty ---")
            return True
        for i in data:
            arr = i.strip().split(',')
            text = ", ".join(arr[1::])
            print("Order No. {} ---> {}".format(arr[0],text))
        print()

def dispatch():
    a = orderlist()
    if a:
        return
    ord_l = input("Enter Order Nos. To Dispatch ---> ").split()
    for i in ord_l:
        temp_l = []
        with open("orderslist.txt","r") as ol:
            data = ol.readlines()
            for j in data:
                arr = j.strip().split(',')
                if arr[0] == i:
                    continue
                ux = ",".join(arr)+"\n"
                temp_l.append(ux)
        open("orderslist.txt","w").close()
        with open("orderslist.txt","w") as ol:
            for k in temp_l:
                ol.writelines(k)
    print()
    print("\nDispatching Orders ....\n")
    for i in ord_l:
        time.sleep(1.5)
        print("Order No. {} Dispatched Succesfully.".format(i))
    time.sleep(1.5)
    print("\nAll Orders Dispatched Successfully ......\n")        