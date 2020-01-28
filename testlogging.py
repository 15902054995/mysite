# import logging
# # logging.basicConfig(filename='example.log', level=logging.DEBUG)
# # logging.basicConfig(filename='example.log')
# # logging.basicConfig(filename='example.log', filemode='w')
# logging.basicConfig(filename='example.log', filemode='w',\
#     format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.warning('%s before you %s', 'Look', 'leap!')

# loglevel = 'debug'
# numeric_level = getattr(logging, loglevel.upper(), None)
# if not isinstance(numeric_level, int):
#     raise ValueError('Invalid log level: %s' % loglevel)
# print('numeric_level',numeric_level)
# logging.basicConfig(filename='example.log', level=numeric_level)

############################################### 方法一：
# import logging

# # 创建logger记录器
# logger = logging.getLogger('li_min_sheng')
# logger.setLevel(logging.DEBUG)

# # 创建一个控制台处理器，并将日志级别设置为debug。
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)

# # 创建formatter格式化器
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# # 将formatter添加到ch处理器
# ch.setFormatter(formatter)

# # 将ch添加到logger
# logger.addHandler(ch)

# # 然后就可以开始使用了！
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')

############################################### 方法二：
# import logging
# import logging.config

# logging.config.fileConfig('logging.conf') # 读取config文件

# # 创建logger记录器
# logger = logging.getLogger('li_min_sheng')

# # 使用日志功能
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')

############################################## 方法三：
import logging
import logging.config
import yaml

# 通过yaml文件配置logging
f = open("logging.conf.yaml")
dic = yaml.load(f)
f.close()
logging.config.dictConfig(dic)

# 创建logger
logger = logging.getLogger('li_min_sheng')

# 输出日志
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')