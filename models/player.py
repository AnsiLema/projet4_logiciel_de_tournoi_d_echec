class Player:
    def __init__(self, lastname, firstname, national_id, birth_date):
        self.lastname = lastname
        self.firstname = firstname
        self.national_id = national_id
        self.birth_date = birth_date

    def __repr__(self):
        return f"{self.firstname} {self.lastname} (ID: {self.national_id})"
