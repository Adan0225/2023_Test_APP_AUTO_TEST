import allure
from appium.webdriver.webdriver import By


@allure.epic('安卓計算機目')
@allure.feature('V1.0版本')
class TestAddSub():
    @allure.story('加法運算')
    @allure.title('[case01] 驗證計算機能否正常完成加法功能')
    # @pytest.mark.add_basic
    def test_cases01(self, start_app, close_app):
        with allure.step('1、啟動安卓系统中的計算機app'):
            driver = start_app
        with allure.step('2、依次按下9、+、8、='):
            driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.android.calculator2:id/digit_9"]').click()
            driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.android.calculator2:id/op_add"]').click()
            driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.android.calculator2:id/digit_8"]').click()
            driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.android.calculator2:id/eq"]').click()
            actual_result = driver.find_element(By.XPATH,
                                                '//android.widget.EditText[@resource-id="com.android.calculator2:id/formula"]').text
        with allure.step('3、驗證實際结果是否正確'):
            # 断言 實際结果 == 17.0
            assert actual_result == '17.0'