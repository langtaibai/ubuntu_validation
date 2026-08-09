from uvf.logger.logger import get_logger

logger = get_logger()

logger.debug('debug message')
logger.info('ssh connection info')
logger.warning('system degraded')
logger.error('test failed')