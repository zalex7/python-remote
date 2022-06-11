class Warehouse:
    def __init__(self, number, address, max_capacity):
        self.number = number
        self.address = address
        self.max_capacity = max_capacity
        self.free_spaces = max_capacity
        self.records = 0
        self.equipment = {}
        self.database = {}
        self.log = {}

    def to_warehouse(self, obj_id, quantity, department):
        if quantity <= self.free_spaces:
            self.records += 1
            self.log[self.records] = ["in", obj_id, quantity, department]
            self.database[obj_id] += quantity
            self.free_spaces -= quantity
        else:
            print(f"Not not enough free space in the warehouse № {self.number} at {self.address}!")

    def from_warehouse(self, obj_id, quantity, department):
        if quantity < self.database[obj_id]:
            self.records += 1
            self.log[self.records] = ["out", obj_id, quantity, department]
            self.database[obj_id] -= quantity
            self.free_spaces += quantity
        elif quantity == self.database[obj_id]:
            self.records += 1
            self.log[self.records] = ["out", obj_id, quantity, department]
            self.database.pop(obj_id)
            self.free_spaces += quantity
            self.remove_equipment(obj_id)
        else:
            print("Not not enough required equipment in warehouse!")

    def add_equipment(self, obj):
        if obj in self.equipment.values():
            return list(self.equipment.keys())[list(self.equipment.values()).index(obj)]
        else:
            if self.equipment == {}:
                equipment_id = 1
            else:
                equipment_id = max(self.equipment.keys()) + 1
            self.equipment[equipment_id] = obj
            return equipment_id

    def remove_equipment(self, obj_id):
        return self.equipment.pop(obj_id)


class OfficeEquipment:
    def __init__(self, brand, model, paper_format, price):
        self.brand = brand
        self.model = model
        self.paper_format = paper_format
        self.price = price

    def __eq__(self, other):
        if isinstance(other, (Printer, Scanner, Xerox)):
            return all((self.brand == other.brand, self.model == other.model, self.paper_format == other.paper_format,
                        self.price == other.price))
        return NotImplemented


class Printer(OfficeEquipment):
    def __init__(self, brand, model, paper_format, price, print_type, cartridge_resource):
        super().__init__(brand, model, paper_format, price)
        self.print_type = print_type
        self.cartridge_resource = cartridge_resource


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, paper_format, price, sensor_type, resolution):
        super().__init__(brand, model, paper_format, price)
        self.sensor_type = sensor_type
        self.resolution = resolution


class Xerox(OfficeEquipment):
    def __init__(self, brand, model, paper_format, price, copy_speed, max_copy):
        super().__init__(brand, model, paper_format, price)
        self.copy_speed = copy_speed
        self.max_copy = max_copy


class Menu:
    commands = ["Show equipment in warehouse", "Input equipment type", "Place equipment to warehouse",
                "Take equipment from warehouse", "Quit"]
    type_of_equipment = ["Printer", "Scanner", "Xerox"]

    @staticmethod
    def check_types(value, type):
        if type == "int":
            try:
                int(value)
            except ValueError:
                return False
            else:
                return True
        elif type == "float":
            try:
                float(value)
            except ValueError:
                return False
            else:
                return True
        else:
            return False


w1 = Warehouse(1, "Ryazan, Lenina st, 28", 100)
m = Menu
while True:
    print("-" * 30)
    print(*[f"{i}) {el}" for i, el in enumerate(m.commands, 1)], sep="\n")
    print("-" * 30)
    command = input("Input command: ")
    if command.isdigit():
        c = int(command)
        if 1 <= c <= 4:
            if c == 1:
                if w1.equipment == {}:
                    print("There is no equipment in stock at the moment")
                    continue
                else:
                    print(*[f"{key}) {' / '.join([value.brand, value.model, value.paper_format, str(value.price)])}" for
                            key, value in w1.equipment.items()], sep="\n")
                    continue
            elif c == 2:
                print("-" * 30)
                print(*[f"{i}) {el}" for i, el in enumerate(m.type_of_equipment, 1)], sep="\n")
                print("-" * 30)
                command = input("Input command: ")
                if command.isdigit():
                    c = int(command)
                    if 1 <= c <= 3:
                        if c == 1:
                            param = input(
                                "Input brand, model, paper_format, price, print_type, cartridge_resource: ").split()
                            if m.check_types(param[3], "float") and m.check_types(param[5], "int"):
                                w1.add_equipment(
                                    Printer(param[0], param[1], param[2], float(param[3]), param[4], int(param[5])))
                                continue
                            else:
                                print("Input parameters are incorrect")
                                continue
                        elif c == 2:
                            param = input(
                                "Input brand, model, paper_format, price, sensor_type, resolution: ").split()
                            if m.check_types(param[3], "float") and m.check_types(param[5], "int"):
                                w1.add_equipment(
                                    Scanner(param[0], param[1], param[2], float(param[3]), param[4], int(param[5])))
                                continue
                            else:
                                print("Input parameters are incorrect")
                                continue
                        elif c == 3:
                            param = input(
                                "Input brand, model, paper_format, price, copy_speed, max_copy: ").split()
                            if m.check_types(param[3], "float") and m.check_types(param[5], "int"):
                                w1.add_equipment(
                                    Xerox(param[0], param[1], param[2], float(param[3]), param[4], int(param[5])))
                                continue
                            else:
                                print("Input parameters are incorrect")
                                continue
            elif c == 3:
                print(*[f"{key}) {' / '.join([value.brand, value.model, value.paper_format, str(value.price)])}" for
                        key, value in w1.equipment.items()], sep="\n")
                equipment_id = input("Enter the number of the required equipment: ")
                if equipment_id.isdigit():
                    equipment_id = int(equipment_id)
                    if 1 <= equipment_id <= max(w1.equipment.keys()):
                        equipment_quantity = input("Input necessary equipment quantity: ")
                        if equipment_quantity.isdigit():
                            equipment_quantity = int(equipment_quantity)
                            w1.to_warehouse(equipment_id, equipment_quantity, input("Input department title: "))
                            continue
            elif c == 4:
                print(*[f"{key}) {' / '.join([value.brand, value.model, value.paper_format, str(value.price)])}" for
                        key, value in w1.equipment.items()], sep="\n")
                equipment_id = input("Enter the number of the required equipment: ")
                if equipment_id.isdigit():
                    equipment_id = int(equipment_id)
                    if 1 <= equipment_id <= max(w1.equipment.keys()):
                        equipment_quantity = input("Input necessary equipment quantity: ")
                        if equipment_quantity.isdigit():
                            equipment_quantity = int(equipment_quantity)
                            w1.from_warehouse(equipment_id, equipment_quantity, input("Input department title: "))
                            continue
            elif c == 5:
                break
    print("invalid command. please, try again.")
