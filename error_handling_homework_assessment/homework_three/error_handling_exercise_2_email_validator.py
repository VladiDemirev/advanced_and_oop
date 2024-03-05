# 2.Email Validator
class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = ["com", "bg", "net", "org"]
email = input()

while email != "End":

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if len(email.split("@")[0]) < 5:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = email.split(".")[-1]
    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email = input()
