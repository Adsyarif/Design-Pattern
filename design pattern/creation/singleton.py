class Database:
    databse = None

    @classmethod
    def get_database(cls):
        if cls.databse is None:
            cls.databse = cls()
            cls.databse.init_database()
        return cls.databse

    def init_database(self):
        self.connection = "DATABASE CONNECTED"


db1 = Database.get_database()
db2 = Database.get_database()

print(db1 is db2)
print(db1)
