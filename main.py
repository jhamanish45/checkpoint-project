import csv



def main():
    filename= input("Enter the csv file: ")

    try:
        with open('equipment.csv','r') as file:
            reader= csv.DictReader(file)


            data=[]

            for row in reader:
                data.append(row)
                print(row['tag'],row['service'],row['design_pressure'],row['design_temperature'])

            print("Data loaded successfully") 

            # task 2
            search_tag = input("\nEnter tag to search: ")
            found = False

            for row in data:
                if row['tag']==search_tag:
                    print("\nEquipment Found:")
                    print("Tag:", row["tag"])
                    print("Service:", row["service"])
                    print("Design Pressure:", row["design_pressure"])
                    print("Design Temperature:", row["design_temperature"])

                    found =True
                    break
            if not found:
                    print("tag not found")

            # task 3jsk
            threshold = float(input("\nEnter pressure threshold: "))
            count=0

            for row in data:
                pressure = float(row["design_pressure"])

                if pressure > threshold:
                    count += 1

            print(f"\n{count} tags exceed the pressure threshold.")
                   



    except FileNotFoundError:
        print("Error: File not found")  





if __name__=="__main__":
    main()