# creating class flight
class flight:
    def __init__(self,flight_no,source,destination,base_fare):
        self.flight_no=flight_no
        self.source=source
        self.destination=destination
        self.base_fare=base_fare

#Flight Info Printing
    def get_flight_info(self):
        print(f"The Flight Deatils \n ------------- \n flightNo:{self.flight_no} \n Source:{self.source} \n Destination:{self.destination}")

#Calculating price

    def calculateprice(self,passenger_count,discount=0):
        total_fare=(self.base_fare * passenger_count)-discount
        print("Totalfare:",total_fare)

# update source and destination
    def update_method(self,new_source,new_destination=None):
        if  new_destination is None:
            self.destination=new_source
        else:
            self.source=new_source
            self.destination=new_destination
        print(f"Updated Deatils:\n Source:{self.source}\n Destination:{self.destination}")
    
#object creation
domestic=flight("AB405","Bangalore","Delhi",10000)
domestic.get_flight_info()
domestic.calculateprice(200)
domestic.calculateprice(200,1200)
domestic.update_method("bombay")
domestic.update_method("bombay","Kochi")


