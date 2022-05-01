import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the file handler to the logger
logger.addHandler(handler)


# load the logging configuration
#logging.config.fileConfig('logging.ini')


def hello():
    logger.debug('Start Logging Hello World')

    num = 1
    for value in range(10):
        logger.info('Hello World '+ str(value))


def hello_exception():
    try:
        open('/path/to/does/not/exist', 'rb')
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception as exception:
        logger.error('Failed to open file', exc_info=True)
