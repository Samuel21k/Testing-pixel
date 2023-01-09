from seleniumbase import BaseCase


class HomeTest(BaseCase):

        def test_home_page(self):
            #open home page
            self.open("https://www.pixel.bet")
            self.click('a:contains("Register")')

            #registering
            self.type('#email', "hellohello@byebye.com")
            self.type('#password', "Mypass123")
            self.click('button[type="submit"]')

            self.type('#city', "Thisismmycity")
            self.type('#street', "Thisismmyaddress")
            self.type('#postCode', 'AAA 123')
            self.click('button[type="submit"]')

            self.type('#firstName', "Dio")
            self.type('#lastName', "Brando")
            self.type('input[type="tel"]', '06011989')
            self.click('button[type="submit"]')


            self.click('.react-toggle-track-check')
            self.click("//*[@id=\"modalBody\"]/div/div/form/div[2]/div/div/div[1]/div/div[2]")
            self.click('button[type="submit"]')



            self.type('#phone', 9110189)
            self.click('button[type="submit"]')
            self.click('.close')

        def test_setting_limits(self):
            # open home page
            self.open("https://www.pixel.bet")
            self.click('a:contains("Login")')

            #logging in
            self.type('#email', "hellohello@byebye.com")
            self.type('#password', "Mypass123")
            self.click('button[type="submit"]')


            self.click('#nav-menu-icon')
            self.click('a[href*="limits"]')
            self.click(".btn-cta.cta-blue-gradiant.btn-addlimit")
            self.click(".btn-purple-border-box.limits-deposit-btn")
            self.click("#modalBody > div > div > div.nav-buttons-holder > span.btn-cta.cta-blue-gradiant")
            self.click('//*[@id="modalBody"]/div/div/div[1]/span[1]')
            self.click("#modalBody > div > div > div.nav-buttons-holder > span.btn-cta.cta-blue-gradiant")
            self.type('#amount', '5000')
            self.wait(5)
            #self.click("#modalBody > div > div > form > div.nav-buttons-holder > div > button")

        def test_self_exclusion(self):
            # open home page
            self.open("https://www.pixel.bet")
            self.click('a:contains("Login")')

            # logging in
            self.type('#email', "hellohello@byebye.com")
            self.type('#password', "Mypass123")
            self.click('button[type="submit"]')

            #SE
            self.click('#nav-menu-icon')
            self.click('a[href*="limits"]')
            self.click("#pixelContent > div.modal-style-holder > div > div > div.modal-style-content > div > div > "
                      "div.limit-row-container.self-exclusion-section > div > div")
            self.click(".Select-placeholder")
            self.click_nth_visible_element(".Select-menu-outer", {2})
            #self.click(".Select-menu-outer")
            self.wait(5)
            #self.click("#modalBody > div > div > form > div.nav-buttons-holder > div > button")

        def test_search(self):
            self.open("https://www.pixel.bet")
            self.click('a:contains("Login")')

            # logging in
            self.type('#email', "hellohello@byebye.com")
            self.type('#password', "Mypass123")
            self.click('button[type="submit"]')

            self.click('a[href*="casino"]')
            self.type('#search-box', "mad cars")
            self.click('document.querySelector("#SearchResults > li:nth-child(1) > div:nth-child(1) > div.card-image-container > div.thumbnail-overlay")')
            self.click("#pixelContent > div.container-fluid > div > div > div.game-page-container > div.game-image-details > div.game-details > div.game-btns > div.try-game.btn-purple-box")








