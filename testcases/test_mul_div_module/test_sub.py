import allure
from appium.webdriver.webdriver import By


@allure.epic('安卓計算機项目')
@allure.feature('V1.0版本')
class TestAddSub():
    @allure.story('减法運算')
    @allure.title('[case01] 驗證計算機能否正常完成减法功能')
    def test_cases01(self, start_app, close_app):
        with allure.step('1、啟動安卓系统中的計算機app'):
            driver = start_app
        with allure.step('2、依次按下6、-、2、='):
            driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.sky.jisuanji:id/btn6"]').click()
            driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.sky.jisuanji:id/jian"]').click()
            driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.sky.jisuanji:id/btn2"]').click()
            driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.sky.jisuanji:id/denyu"]').click()
            actual_result = driver.find_element(By.XPATH,
                                                '//android.widget.EditText[@resource-id="com.sky.jisuanji:id/text"]').text
        with allure.step('3、驗證實際结果是否正確'):
            # 断言 实际结果 == 4.0
            assert actual_result == '4.0'