class Patient:
    def __init__(self, name, age, gender, contact):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact
        self.selected_services = []
        self.selected_costs = []
        self.subtotal = 0
        self.gst = 0
        self.grand_total = 0
        self.discount = 0
    
    def select_services(self, service_indices, services, costs):
        self.selected_services = []
        self.selected_costs = []
        for idx in service_indices:
            if 1 <= idx <= len(services):
                service_name = services[idx-1]
                self.selected_services.append(service_name)
                self.selected_costs.append(costs[idx-1])
    
    def calculate_bill(self):
        self.subtotal = sum(self.selected_costs)
        
        original_subtotal = self.subtotal
        self.discount = 0
        
        if self.age >= 60:
            senior_discount = original_subtotal * 0.10
            self.discount += senior_discount
            self.subtotal -= senior_discount
        
        if original_subtotal > 5000:
            high_bill_discount = self.subtotal * 0.05
            self.discount += high_bill_discount
            self.subtotal -= high_bill_discount
        
        self.gst = self.subtotal * 0.18
        self.grand_total = self.subtotal + self.gst
        
        return self.subtotal, self.gst, self.grand_total, self.discount
    
    def display_invoice(self):
        print("\n" + "-" * 48)
        print("HealWell Care Hospital")
        print("Patient Invoice")
        print("-" * 48)
        print("Patient Information:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Contact: {self.contact}")
        print("\nServices Availed:")
        for i, (service, cost) in enumerate(zip(self.selected_services, self.selected_costs), 1):
            print(f"{i}. {service}: ₹{cost}")
        print(f"\nSubtotal: ₹{sum(self.selected_costs)}")
        if self.discount > 0:
            print(f"Discount Applied: ₹{self.discount:.2f}")
            print(f"Subtotal after discount: ₹{self.subtotal:.2f}")
        print(f"GST (18%): ₹{self.gst:.2f}")
        print(f"Grand Total: ₹{self.grand_total:.2f}")
        print("\nThank you for choosing HealWell Care Hospital!")
        print("-" * 48)