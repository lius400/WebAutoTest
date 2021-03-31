# --^_^-- coding:utf-8 --^_^--
import time
import pytest,logging
from Common import InitializeDriver

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

@pytest.fixture(scope='function', autouse=True)
def func_scope():

    print('\n Function Fixture start!')
    yield
    print('\n Function Fixture end!')


@pytest.fixture(scope='module', autouse=True)
def mod_scope():
    start = time.time()
    print('\n Module Fixture start: {}'.format(time.strftime(DATE_FORMAT,time.localtime(start))))
    yield
    start = time.time()
    print('\n Module Fixture end: {}'.format(time.strftime(DATE_FORMAT, time.localtime(start))))


@pytest.fixture(scope='session', autouse=True)
def sess_scope():

    print("\n Session Fixture start!")
    yield
    logging.info("退出webdriver实例，关闭浏览器")
    driver = InitializeDriver.CustomDriver
    driver.quit()
    print("\n Session Fixture end!")


@pytest.fixture(scope='class', autouse=True)
def class_scope():
    print("\n Class Fixture start!")
    yield
    print("\n Class Fixture end!")