import config

config_reader = config.IniReader().get_section_data("database")
print(config_reader["host"])
