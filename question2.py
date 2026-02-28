flight_no ="A1203"
base_fare="4500.75"
tax_precent="5"
seat_numbers="12A,12B,14C,15D"
is_international="true"

#converting string to integer

base_fare1=int(float(base_fare))
tax_precent1=int(tax_precent)
final_fare=base_fare1+(base_fare1*tax_precent1/100)
print("Final Fareprice:",final_fare)

#converting into list

seat_values=list(seat_numbers.split())
print("The values is list format:",seat_values)

# converting to boolean
print("before converting value is:",is_international)
proper_boolean=bool(is_international)
print("Boolean value:",proper_boolean)

# creating a dictonary
seat_numbers=tuple(seat_numbers.split())
final_fare=int(float(final_fare))
flight_summary={"flightno":flight_no,"SeatNo":seat_numbers,"Final_price":final_fare}
print(flight_summary)