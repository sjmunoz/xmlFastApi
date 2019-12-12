import datetime
import random


def random_date():
    """Generate a random datetime between `start` and `end`"""
    start = datetime.datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
    end = datetime.datetime.strptime('1/1/2019 4:50 AM', '%m/%d/%Y %I:%M %p')
    return start + datetime.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

def random_indications():
    indication_list = ["Tecito", "Deporte", "Distrarese", "Mermelada"]
    return random.choice(indication_list)

def random_diagnosis():
    diagnosis_list = ["Obesidad", "Crece Poco", "Mala Nutricion", "Falta Calcio"]
    return random.choice(diagnosis_list)

class baseNum:
    def __init__(self):
        self.num = 0

    def incBase(self):
        self.num += 1
        return self.num


incremental = baseNum()
dicti = {
    "id": random.randint(0,5000), 
    "doctor": random.randint(1,300), 
    "patient": random.randint(1,300), 
    "medicCenter": random.randint(1,15), 
    "responsible": random.randint(1,1000), 
    "appointmentDate": random_date(), 
    "indications": random_indications(), 
    "diagnosis": random_diagnosis(), 
    "weight": random.randint(2200, 3500), 
    "height": random.randint(40, 55), 
    "skullCircumference": random.randint(40, 55), 
    "nutritionalStatus": "Sana", 
    "nutritionalStatusComment": "Siga Así", 
    "lactation": "Cada 2 horas", 
    "lactationComment": "", 
    "psychomotorDev": "", 
    "psychomotorDevComment": "", 
    "CIAP2Code": "", 
    "CIAP2Diagnosis": "", 
    "CIE10Code": "", 
    "CIE10Diagnosis": "", 
    "observations": "", 
    "nextAppointment": "", 
    "internal": "", 
    "isRegular": "", 
}