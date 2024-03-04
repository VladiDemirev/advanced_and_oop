class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


MIN_NAME_LENGTH = 5
ALLOWED_DOMAINS = [".com", ".bg", ".org", ".net"]

while True:
    command = input()

    if command == "End":
        break

    if "@" not in command:
        raise MustContainAtSymbolError("Email must contain @")

    name = command.split("@")[0]

    if len(name) < MIN_NAME_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = "." + command.split(".")[-1]

    if domain not in ALLOWED_DOMAINS:
        # raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(ALLOWED_DOMAINS)}")

    print("Email is valid")
