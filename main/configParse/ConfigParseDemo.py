import ConfigParser
import os

#2.x语法
def get_conf(section, key):
    conf_file = ConfigParser.ConfigParser()
    conf_file.read(os.path.join(os.getcwd(), 'config.ini'))
    return conf_file.get(section, key)


print get_conf('local', 'name')
print get_conf('local', 'age')
print get_conf('local', 'address')
