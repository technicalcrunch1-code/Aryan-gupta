
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



explaining the whole code

 I set up a global counter. The idea is pretty straightforward: every time a new booking is created, this counter ticks up and assigns a unique ID to the booking. This way, we can easily keep track of how many bookings we've got.
​The core of the program is the BookingSystem class, which is basically the blueprint for any booking request. When you create a new booking object, the _init_ method (the constructor) kicks in. It initializes all the essential details like the staff member's name and ID, a phone/reference number, and also sets up empty lists for the items and a counter for the total fare. This just makes sure every new booking starts with a clean slate.
​The class has a few methods to handle everything:
​The coustumer_info method is super basic. It just displays the staff name, ID, and number associated with the booking.
​Next up is ferry_service_details. This is where the user can add items and their prices. It's a simple loop that keeps asking for input until the user types "done." As you add stuff, it automatically calculates the total fare.
​There's also a method for handling booking approval. This lets a manager update the status of the booking to "approved," "pending," or "not approved."
​To get a full picture, the display_booking_info method prints out a complete summary of everything: staff details, the booking status, all the items requested, and the final total fare.
​Lastly, I made a booking_statistics method. This one is supposed to look at a whole list of booking objects and spit out the number of approved, pending, and not approved bookings.
​Basically, every function in the class has a specific job: one creates the booking, another shows the details, one calculates the costs, and others handle approvals and stats. Together, they make a simple system for keeping ferry booking records.
​Yeah, I know the code has a few bugs, like some variable names are misspelled and I might have missed a parameter or two, but the concept is solid. It’s a good example of how you can use object-oriented programming to model a real-world system like this. It was a decent way to practice Python and get a better handle on how classes work












