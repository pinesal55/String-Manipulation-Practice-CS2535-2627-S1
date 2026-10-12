name = "   aLeX mOrGaN   "
clean_name = name.strip().title()
print(clean_name)

status = "WARNING::ENGINE_OVERHEAT::SECTOR_7"
clean_status = status.lower()
clean_status = clean_status.replace("::", " | ").replace("_", " ")
print(clean_status)

modules = "navigation|life_support|cargo_bay|engine_control"
module_list = modules.split("|")
clean_modules = []
for module in module_list:
    clean_module = module.replace("_", " ").title()
    clean_modules.append(clean_module)
finished_modules = ", ".join(clean_modules)
print(finished_modules)

readings = "  18,27,35,20  "
reading_list = readings.strip().split(",")
numbers = []
for reading in reading_list:
    number = int(reading)
    numbers.append(number)
total = sum(numbers)
average = total / len(numbers)
print(f"Total: {total}")
print(f"Average: {average}")