def main():
    speed = 50
    print("Calculate Trip Duration\n")
    start = str(input("\tEnter the starting location: "))
    end = str(input("\tEnter the ending location: "))
    distance = float(input("\tEnter the distance between the locations: "))
    duration = distance / speed
    print(f"\nDetails")
    print(f"\tStart:\t\t{start}")
    print(f"\tEnd:\t\t{end}")
    print(f"\tDistance:\t{distance} km")
    print(f"\tDuration:\t{duration} hours")

if __name__ == "__main__":
    main()

