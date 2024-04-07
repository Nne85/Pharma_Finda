# models/custom_encoder.py
import json
from models.pharmacy_store import PharmacyStore
from models.drugs import Drug
from models.users import User
from models.drug_store_inventory import DrugStoreInventory

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, PharmacyStore):
            # ... (PharmacyStore serialization code)
            return {
                'id': obj.id,
                'name': obj.name,
                'address': obj.address,
                'city': obj.city,
                'state': obj.state,
                'postal_code': obj.postal_code,
                'country': obj.country,
                'latitude': obj.latitude,
                'longitude': obj.longitude,
                'drugs': [drug.to_dict() for drug in obj.drugs]
            }
        elif isinstance(obj, Drug):
            return {
                'id': obj.id,
                'name': obj.name,
                'price': obj.price,
                'description': obj.description,
                'category': obj.category,
                'in_stock': obj.in_stock
            }
        elif isinstance(obj, User):
            return {
                'id': obj.id,
                'name': obj.name,
                'email': obj.email,
                'location': obj.location
            }
        elif isinstance(obj, DrugStoreInventory):
            return {
                'id': obj.id,
                'pharmacy_id': obj.pharmacy_id,
                'drug_id': obj.drug_id,
                'stock_quantity': obj.stock_quantity
            }
        return super().default(obj)