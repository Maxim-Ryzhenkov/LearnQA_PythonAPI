import logging
import allure

logger = logging.getLogger(__name__)


def pytest_runtestloop(session) -> None:
    allure_logger = AllureLogger()
    if allure_logger not in logger.handlers:
        logger.info('Adding Allure logger')
        logger.addHandler(allure_logger)


    # в другом файле allure_log_handler.py (или как хотите):


class AllureLogger(logging.Handler):
    def emit(self, record):
        if logging.DEBUG < record.levelno:  # print to allure only "info" messages
            with allure.step(f'LOG ({record.levelname}): {record.getMessage()}'):
                pass  # No need for content, since the step context is doing the work.
