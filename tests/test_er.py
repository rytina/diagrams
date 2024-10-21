import os
import random
import string
import unittest

from diagrams import Diagram
from diagrams.er import Entity, Relationship, Attribute


class ERDiagramTest(unittest.TestCase):
    def setUp(self):
        self.name = "er_diagram-" + "".join([random.choice(string.hexdigits) for n in range(7)]).lower()

    def tearDown(self):
        try:
            os.remove(self.name + ".png")
        except FileNotFoundError:
            pass

    def test_entities(self):
        with Diagram(name=self.name, show=False):
            vets = Entity("vets")
            specialties = Entity("specialties")
            vet_specialties = Entity("vet_specialties")
            types = Entity("types")
            owners = Entity("owners")
            pets = Entity("pets")
            visits = Entity("visits")

    def test_attributes(self):
        with Diagram(name=self.name, show=False):
            vets_id = Attribute("id")
            vets_first_name = Attribute("first_name")
            vets_last_name = Attribute("last_name")
            specialties_id = Attribute("id")
            specialties_name = Attribute("name")
            vet_specialties_vet_id = Attribute("vet_id")
            vet_specialties_specialty_id = Attribute("specialty_id")
            types_id = Attribute("id")
            types_name = Attribute("name")
            owners_id = Attribute("id")
            owners_first_name = Attribute("first_name")
            owners_last_name = Attribute("last_name")
            owners_address = Attribute("address")
            owners_city = Attribute("city")
            owners_telephone = Attribute("telephone")
            pets_id = Attribute("id")
            pets_name = Attribute("name")
            pets_birth_date = Attribute("birth_date")
            pets_type_id = Attribute("type_id")
            pets_owner_id = Attribute("owner_id")
            visits_id = Attribute("id")
            visits_pet_id = Attribute("pet_id")
            visits_visit_date = Attribute("visit_date")
            visits_description = Attribute("description")

    def test_relationships(self):
        with Diagram(name=self.name, show=False):
            vets = Entity("vets")
            specialties = Entity("specialties")
            vet_specialties = Entity("vet_specialties")
            types = Entity("types")
            owners = Entity("owners")
            pets = Entity("pets")
            visits = Entity("visits")

            vets_id = Attribute("id")
            vets_first_name = Attribute("first_name")
            vets_last_name = Attribute("last_name")
            specialties_id = Attribute("id")
            specialties_name = Attribute("name")
            vet_specialties_vet_id = Attribute("vet_id")
            vet_specialties_specialty_id = Attribute("specialty_id")
            types_id = Attribute("id")
            types_name = Attribute("name")
            owners_id = Attribute("id")
            owners_first_name = Attribute("first_name")
            owners_last_name = Attribute("last_name")
            owners_address = Attribute("address")
            owners_city = Attribute("city")
            owners_telephone = Attribute("telephone")
            pets_id = Attribute("id")
            pets_name = Attribute("name")
            pets_birth_date = Attribute("birth_date")
            pets_type_id = Attribute("type_id")
            pets_owner_id = Attribute("owner_id")
            visits_id = Attribute("id")
            visits_pet_id = Attribute("pet_id")
            visits_visit_date = Attribute("visit_date")
            visits_description = Attribute("description")

            vets >> Relationship("has") >> [vets_id, vets_first_name, vets_last_name]
            specialties >> Relationship("has") >> [specialties_id, specialties_name]
            vet_specialties >> Relationship("has") >> [vet_specialties_vet_id, vet_specialties_specialty_id]
            types >> Relationship("has") >> [types_id, types_name]
            owners >> Relationship("has") >> [owners_id, owners_first_name, owners_last_name, owners_address, owners_city, owners_telephone]
            pets >> Relationship("has") >> [pets_id, pets_name, pets_birth_date, pets_type_id, pets_owner_id]
            visits >> Relationship("has") >> [visits_id, visits_pet_id, visits_visit_date, visits_description]

            vets >> Relationship("specializes in") >> vet_specialties
            vet_specialties >> Relationship("is a") >> specialties
            pets >> Relationship("belongs to") >> types
            pets >> Relationship("owned by") >> owners
            visits >> Relationship("for") >> pets
