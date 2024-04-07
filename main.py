#!/usr/bin/python3
""" Test link Many-To-Many HarmayStore <> Drug
"""

from models import storage
from models.pharmacy_store import PharmacyStore
from models.drugs import Drug
import uuid


def generate_store_id():
  """Generates a unique UUID value."""
  return uuid.uuid4()

# Generate a unique store_id
store_id = generate_store_id()

def generate_drug_id():
  """Generates a unique UUID value."""
  return uuid.uuid4()

# Generate a unique drug_id
drug_id = generate_drug_id()

# Create instances of PharmacyStore
pharmacy_store1 = PharmacyStore(
        store_id = store_id,
        name="Abiola Pharmacy",
        address="123 Main St",
        city="City A",
        state="State A",
        postal_code="12345",
        country="Country A",
        latitude=40.1234,
        longitude=-75.5678,
        )

pharmacy_store2 = PharmacyStore(
        store_id = store_id,
        name="Babalola Pharmacy",
        address="456 Elm St",
        city="City B",
        state="State B",
        postal_code="67890",
        country="Country B",
        latitude=35.6789,
        longitude=-80.1234,
        )

# Create instances of Drug
drug1 = Drug(
        drug_id = drug_id,
        name="Diphastom",
        price=10.99,
        description="Description for Drug X",
        category="Category X",
)

drug2 = Drug(
        drug_id = drug_id,
        name="Yeast tablets",
        price=5.99,
        description="Description for Drug Y",
)

# Associate drugs with pharmacy stores
pharmacy_store1.drugs.append(drug1)
pharmacy_store2.drugs.append(drug1)
pharmacy_store2.drugs.append(drug2)

# Save instances to the database
storage.new(pharmacy_store1)
storage.new(pharmacy_store2)
storage.new(drug1)
storage.new(drug2)
storage.save()

# Retrieve pharmacy stores for a specific drug
drug1_pharmacies = drug1.pharmacy_stores
if drug1_pharmacies:
    print(f"Pharmacy stores where Diphastom is available:")
    for store in drug1_pharmacies:
        print(store.name)
else:
    print("Diphastom is not available in any pharmacy stores.")

# Retrieve pharmacy stores for a specific drug
drug2_pharmacies = drug2.pharmacy_stores
if drug2_pharmacies:
    print(f"Pharmacy stores where Yeast tablets is available:")
    for store in drug2_pharmacies:
        print(store.name)
else:
    print("Yeast tablets is not available in any pharmacy stores.")
