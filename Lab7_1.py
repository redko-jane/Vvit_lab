class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def get_info(self):
        return "Имя: {} Идентификационный номер: {} ".format(self.name,self.id)

class Manager(Employee):
    def __init__(self,name,id,department):
        Employee.__init__(self,name,id)
        self.department = department
    def manage_project(self):
        return "Проектом в отделе {} управляет {}".format(self.department,self.name)
    def get_info(self):
        return "Имя: {} Идентификационный номер: {} Отдел: {} ".format(self.name,self.id,self.department)

class Technician(Employee):
    def __init__(self,name,id,specialization):
        Employee.__init__(self,name,id)
        self.specialization = specialization
    def perform_maintenance(self):
        return "Техническое обслуживание в области {} выполняет {}".format(self.specialization,self.name)
    def get_info(self):
        return "Имя: {} Идентификационный номер: {} Специализация: {} ".format(self.name,self.id,self.specialization)

class TechManager(Manager,Technician):
    def __init__(self,name,id,department,specialization):
        Manager.__init__(self,name,id,department)
        Technician.__init__(self,name,id,specialization)
        self.subordinates=[]
    def add_employee(self,employee):
        self.subordinates.append(employee)
    def get_team_info(self):
        if not self.subordinates:
            return "{} не имеет подчинённых.".format(self.name)
        team_info = "Подчинённые {}:\n".format(self.name)
        for subordinate in self.subordinates:
            team_info += "- {}\n".format(subordinate.get_info())
        return team_info
    def get_info(self):
        return "Имя: {} Идентификационный номер: {} Отдел: {} Специализация: {} ".format(self.name,self.id,self.department,self.specialization)
    def manage_project(self):
        return Manager.manage_project(self)
    def perform_maintenance(self):
        return Technician.perform_maintenance(self)
employee1 = Employee("Анна Кузнецова", 12345)
technician1 = Technician("Игорь Сидоров", 67890, "Сетевое администрирование")
manager1 = Manager("Мария Петрова", 54321, "Разработка")
tech_manager = TechManager("Сергей Васильев", 98765, "IT", "Системное администрирование")
tech_manager.add_employee(employee1)
tech_manager.add_employee(technician1)
print(employee1.get_info())
print(technician1.get_info())
print(technician1.perform_maintenance())
print(manager1.get_info())
print(manager1.manage_project())
print(tech_manager.get_info())
print(tech_manager.manage_project())
print(tech_manager.perform_maintenance())
print(tech_manager.get_team_info())
