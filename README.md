# Aryan-gupta

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

