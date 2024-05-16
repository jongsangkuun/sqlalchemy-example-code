import configparser
import os


class IniReader:
    def __init__(self, filename="config.ini"):
        self.config = configparser.ConfigParser()

        current_dir = os.path.abspath(os.path.dirname(__file__))
        root_dir = os.path.abspath(
            os.path.join(current_dir, os.pardir)
        )  # 프로젝트 root 경로

        filepath = os.path.join(root_dir, filename)
        print("Read config.ini ::: " + filepath)
        self.config.read(filepath)

    def get_section_data(self, section):
        if self.config.has_section(section):
            return dict(self.config.items(section))
        else:
            return "Section not found in config file"
