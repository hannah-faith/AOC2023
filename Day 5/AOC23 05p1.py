file_path = "Day 5/input.txt"

with open(file_path, 'r') as file:
    lines_array = [line.strip() for line in file.readlines()]

seeds = lines_array[0][lines_array[0].index(":") + 2:].split(" ")
seed_to_soil = {}
soil_to_fertilizer = {}
fertilizer_to_water = {}
water_to_light = {}
light_to_temperature = {}
temperature_to_humidity = {}
humidity_to_location = {}
locations = []

seeds_to_soil_start_index = lines_array.index("seed-to-soil map:") + 1
seeds_to_soil_end_index = lines_array.index("soil-to-fertilizer map:") - 2
soil_to_fertilizer_start_index = lines_array.index("soil-to-fertilizer map:") + 1
soil_to_fertilizer_end_index = lines_array.index("fertilizer-to-water map:") - 2
fertilizer_to_water_start_index = lines_array.index("fertilizer-to-water map:") + 1
fertilizer_to_water_end_index = lines_array.index("water-to-light map:") - 2
water_to_light_start_index = lines_array.index("water-to-light map:") + 1
water_to_light_end_index = lines_array.index("light-to-temperature map:") - 2
light_to_temperature_start_index = lines_array.index("light-to-temperature map:") + 1
light_to_temperature_end_index = lines_array.index("temperature-to-humidity map:") - 2
temperature_to_humidity_start_index = lines_array.index("temperature-to-humidity map:") + 1
temperature_to_humidity_end_index = lines_array.index("humidity-to-location map:") - 2
humidity_to_location_start_index = lines_array.index("humidity-to-location map:") + 1
humidity_to_location_end_index = len(lines_array) - 1

def dictionary_builder(dictionary, start_index, end_index):
    for i in range(start_index, end_index + 1):
        temp = lines_array[i].split(" ")
        dictionary[temp[0]] = temp[1:]

def map_builder(dictionary, map):
    for key, value in dictionary.items():
        for i in range(int(value[1])):
            map[str(int(dictionary[key][0]) + i)] = str(int(key) + i)

def mapper(dictionary, element):
    for key, value in dictionary.items():
        lower_range = int(value[0])
        upper_range = int(value[0]) + int(value[1])
        if lower_range <= element < upper_range:
            diff = element - lower_range
            return int(key) + diff
    else:
        return element


dictionary_builder(seed_to_soil, seeds_to_soil_start_index, seeds_to_soil_end_index)
dictionary_builder(soil_to_fertilizer, soil_to_fertilizer_start_index, soil_to_fertilizer_end_index)
dictionary_builder(fertilizer_to_water, fertilizer_to_water_start_index, fertilizer_to_water_end_index)
dictionary_builder(water_to_light, water_to_light_start_index, water_to_light_end_index)
dictionary_builder(light_to_temperature, light_to_temperature_start_index, light_to_temperature_end_index)
dictionary_builder(temperature_to_humidity, temperature_to_humidity_start_index, temperature_to_humidity_end_index)
dictionary_builder(humidity_to_location, humidity_to_location_start_index, humidity_to_location_end_index)

for seed in seeds:
    soil = mapper(seed_to_soil, int(seed))
    fertilizer = mapper(soil_to_fertilizer, soil)
    water =  mapper(fertilizer_to_water, fertilizer)
    light = mapper(water_to_light, water)
    temperature = mapper(light_to_temperature, light)
    humidity = mapper(temperature_to_humidity, temperature)
    location = mapper(humidity_to_location, humidity)

    locations.append(int(location))

locations.sort()
print(locations[0])
