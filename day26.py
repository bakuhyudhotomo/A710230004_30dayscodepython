class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

# Example usage
contact1 = Contact("Bakuh yudho", "087848899380", "bakuh@gmail.com")
print(contact1)  # Output: Name: Bakuh yudho, Phone: 087848899380, Email: bakuh@gmail.com