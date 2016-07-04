import random
from common.test_core import BaseLiveTestCase


class RemoteControlTestCase(BaseLiveTestCase):
    def setUp(self):
        self.login_user()
        # add visit page here self.visit("/")

    def test_see_buttons(self):
        top_links = self.find_all("#user-tools a")
        top_link_texts = [a.text for a in top_links]
        top_link_texts.should.contain("Log out")
        top_link_texts.should.contain("Change password")
        top_link_texts.should.contain("View site")

    def test_refrest_add_poll(self):
        user2, browser2 = self.another_user_join_room()
        self.find(".app-polls .addlink").click()

        self.should_see_text("Add question")
        self.find("#id_question_text").send_keys('question 1')
        self.find("input[value='Save']").click()

        top_links = self.find_all(".object-tools a")
        top_link_texts = [a.text for a in top_links]
        top_link_texts.should.contain("Add question")

        self.should_see_text('The question "quest 2" was added successfully.')
        self.visit('/polls')
        self.should_see_text('question 1')
        self.browser.refresh()
        self.should_see_text('question 1')

        with self.in_browser(browser2):
            self.find(".app-polls .addlink").click()

            self.should_see_text("Add question")
            self.find("#id_question_text").send_keys('question 2')
            self.find("input[value='Save']").click()

            top_links = self.find_all(".object-tools a")
            top_link_texts = [a.text for a in top_links]
            top_link_texts.should.contain("Add question")

            self.should_see_text('The question "quest 2" was added successfully.')
            self.visit('/polls')
            self.should_see_text('question 2')
            self.browser.refresh()
            self.should_see_text('question 2')


    def another_user_join_room(self):
        browser = self.init_browser()
        user = self.init_user()
        with self.in_browser(browser):
            self.login_user(user)
            self.browser.get('/admin')
        self.until(lambda: self.should_see_text(user.first_name))
        return user, browser
