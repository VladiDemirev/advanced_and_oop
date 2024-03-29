from typing import List


class EmailValidator:
    def __init__(self, min_length: int, mails: List[str], domains: List[str]):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str) -> bool:
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str) -> bool:
        # return any([mail == m for m in self.mails])
        return mail in self.mails

    def __is_domain_valid(self, domain: str) -> bool:
        # return any([domain == d for d in self.domains])
        return domain in self.domains

    def validate(self, email: str) -> bool:
        email_data = email.split("@")
        username = email_data[0]
        mail, domain = email_data[1].split(".")
        # return all([self.__is_name_valid(username), self.__is_mail_valid(mail), self.__is_domain_valid(domain)])
        return (
                self.__is_name_valid(username) and
                self.__is_mail_valid(mail) and
                self.__is_domain_valid(domain)
        )


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
