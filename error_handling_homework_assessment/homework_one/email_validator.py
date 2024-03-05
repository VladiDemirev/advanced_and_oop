class MustContainAtSymbolError(Exception):
    pass

class NameTooShortError(Exception):
    pass

class InvalidDomainError(Exception):
    pass


NAME_MIN_LENGTH = 5
ACCEPTED_DOMAINS = [".com", ".bg", ".org", ".net"]

while True:
    current_email = input()
    if current_email == "End":
        break

    index_at = current_email.find("@")
    if index_at != -1:
        if len(current_email[0:index_at]) < NAME_MIN_LENGTH:
            raise NameTooShortError("Name must be more than 4 characters")
    else:
        raise MustContainAtSymbolError("Email must contain @")

    dot_index = current_email.find(".")
    if current_email[dot_index:] not in ACCEPTED_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")