# Function to calculate hotel cost
def hotel_cost(num_nights):
    # Assuming £100 per night
    return num_nights * 100

# Function to calculate plane cost
def plane_cost(city_flight):
    # Prices for different cities
    city_prices = {
        "New York": 300,
        "London": 500,
        "Paris": 400,
        "Tokyo": 600
    }
    # Return cost based on selected city, defaulting to £0 if city not found
    return city_prices.get(city_flight, 0)

# Function to calculate car rental cost
def car_rental(rental_days):
    # Assuming £50 per day
    return rental_days * 50

# Function to calculate total holiday cost
def holiday_cost(num_nights, city_flight, rental_days):
    total_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost

# Main function to get user inputs and display holiday details
def main():
    city_flight = input("Enter the city you will be flying to (New York, London, Paris, Tokyo): ")
    num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
    rental_days = int(input("Enter the number of days for which you will be hiring a car: "))

    total_cost = holiday_cost(num_nights, city_flight, rental_days)

    print("\nHoliday Details:")
    print("City: ", city_flight)
    print("Number of Nights in Hotel: ", num_nights)
    print("Number of Days for Car Rental: ", rental_days)
    print("Total Holiday Cost: £", total_cost)

# Run the main function
if __name__ == "__main__":
    main()
