# --^_^-- coding:utf-8 --^_^--
# @Remark:测试登录功能

import pytest
from Common import InitializeDriver
from PageObjects.login.login_page import LoginPage
from PageObjects.home.home_page import HomePage
from TestDatas import login_datas as ld
from TestDatas import Comm_Datas as cd
import logging
import time


class TestLogin():

    @pytest.fixture(scope='function', autouse=True)
    def func_scope(self):

        # 前置：打开浏览器，登录网页
        self.driver = InitializeDriver.CustomDriver
        self.driver.get(cd.web_login_url)
        self.lp = LoginPage(self.driver)
        yield

        # 刷新一下当前页面
        self.driver.refresh()

    # 正常用例
    @pytest.mark.parametrize('data', ld.success_data)
    def test_login_2_success(self,data):
        logging.info("*********登录用例：正常场景-登录成功*********")
        # 步骤：登录页面-登录操作
        self.lp.login(data["user"], data["pwd"])
        time.sleep(3)
        # 断言：首页-LOGO这个元素存在
        assert HomePage(self.driver).check_login_ele_exists()

    # 异常用例
    @pytest.mark.parametrize('data', ld.wrong_datas)
    def test_login_1_error(self, data):
        time.sleep(2)
        logging.info("*********登录用例：异常场景-登录失败*********")
        self.lp.login(data["user"], data["pwd"])
        time.sleep(2)
        # 断言：判断提示信息是否一致
        assert data["check"] == LoginPage(self.driver).get_errorMsg()