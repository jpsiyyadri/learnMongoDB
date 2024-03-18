from mongoengine import (Document, EmbeddedDocumentListField, StringField,
                         connect)

from src.data.plant import Plant

connect(db="mydatabase", host="mongodb://localhost:27017")


class Category(Document):
    # give the table name
    meta = {"collection": "categories_v2"}
    name = StringField(required=True)

    plants = EmbeddedDocumentListField(Plant)

    def __str__(self):
        return f"{self.name} plants: {", ".join([plant for plant in self.plants])}"


if __name__ == "__main__":
    category_name = "Test Catrgory Name"
    category = Category(name=category_name)
    category.save()
    print("Category saved successfully")
