from typing import List
from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student

from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENTS = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str) -> str:
        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")
        loan = self.VALID_LOANS[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float) -> str:
        if client_type not in self.VALID_CLIENTS:
            return "Invalid client type!"
        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."
        client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str) -> str:
        loan = next((l for l in self.loans if l.__class__.__name__ == loan_type), None)
        client = next((c for c in self.clients if c.client_id == client_id), None)
        if (
                (loan_type == "StudentLoan" and client.__class__.__name__ == "Adult") or
                (loan_type == "MortgageLoan" and client.__class__.__name__ == "Student")
        ):
            raise Exception("Inappropriate loan type!")
        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str) -> str:
        client = next((c for c in self.clients if c.client_id == client_id), None)
        if client is None:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str) -> str:
        changed_loans = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                changed_loans += 1
        return f"Successfully changed {changed_loans} loans."

    def increase_clients_interest(self, min_rate: float) -> str:
        changed_client_rates = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_client_rates += 1
        return f"Number of clients affected: {changed_client_rates}."

    def get_statistics(self):
        avg_client_interest_rate = sum(c.interest for c in self.clients) / len(self.clients) if self.clients else 0.00
        # total_sum = 0
        # for c in self.clients:
        #     for l in c.loans:
        #         total_sum += l.amount
        total_sum = sum([sum([l.amount for l in c.loans] )for c in self.clients])
        result = [f"Active Clients: {len(self.clients)}",
                  f"Total Income: {sum(c.income for c in self.clients):.2f}",
                  f"Granted Loans: {sum(len(c.loans) for c in self.clients)}, "
                  f"Total Sum: {total_sum:.2f}",
                  f"Available Loans: {len(self.loans)}, Total Sum: {sum([l.amount for l in self.loans]):.2f}",
                  f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"]
        return "\n".join(result)
