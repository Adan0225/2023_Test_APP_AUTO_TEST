import allure
from appium.webdriver.webdriver import By


@allure.epic('安卓計算機项目')
@allure.feature('V1.0版本')
class TestAddSub():
    @allure.story('乘法運算')
    @allure.title('[case01] 驗證計算機能否正常完成乘法功能')
    def test_cases01(self, start_app, close_app):
        with allure.step('1、啟動安卓系统中的計算机app'):
            driver = start_app
        with allure.step('2、依次按下3、*、4、='):
            driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.sky.jisuanji:id/btn3"]').click()
            driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.sky.jisuanji:id/chen"]').click()
            driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.sky.jisuanji:id/btn4"]').click()
            driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.sky.jisuanji:id/denyu"]').click()
            actual_result = driver.find_element(By.XPATH,
                                                '//android.widget.EditText[@resource-id="com.sky.jisuanji:id/text"]').text
        with allure.step('3、驗證實際结果是否正確'):
            # 断言 實際结果 == 12.0
            assert actual_result == '12.0'