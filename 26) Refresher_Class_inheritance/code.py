class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device: {self.name!r} ({self.connected_by})"  # !r calls the repr method of self.name

    def disconnect(self):
        self.connected = False
        print("Disconnected.")


class Printer(Device):  # this means   <class a_new_class(inherits_from_this_class)>
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)  # it gets the super class or parent class which is the Device class
        # and it's going to call the __init__ method of that super class
        self.capacity = capacity  # maximum capacity
        self.remaining_pages = capacity  # current capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def printing_page(self, pages):
        if not self.connected:  # similar of, if self.connected == False:
            print("Your device is not connected")
            return
        print(f"Printing {pages} pages")
        self.remaining_pages -= pages


printer_device = Printer("HP Inkjet 3600", "Bluetooth", 200)
printer_device.printing_page(40)
print(printer_device)
printer_device.disconnect()  # first python checks for the disconnect method in Printer class
# if not found in Printer class then it proceeds to check the parent class which is Super class or Device class
printer_device.printing_page(20)