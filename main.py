from fastapi import FastAPI
import names
from lxml import etree
from back import dicti
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/appointments")
def r_patients():
    root = etree.Element("Appointments")
    for i in range(random.randint(100, 300)):
        new_patient(root)
    etree.tostring(root, pretty_print=True)
    return{etree.tostring(root, method='xml', pretty_print=True)}

@app.get("/appointment/{appointment_id}")
def r_patient(appointment_id: int):
    root = etree.Element("Appointments")
    new_patient(root, appointment_id)
    return etree.tostring(root)


def new_patient(root, *args):
    appointment = etree.SubElement(root, "Appointment")
    for i in dicti:
        if (i == "id" and len(args) > 0):
            etree.SubElement(appointment, i).text = str(args[0])
        else:
            etree.SubElement(appointment, i).text = str(dicti[i])