# Aryan-gupta

 I set up a global counter. The idea is pretty straightforward: every time a new booking is created, this counter ticks up and assigns a unique ID to the booking. This way, we can easily keep track of how many bookings we've got.
​The core of the program is the BookingSystem class, which is basically the blueprint for any booking request. When you create a new booking object, the _init_ method (the constructor) kicks in. It initializes all the essential details like the staff member's name and ID, a phone/reference number, and also sets up empty lists for the items and a counter for the total fare. This just makes sure every new booking starts with a clean slate.
​The class has a few methods to handle everything:
​The coustumer_info method is super basic. It just displays the staff name, ID, and number associated with the booking.
​Next up is ferry_service_details. This is where the user can add items and their prices. It's a simple loop that keeps asking for input until the user types "done." As you add stuff, it automatically calculates the total fare.

designed pattren 
encapsulation - all booking information 
future extention - in nedw types of booking

K.I.S.S
this code is written in a simple way so it is easy to read and understand .

d.r.y
the bookingdetails are stored in one class so the code is not repeated in many places

open/closed principle
the classs can extended with new booking features without changing the old code.

composition 

the programm use one class with clear methods instead of a big inheritance tree.

single responsibility principle
each methord has one clear job 

 coustumer_info() shows staff info  
 ferry_service_details() adds items and total  
booking_approval() sets the approval status  
display_booking_info() shows all details  
booking_statistic() counts approvals

Y.A.G.N.I 
0nly the needed features are coded. No extra features are added just in case



integration of Research and Practice
From research on software design principles 
encapsulation protects data by keeping it inside the class.  
SRP and Separation of Concernsmake programs easier to maintain.  
ocpand yagni encourage flexible code that grows naturally without extra featires.  

conclusion 
this booking system is a samll project that depicts 

Use ofdesign patterns like Separation of Concerns
application of design principles like srp, kiss, and ocp
integration of research and practice, showing how theory i appplied in code  




