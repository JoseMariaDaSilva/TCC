import sqlite3

class MotorModel:

    def __init__(self, _id, tag, potencia, fp, rotacao, rendimento, date, ensaios):
        self._id = id
        self.tag = tag
        self.potencia = potencia
        self.fp = fp
        self.rotacao = rotacao
        self.rendimento = rendimento
        self.date = date
        self.ensaios = ensaios

    @classmethod
    def find_by_tag(cls, tag):
        connection = sqlite3.connect("motor.db")
        cursor = connection.cursor()

        query_tag = "SELECT * FROM motor WHERE tag=?"
        result = cursor.execute(query_tag,(tag,))
        row = result.fetchone()
        print(row)
        if row:
            motor = cls(*row)
        else:
            motor = None
        connection.close()
        return motor

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('motor.db')
        cursor = connection.cursor()
        query = "SELECT * FROM motor WHERE id=?"
        result = cursor.execute(query,(_id,))
        row = result.fetchone()
        if row:
            motor = cls(*row)
        else:
            motor = None
        
        connection.close()
        return motor