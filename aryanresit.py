
ferry_counter = 0

class BookingSystem():
    def __init__(self, name,id,number):
        global ferry_counter
        ferry_counter = ferry_counter + 1
    
        self.ferry_id = ferry_counter + 1
        self.staff_name = name
        self.staff_id = id
        self.number = number
        self.item = []
        self.total = 0
        self.status = "Approved"


    def coustumer_info(self):
        print("\n costumer information")

        print(f"staff_name:{self.name}")
        print(f"staff_id:{self.staff_id}")
        print(f"number:{self.number}")
        
    
    def  ferry_service_details(self):

        print("\nEnter your req items (type 'done' to finish):")
        self.item = []
        self.total = 0

        while True:
            item = input("Item name (or type 'done' to finish): ")

            if item.lower() == 'done':
                break
            else:
                price = float(input(f"Enter price for {item}: $"))
                self.item.append((item,price))
                self.total += price

        print(f"\nTotal ferry amount: ${0}")
        



    def booking_approval(self):
        if manager_approval == "approved":
            self.status = "approved"
        elif manager_approval == "pending" :
            self.status = "pending"
        else:
            manager_approval ="not_approved"
            self.status = "not_approved"
    

    def  display_booking_info(self):

        print("\n print req details")
        print("staff id:" ,self.staff_id)
        print("staff name:" ,self.staff_name)
        print("number :",self.number)
        print("status:",self.status)
        print("item:" , self.item)
        print("total:", self.total)
    



    def booking_statistic(self, all_req):

        for req in all_req:
            total = len(all_req)

            approved = 0
            pending = 0
            not_approved = 0

        if self.status =="approved":
            approved = approved + 1
        elif self.status == "pending":
            pending = pending + 1
        else:
            self.status = "not_approved"
            not_approved = not_approved + 1

req_all = BookingSystem()

req_all.coustumer_info("aryan", 43, "qwe")
# req1 = BookingSystem("aaa",4,"eee")
# req1.ferry_services_details = (["aaa"],["222"])
# req1.booking_statistic = 0

# req2 = BookingSystem ("qqq",5,"rrr")
# req2.ferry_service_details = (["rrr"],["qqq"])
# req2.booking_statistic = 0

# req3 = BookingSystem ("uuu",0,"ooo")
# req3.ferry_service_details = (["yyy"],[000])
# req3.booking_statistic = 0

# req4 = BookingSystem ("aaa",666,"zzz")
# req4.ferry_service_details = (["www"],["vvv"])
# req4.booking_statistic = 0


# req5 = BookingSystem ("ccc",444,"ddd")
# req5.ferry_service_details = (["lll"],["jjj"])
# req5.booking_statistic = 0

# all_req = [req1,req2,req3,req4,req5]

# BookingSystem.booking_statistic(all_req)

# req2.booking_approval("approved")
# req3.booking_approval("pending")
# req4.booking_approval("not_approved")



# BookingSystem.booking_statistic(all_req)














