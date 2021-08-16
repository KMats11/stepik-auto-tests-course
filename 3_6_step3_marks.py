import time
import math
from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestCorrectText():
    @pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                      'https://stepik.org/lesson/236896/step/1',
                                      'https://stepik.org/lesson/236897/step/1',
                                      'https://stepik.org/lesson/236898/step/1',
                                      'https://stepik.org/lesson/236899/step/1',
                                      'https://stepik.org/lesson/236903/step/1',
                                      'https://stepik.org/lesson/236904/step/1',
                                      'https://stepik.org/lesson/236905/step/1'])
    def test_links(self, browser, link):
        print("start test1")
        browser.implicitly_wait(3)
        browser.get(link)
        field = browser.find_element_by_xpath("//div/textarea[@placeholder='Напишите ваш ответ здесь...']")
        answer = math.log(int(time.time()))
        field.send_keys(str(answer))
        button = browser.find_element_by_css_selector("button.submit-submission")
        button.click()
        correct_text_elt = browser.find_element_by_xpath("//pre")
        correct_text = correct_text_elt.text
        assert "Correct!" == correct_text, f'wrong txt: {correct_text}'
        print("finish test1")
