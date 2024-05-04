import pandas as pd
import matplotlib.pyplot as plt
import io

# Data 
data = """
Manufacturer,Model,Type,Min.Price,Price,Max.Price,MPG.city,MPG.highway,AirBags,DriveTrain,Cylinders,EngineSize,Horsepower,RPM,Rev.per.mile,Man.trans.avail,Fuel.tank.capacity,Passengers,Length,Wheelbase,Width,Turn.circle,Rear.seat.room,Luggage.room,Weight,Origin,Make
Acura,Integra,Small,12.9,15.9,18.8,25,31,None,Front,4,1.8,140,6300,2890,Yes,13.2,5,177,102,68,37,26.5,11,2705,non-USA,Acura Integra
Acura,Legend,Midsize,29.2,33.9,38.7,18,25,Driver & Passenger,Front,6,3.2,200,5500,2335,Yes,18,5,195,115,71,38,30,15,3560,non-USA,Acura Legend
Audi,90,Compact,25.9,29.1,32.3,20,26,Driver only,Front,6,2.8,172,5500,2280,Yes,16.9,5,180,102,67,37,28,14,3375,non-USA,Audi 90
Audi,100,Midsize,30.8,37.7,44.6,19,26,Driver & Passenger,Front,6,2.8,172,5500,2535,Yes,21.1,6,193,106,70,37,31,17,3405,non-USA,Audi 100
BMW,535i,Midsize,23.7,30,36.2,22,30,Driver only,Rear,4,3.5,208,5700,2545,Yes,21.1,4,186,109,69,39,27,13,3640,non-USA,BMW 535i
Buick,Century,Midsize,14.2,15.7,17.3,22,31,Driver only,Front,4,2.2,110,5200,2565,No,16.4,6,189,105,69,41,28,16,2880,USA,Buick Century
Buick,LeSabre,Large,19.9,20.8,21.7,19,28,Driver only,Front,6,3.8,170,4800,1570,No,18,6,200,111,74,42,30.5,17,3470,USA,Buick LeSabre
Buick,Roadmaster,Large,22.6,23.7,24.9,16,25,Driver only,Rear,6,5.7,180,4000,1320,No,23,6,216,116,78,45,30.5,21,4105,USA,Buick Roadmaster
Buick,Riviera,Midsize,26.3,26.3,26.3,19,27,Driver only,Front,6,3.8,170,4800,1690,No,18.8,5,198,108,73,41,26.5,14,3495,USA,Buick Riviera
"""

# Convert data to DataFrame 
df = pd.read_csv(io.StringIO(data))

# Barplot for mean horsepower
car_types = df['Type'].unique()
mean_horsepower = [df[df['Type'] == car_type]['Horsepower'].mean() for car_type in car_types]

plt.figure(figsize=(10, 6))
plt.bar(car_types, mean_horsepower, color='lightgreen')
plt.title('Mean Horsepower for Each Car Type')
plt.xlabel('Car Type')
plt.ylabel('Mean Horsepower')
plt.show()
