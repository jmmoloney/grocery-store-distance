from configparser import ConfigParser, ExtendedInterpolation
import os

config_parser = ConfigParser(interpolation=ExtendedInterpolation())

try:
	config_path = os.environ['config']
	config_parser.read(config_path)
except KeyError:
	path = os.path.split(__file__)[0]
	print("No Environment var `config` path set.\n"
	      "Trying to read from {}".format(path))
	config_parser.read(os.path.join(path, "config.cfg"))


class Config:
	"Load main configuration file"
	def __init__(self):
		self.config = config_parser


if __name__ == '__main__':
	config = Config()
