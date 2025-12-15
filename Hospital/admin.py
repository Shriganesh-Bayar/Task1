services = ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]
costs = [500, 300, 800, 1500, 4000, 7000]

def display_services():
    print("Available Services:")
    for i, service in enumerate(services, 1):
        print(f"{i}. {service}: ₹{costs[i-1]}")

def get_service_cost(service_name):
    if service_name in services:
        index = services.index(service_name)
        return costs[index]
    return 0

def get_services():
    return services

def get_costs():
    return costs