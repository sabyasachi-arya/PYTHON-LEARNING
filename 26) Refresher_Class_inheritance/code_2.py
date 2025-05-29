# class inheritance
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


new_device = Device("Mouse", "Bluetooth")
print(new_device)
new_device.disconnect()