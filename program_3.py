def main():
    all_entered_values = []
    num_entries = int(input("How many state records would you like to enter: "))
    for i in range(num_entries):
        print(f"Entry # {i+1}")
        year = int(input("Enter year: "))
        name_of_state = input("Enter state name: ")
        population = int(input("Enter population: "))

        all_entered_values.append([year,name_of_state,population])

    year_to_sum = int(input("Enter year to sum the total population: "))
    sum_population_for_year(all_entered_values,year_to_sum)

def sum_population_for_year(all_entered_values, year_to_sum):
    total_population = 0

    for record in all_entered_values:
        year = record[0]
        population = record[2]

        if year == year_to_sum:
            total_population += population

    print(f"Total population for {year_to_sum}: {total_population:,}")

if __name__ == '__main__':
    main()