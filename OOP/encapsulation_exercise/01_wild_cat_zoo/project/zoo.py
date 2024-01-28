from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__animal_capacity <= len(self.animals):
            return f"Not enough space for animal"
        if self.__budget < price:
            return f"Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return f"Not enough space for worker"

    def fire_worker(self, worker_name) -> str:
        try:
            worker = next(filter(lambda x: x.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        # sum_salaries = sum([w.salary for w in self.workers])
        sum_salaries = 0
        for worker in self.workers:
            sum_salaries += worker.salary
        if self.__budget >= sum_salaries:
            self.__budget -= sum_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        # sum_care_cost = sum([a.money_for_care for a in self.animals])
        sum_care_cost = 0
        for animal in self.animals:
            sum_care_cost += animal.money_for_care
        if self.__budget >= sum_care_cost:
            self.__budget -= sum_care_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        result = f"You have {len(self.animals)} animals\n"

        lion_count = sum([animal.__class__.__name__ == 'Lion' for animal in self.animals])
        tiger_count = sum([animal.__class__.__name__ == 'Tiger' for animal in self.animals])
        cheetah_count = sum([animal.__class__.__name__ == 'Cheetah' for animal in self.animals])

        lion_info = f"----- {lion_count} Lions:\n"
        tiger_info = f"----- {tiger_count} Tigers:\n"
        cheetah_info = f"----- {cheetah_count} Cheetahs:\n"

        for animal in self.animals:
            animal_data = f'{animal.__repr__()}\n'
            if animal.__class__.__name__ == "Lion":
                lion_info += animal_data
            elif animal.__class__.__name__ == "Tiger":
                tiger_info += animal_data
            elif animal.__class__.__name__ == "Cheetah":
                cheetah_info += animal_data.strip()
        return result + lion_info + tiger_info + cheetah_info

    def workers_status(self) -> str:
        result = f"You have {len(self.workers)} workers\n"

        keepers = [w.__repr__() for w in self.workers if w.__class__.__name__ == "Keeper"]
        caretakers = [w.__repr__() for w in self.workers if w.__class__.__name__ == "Caretaker"]
        vets = [w.__repr__() for w in self.workers if w.__class__.__name__ == "Vet"]

        keepers_len = f"----- {len(keepers)} Keepers:\n"
        keepers_data = "\n".join(keepers) + "\n"

        caretakers_len = f"----- {len(caretakers)} Caretakers:\n"
        caretakers_data = "\n".join(caretakers) + "\n"

        vets_len = f"----- {len(vets)} Vets:\n"
        vets_data = "\n".join(vets)

        return result + keepers_len + keepers_data + caretakers_len + \
            caretakers_data + vets_len + vets_data
