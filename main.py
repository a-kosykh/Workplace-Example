from datetime import date


class Subdivision:
    def __init__(self, name=None, desc=None):
        self.name = name
        self.desc = desc


class Position:
    def __init__(self, name, subdivision, rate, share):
        self.name = name
        self.subdivision = subdivision
        self.rate = rate
        self.share = share


class Employee:
    def __init__(self, name, birth_date, employment_date, snils, position=None):
        self.name = name
        self.birth_date = birth_date
        self.position = position
        self.employment_date = employment_date
        self.snils = snils


class DatabaseLayer:
    def __init__(self, subdivs, positions, employees):
        self.__database = {
            "subdivisions": subdivs,
            "positions": positions,
            "employees": employees
        }

    def add_position(self, name, subdiv_name, rate, share):
        subdiv = self._get_subdivision(subdiv_name)
        if subdiv is not None:
            print(f"Position {name} is added")
            self.__database.get("positions").append(
                Position(name, subdiv, rate, share)
            )

    def add_employee(self, name, birth_date, snils, position=None):
        self.__database.get("employees").append(
            Employee(name, birth_date, date.today(), snils, position)
        )

    def get_employees(self):
        print("get_employees")
        for employee in self.__database.get("employees"):
            print(employee.name, " --- ", employee.birth_date, " --- ", employee.snils)

        return self.__database.get("employees")

    def find_employee(self, name=None, snils=None):
        rv = []
        print("find_employee")
        for employee in self.__database.get("employees"):
            if employee.name == name or employee.snils == snils:
                print(f"Name: {employee.name}")
                print(f"Birth Date: {employee.birth_date}")
                print(f"Employment Date: {employee.employment_date}")
                print(f"SNILS: {employee.snils}")
                if employee.position is not None:
                    print(f"Position: {employee.position.name}")
                    print(f"Subdivision: {employee.position.subdivision.name}")
                    print(f"Rate: {employee.position.rate}")
                    print(f"Share: {employee.position.share}")
                rv.append(employee)
        return rv

    def change_employee(self, snils, new_name=None, new_position_name=None):
        new_position = None
        if new_position_name is not None:
            for position in self.__database.get("positions"):
                if position.name == new_position_name:
                    new_position = position
                    break

        for employee in self.__database.get("employees"):
            if employee.snils == snils:
                print(f"Employee {employee.name} ({employee.snils}) found! Changing"
                      f" to {new_name}")
                if new_position is not None:
                    print(f"New position: {new_position.name}")
                employee.name = new_name
                employee.position = new_position

    def delete_employee(self, snils):
        for employee in self.__database.get("employees"):
            if employee.snils == snils:
                print(f"Employee {employee.name} ({employee.snils}) found! Deleting...")
                self.__database.get("employees").remove(
                    employee
                )

    def add_subdivision(self, name=None, desc=None):
        self.__database.get("subdivisions").append(
            Subdivision(name, desc)
        )
        print(f"Subdivision {name} added")

    def _get_subdivision(self, name):
        for subdivision in self.__database.get("subdivisions"):
            if subdivision.name == name:
                return subdivision
        return None

    def list_subdivisions(self):
        print("list_subdivisions")
        for subdivision in self.__database.get("subdivisions"):
            print(subdivision.name)

        return self.__database.get("subdivisions")

    def change_subdivision(self, name, new_name, new_desc=None):
        subdiv = self._get_subdivision(name)
        if subdiv is not None:
            print("Subdiv found! Changing...")
            subdiv.name = new_name
            subdiv.desc = new_desc

    def delete_subdivision(self, name):
        subdiv = self._get_subdivision(name)
        if subdiv is not None:
            print(f"subdiv {name} found! Deleting....")
            for employee in self.__database.get("employees"):
                if employee.position is not None and employee.position.subdivision == subdiv:
                    employee.position = None
            for position in self.__database.get("positions"):
                if position.subdivision == subdiv:
                    position.subdivision = None
            self.__database.get("subdivisions").remove(
                subdiv
            )


def fill_db():
    subdivs = [Subdivision("Администрация", "Администрация"),
               Subdivision("Бухгалтерия", "Бухгалтерия")]

    positions = [Position("Генеральный директор", subdivs[0], 100000, 1),
                 Position("Зам. генерального директора", subdivs[0], 80000, 1),
                 Position("Бухгалтер", subdivs[1], 50000, 1),
                 Position("Кассир", subdivs[1], 40000, 0.5)]
    employees = [
        Employee("Иванов И.И.", date(1989, 2, 6), date(2007, 2, 3), "13322564", positions[0]),
        Employee("Козлов И.И.", date(1985, 5, 6), date(2007, 2, 3), "22324788", positions[1]),
        Employee("Петрова А.В.", date(1995, 12, 6), date(2013, 12, 3), "33676569", positions[2]),
        Employee("Дроздов А.И.", date(1991, 6, 14), date(2019, 2, 3), "45322564", positions[3])
    ]

    return DatabaseLayer(subdivs, positions, employees)


def main():
    db = fill_db()


    db.get_employees()
    print("\n")

    db.list_subdivisions()
    print("\n")

    db.add_position("Директор по маркетингу", 'Администрация', 0.7, 60000)
    print("\n")

    db.add_employee("Косых Александр", date(1999, 1, 1), "666666", )
    print("\n")

    db.change_employee("666666", "Косых Алекснадр", "Директор по маркетингу")
    print("\n")

    db.find_employee(snils="666666")
    print("\n")

    db.add_subdivision("Хозотдел")
    print("\n")

    db.change_subdivision("Хозотдел", "Хозяйственный отдел", "")
    print("\n")

    db.delete_subdivision("Хозяйственный отдел")
    print("\n")

    db.delete_subdivision("Администрация")
    print("\n")

    db.list_subdivisions()

    db.find_employee(snils="666666")
    print("\n")

    print()


if __name__ == '__main__':
    main()
