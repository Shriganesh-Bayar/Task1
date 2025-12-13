
def calculate_sales(area1, yield1, area, cost, area2 = 0, yield2 = 0):
    A1 = area * area1
    A2 = area * area2
    # total_crop = area * yield in that area
    total_crop = A1 * yield1 + A2 * yield2
    total_crop_in_kg = total_crop * 1000
    total_yield = total_crop_in_kg * cost
    return round(total_yield, 2)

if __name__ == "__main__":
    # given total land = 80 acre
    total_land = 80

    # it has 5 segments, and it's respective crops
    area = 80 // 5

    print("Question a:")

    '''
        Tomato:
        30% -> 10 tonne/acre
        70% -> 12 tonne/acre
        cost -> 7 rupees/kg
    '''
    tomato_area1 = 0.3
    tomato_area2 = 0.7
    tomato_yield1 = 10
    tomato_yield2 = 12
    tomato_cost = 7

    tomato_sale = calculate_sales(tomato_area1, tomato_yield1, area, tomato_cost, tomato_area2, tomato_yield2)
    print("Tomato yield: ", tomato_sale)

    '''
        Potato:
        100% -> 10 tonne/acre
        cost -> 20 rupeees/kg
    '''
    potato_area = 1
    potato_yield = 10
    potato_cost = 20
    potato_sale = calculate_sales(potato_area, potato_yield, area, potato_cost)
    print("Potato yield:", potato_sale)

    '''
        Cabbage:
        100% -> 14 tonne/acre
        cost -> 24 rupees/kd
    '''
    cabbage_area = 1
    cabbage_yield = 14
    cabbage_cost = 24
    cabbage_sale = calculate_sales(cabbage_area, cabbage_yield, area, cabbage_cost)
    print("Cabbage yield:", cabbage_sale)

    '''
        Sunflower:
        100% -> 0.7 tonne/acre
        cost -> 200 rupees/kg
    '''
    sunflower_area = 1
    sunflower_yield = 0.7
    sunflower_cost = 200
    sunflower_sale = calculate_sales(sunflower_area, sunflower_yield, area, sunflower_cost)
    print("Sunflower yield:", sunflower_sale)

    '''
        Sugarcane:
        100% -> 45 tonne/acre
        cost -> 4000 rupees/tonne => 4 rupees/kg
    '''
    sugarcane_area = 1
    sugarcane_yield = 45
    sugarcane_per_tonne = 4000
    sugarcane_per_kg = sugarcane_per_tonne / 1000
    sugarcane_sale = calculate_sales(sugarcane_area, sugarcane_yield, area, sugarcane_per_kg)
    print("Sugarcane yield:", sugarcane_sale)

    total_sale = tomato_sale + potato_sale + cabbage_sale + sunflower_sale + sugarcane_sale
    print("Total yield in 80 acre of land is:", total_sale)

    '''
        Chemical free sales,
        6 months -> tomato, potato, cabbage
        4 months -> sunflower
        4 months -> sugarcane

        => sugarcane need 14 months, rest of the chemical free crops can be sold by 11 months
    '''

    print("\nQuestion b:")
    total_sale_chemical_free = total_sale - sugarcane_sale
    print("Total yield in chemical free sale is:", total_sale_chemical_free)
