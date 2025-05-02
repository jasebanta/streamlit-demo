import pandas as pd
import random
from faker import Faker

fake = Faker()
Faker.seed()
random.seed()

class SampleData:

    def __init__(self, size):
        self.size = size
        self.demo_records = []
        self.health_records = []
        self.df_demo = self.demographic_data()
        self.df_health = self.health_data() #corrected method call

    def demographic_data(self):
        # Generate Demographic Data
        for _ in range(self.size):
            self.demo_records.append({
                "person_id": fake.uuid4(),
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "dob": fake.date_of_birth(minimum_age=18, maximum_age=80).strftime("%Y-%m-%d"),
                "ssn": fake.ssn(),
                "gender": random.choice(["Male", "Female", "Non-binary", "Other"]),
                "ethnicity": random.choice(["White", "Black", "Hispanic", "Asian", "Other"]),
                "phone": fake.phone_number(),
                "email": fake.email(),
                "record_created_dt": fake.date_time_this_decade().strftime("%Y-%m-%d %H:%M:%S"),
                "consent": random.choice([True, False])
            })
        return pd.DataFrame(self.demo_records) # corrected variable scope

    def health_data(self):
        # Generate Health Data
        allergies = ["Peanuts", "Dairy", "Shellfish", "Gluten", "Pollen"]
        substance_abuse = ["Alcohol", "Tobacco", "Cannabis", "Opioids", "None"]

        for index, row in self.df_demo.iterrows():
            self.health_records.append({
                "person_id": row["person_id"],
                "allergy": random.choice(allergies + [None] * 15),  # 5 values, rest null
                "substance_abuse": random.choice(substance_abuse + [None] * 15),
                "blood_pressure": random.choice(["Normal", "High", "Low", None, None]),
                "cholesterol": random.choice(["Normal", "High", "Low", None, None]),
                "heart_disease": random.choice(["Yes", "No", None, None, None]),
                "diabetes": random.choice(["Type 1", "Type 2", "None", None, None]),
                "bmi": round(random.uniform(18.5, 35.0), 1),
                "smoker": random.choice(["Yes", "No", None, None]),
                "exercise_freq": random.choice(["Daily", "Weekly", "Rarely", None]),
                "sleep_hours": random.randint(4, 10),
                "consent": random.choice([True, False])
            })
        return pd.DataFrame(self.health_records) # corrected variable scope