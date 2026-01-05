from admin import display_services, get_services, get_costs
from patient import Patient

def get_patient_details():
    print("\n" + "=" * 48)
    print("HEALWELL CARE HOSPITAL - PATIENT REGISTRATION")
    print("=" * 48)
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    contact = input("Contact : ")
    return name, age, gender, contact

def get_service_selection(services):
    print("\n" + "-" * 48)
    display_services()
    print("-" * 48)
    
    while True:
        try:
            selection = input("\nEnter service numbers (comma separated): ")
            indices = [int(idx.strip()) for idx in selection.split(",")]
            
            valid = all(1 <= idx <= len(services) for idx in indices)
            if valid and indices:
                return indices
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter valid numbers separated by commas.")

def main():
    print("=" * 48)
    print("WELCOME TO HEALWELL CARE HOSPITAL")
    print("=" * 48)
    
    services = get_services()
    costs = get_costs()
    
    name, age, gender, contact = get_patient_details()
    patient = Patient(name, age, gender, contact)
    
    selected_indices = get_service_selection(services)
    patient.select_services(selected_indices, services, costs)
    
    print(f"\nSelected Services: {patient.selected_services}")
    print(f"Selected Costs: {patient.selected_costs}")
    
    subtotal, gst, grand_total, discount = patient.calculate_bill()
    
    print(f"\nTotal Cost (Before Tax): ₹{sum(patient.selected_costs)}")
    if discount > 0:
        print(f"Discount: ₹{discount:.2f}")
    print(f"Subtotal after discount: ₹{subtotal:.2f}")
    print(f"GST (18%): ₹{gst:.2f}")
    print(f"Grand Total: ₹{grand_total:.2f}")
    
    patient.display_invoice()

if __name__ == "__main__":
    main()