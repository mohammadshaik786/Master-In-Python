# Scope and Nested Functions

age = 24
# Global Variable
print(age)

def increase_age():
    # Local Variable
    age = 30
    def inc_age_inc(age):
        # Nested Local Variable
        age = age + 4
        print("Nestedc Method:"+str(age))
    
    inc_age_inc(age)
    inc_age_inc(50)

increase_age()
print(age)