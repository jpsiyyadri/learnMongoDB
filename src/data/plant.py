from mongoengine import (EmbeddedDocument, FloatField, IntField, ObjectIdField,
                         StringField, connect)

connect(db="mydatabase", host="mongodb://localhost:27017")


class Plant(EmbeddedDocument):
    plant_id = IntField(unique=True, primary_key=True, required=True)
    name = StringField(required=True)
    description = StringField(required=True)
    price = FloatField(required=True)
    image = StringField(required=True)
    stock = IntField(required=True)
    meta = {"collection": "plants_v2"}

    def __str__(self):
        return f"{self.name} {self.price} {self.stock}"
