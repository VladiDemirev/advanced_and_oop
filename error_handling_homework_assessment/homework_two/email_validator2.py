class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


VALID_DOMAIN = [".com", ".bg", ".net", ".org"]
NAME_LENGTH = 5

while True:
    email = input()
    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    first_part = email.split("@")
    if len(first_part[0]) < NAME_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")

    current_domain = "." + email.split(".")[1]
    if current_domain not in VALID_DOMAIN:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
