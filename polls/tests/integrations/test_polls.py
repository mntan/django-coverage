import random
from common.test_core import BaseLiveTestCase


class PollTestCase(BaseLiveTestCase):
    def setUp(self):
        self.login_user()
        # add visit page here self.visit("/")

    def test_see_buttons(self):
        top_links = self.find_all("#user-tools a")
        top_link_texts = [a.text for a in top_links]
        top_link_texts.should.contain("LOG OUT")
        top_link_texts.should.contain("CHANGE PASSWORD")
        top_link_texts.should.contain("VIEW SITE")

    def test_refresh_add_poll(self):
        user2, browser2 = self.another_user_join_room()
        self.find(".app-polls").find(".addlink").click()

        self.should_see_text("Add question")
        # self.find("#id_question_text").send_keys('question 1')
        # self.find('.datetime').find('.datetimeshortcuts').find('a[href*="javascript:DateTimeShortcuts.handleCalendarQuickLink(0, 0);"]').click()
        # self.find('.datetime').find('.datetimeshortcuts').find('a[href*="javascript:DateTimeShortcuts.handleClockQuicklink(0, -1);"]').click()
        # self.find("input[value='Save']").click()

        # top_links = self.find_all(".object-tools a")
        # top_link_texts = [a.text for a in top_links]
        # top_link_texts.should.contain("ADD QUESTION")

        # self.should_see_text('The question "question 1" was added successfully.')
        # self.visit('/polls')
        # self.should_see_text('question 1')
        # self.browser.refresh()
        # self.should_see_text('question 1')

        with self.in_browser(browser2):
            self.find(".app-polls").find(".addlink").click()

            self.should_see_text("Add question")
            # self.find("#id_question_text").send_keys('question 2')
            # self.find('.datetime').find('.datetimeshortcuts').find('a[href*="javascript:DateTimeShortcuts.handleCalendarQuickLink(0, 0);"]').click()
            # self.find('.datetime').find('.datetimeshortcuts').find('a[href*="javascript:DateTimeShortcuts.handleClockQuicklink(0, -1);"]').click()
            # self.find("input[value='Save']").click()

            # top_links = self.find_all(".object-tools a")
            # top_link_texts = [a.text for a in top_links]
            # top_link_texts.should.contain("ADD QUESTION")

            # sself.should_see_text('The question "question 2" was added successfully.')
            # self.visit('/polls')
            # self.should_see_text('question 2')
            # self.browser.refresh()
            # self.should_see_text('question 2')


    def another_user_join_room(self):
        browser = self.init_browser()
        user = self.init_user()
        with self.in_browser(browser):
            self.login_user(user)
        # remove some code
            # self.browser.get('/admin')
        # self.until(lambda: self.should_see_text(user.first_name))
        # self.should_see_text(user.first_name)
        return user, browser
