import configparser


def createConfig(path):
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "id_chat".upper(), "")
    config.set("Settings", "token".upper(), "")

    with open(path, "w") as config_file:
        config.write(config_file)


if __name__ == "__main__":
    path = "config.ini"
    createConfig(path)
