# Aryan-gupta

 I set up a global counter. The idea is pretty straightforward: every time a new booking is created, this counter ticks up and assigns a unique ID to the booking. This way, we can easily keep track of how many bookings we've got.
​The core of the program is the BookingSystem class, which is basically the blueprint for any booking request. When you create a new booking object, the _init_ method (the constructor) kicks in. It initializes all the essential details like the staff member's name and ID, a phone/reference number, and also sets up empty lists for the items and a counter for the total fare. This just makes sure every new booking starts with a clean slate.
​The class has a few methods to handle everything:
​The coustumer_info method is super basic. It just displays the staff name, ID, and number associated with the booking.
​Next up is ferry_service_details. This is where the user can add items and their prices. It's a simple loop that keeps asking for input until the user types "done." As you add stuff, it automatically calculates the total fare.
ill describe the code reflects the design principles and concepts


encapsulation 

defination

Encapsulation is the principle of bundling data and methods that operate on that data within a single unit, such as a class. It also restricts direct access to some of the object’s components, which helps protect the integrity of the data.

application in code 

in my code the BookingSystem class stores all the booking information such as staff name, id, number, items, total, and status inside the class. All the actions like adding items or showing details are done using methods

improvement suggestion:
To improve, I can use private variables for example _staff_name and create getter and setter methods to protect the data better

single responsibility principle (srp)

definition

SRP states that every class or method should have only one reason to change. Each should perform one specific function.

application in code

Each method in the bookingsystem class has a clear purpose:

coustumer_info() displays staff details
ferry_service_details() collects items and calculates the total
booking_approval() updates booking approval status
display_booking_info() shows booking information
booking_statistic() counts and displays booking status statistics

improvement system 

to make this better, i could move the statistics part into a new class, such as BookingStats, so the main class only manages bookings

open/closed principle (ocp)

defination 

OCP means that software entities should be open for extension but closed for modification. This allows developers to add new features without altering existing, stable code.

application in code

my bookingsystem class can easily be extended. for example, i can add a new method for cancel booking or calculate discount without changing old code

improvement suggesion 

i can use inheritance or subclasses in the future, such as OnlineBooking or VIPBooking, which will extend the class instead of editing it.

don’t repeat yourself (DRY)

defination 

DRY emphasizes that every piece of knowledge should have a single, unambiguous representation in the system.

application in code 

all booking details and functions are inside one class, so I don’t repeat the same logic multiple times. For example ferry service()

improvment suggestion 

i can improve DRY by creating helper methods (like calculate_total()) if the same code is used again in other places later

keep it simple (KISS)

definition  

KISS promotes simplicity in design. Code should be easy to read, understand, and maintain.

application in code 

my code uses a single class and simple methods that anyone can read and understand the logic is written step-by-step

improvment suggestions 

I can fix small spelling mistakes (like changing coustumer_info to customer_info) and fix the line print(f"\nTotal ferry amount: ${0}") to print(f"\nTotal ferry amount: ${self.total}") so it shows the right total.

composition over in heritance 

defination 

Composition involves building complex objects from simpler ones rather than relying on inheritance. It helps create flexible and maintainable code.

application in code 

my program uses one main class that includes all the needed functions it is not too complicated and it avoids deep inheritance 

improvment suggestion

i can add small helper classes such as bookingItem or Payment that work together with bookingsystem to make it more organized.


you aren’t gonna need it (YAGNI)

defination 

YAGNI warns against adding features that are not currently necessary. developers should implement only what is required at the moment.

application in code
i only added features that the program needs — booking creation, total fare, and approval there are no extra or unused features

improvment suggestion 
i need to Keep the code focused and avoid adding extra functions until they are really needed.

how these principles improve my codes 

hey make the code easier to read and understand
they help me find and fix errors faster
they make it simpler to add new features in the future
they ensure that the program is organized, clean, and reusable

integration of research and practice

according to research on software engineering, applying principles such as Encapsulation, SRP, and OCP enhances software maintainability and flexibility. Encapsulation helps secure data within classes, while SRP and Separation of Concerns make systems easier to understand and update. OCP and YAGNI promote scalability and efficient growth of the system without adding unnecessary complexity. These principles are effectively reflected in the BookingSystem program, although there is room for refinement to achieve better adherence to software design standards.

Conclusion

the bookingsystem program demonstrates the practical application of fundamental software design principles. it successfully applies Encapsulation, KISS, DRY, and YAGNI, while also allowing for Open/Closed extension and adhering to the Single Responsibility Principle. Although the code is simple and functional, minor improvements such as better naming conventions, improved encapsulation, and separation of responsibilities could enhance the program’s maintainability and scalability.
