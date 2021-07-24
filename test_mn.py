# coding=utf-8
import logging

import yaml
from calculator.calculator import Calculator
import pytest

def getData():
    with open("./tmp/data.yml") as f:
        data = yaml.safe_load(f)
        # print(data["ids_cheng"])
    return data

class TestCalculator():

    def setup_class(cls):
        cls.calc = Calculator()
        logging.info("计算开始......")
        print("\n---class setup...")

    def teardown_class(cls):
        logging.info("结束计算........")
        print("\ntearDown class")

    def setup(self):
        # self.calc = Calculator()
        print("\nfunciton setup ---\n")

    def tearDown(self):
        print("\nfunction tearDown...\n")

    @pytest.mark.parametrize("a,b,expect",getData()["add"],ids=getData()["ids_add"])
    @pytest.mark.add
    def test_add(self,a,b,expect):
        assert expect == self.calc.add(a,b)

    @pytest.mark.minus
    @pytest.mark.parametrize("a,b,expect",getData()["minus"],ids=getData()["ids_add"])
    def test_minus(self,a,b,expect):
        assert self.calc.minus(a,b) == expect

    @pytest.mark.cheng
    @pytest.mark.parametrize("a,b,expect",getData()["cheng"],ids=getData()["ids_cheng"])
    def test_cheng(self,a,b,expect):
        if isinstance(self.calc.cheng(a,b),float):
            assert round(self.calc.cheng(a,b),4) == expect #round()给浮点数进行截断
        else:
            assert self.calc.cheng(a,b) == expect

    @pytest.mark.parametrize("a,b,expect",getData()["div"],ids=getData()["ids_div"])
    def test_div(self,a,b,expect):
        assert self.calc.div(a,b) == expect


if __name__ == "__main__":
    pytest.main()