
###############          ##########        #######   #######        #########      #######       #
#              #        #          #             #         #       #         #           #
#               #       #          #            #         #        #         #          #        #
#              #        #          #           #         #         #         #         #         #
###############         ############          #         #          ###########        #          #
#              #        #          #         #         #           #         #       #           #
#               #       #          #        #         #            #         #      #            #
#              #        #          #       #         #             #         #     #             #
###############         #          #      #######    #######       #         #    #######        #

# Developer: Mohammad Ali Bazzazi (me)
print("*********************************************************************************")
print("*"+" "*79+"*")
print("*  Copyright of Mohammad Ali Bazzazi, 2021 ©                                    *")
print("*"+" "*79+"*")
print("*  https://www.youtube.com/channel/UCeLKoNs3c72Vc-OG3uNQxGw?sub_confirmation=1  *")
print("*"+" "*79+"*")
print("*********************************************************************************")

########################### START ###########################

from selenium import webdriver
import info, time, pyautogui

class Unfollowers:
    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver')
    
    def login(self, Username, Password):
        self.driver.get('https://www.aparat.com/signin?callbackType=postmessage')
        time.sleep(5)
        
        self.driver.find_element_by_xpath("""//*[@id="username"]""").send_keys(Username)
        self.driver.find_element_by_xpath("""//*[@id="main-container"]/section/div/div[2]/form/button""").click()
        time.sleep(3)
        
        self.driver.find_element_by_xpath("""//*[@id="password"]""").send_keys(Password)
        self.driver.find_element_by_xpath("""//*[@id="main-container"]/section/div/div[1]/form/button""").click()
        time.sleep(5)
        
        self.driver.get('https://www.aparat.com/followed')

    def getFollower(self):
        FollowerList = []
        self.driver.get("https://www.aparat.com/user/follow/follower")
        while 1:
            self.scroll()
            response = input("End page? ")
            if response == "Y":
                break
        count = len(self.driver.find_elements_by_css_selector("""#grid1 > div"""))
        for i in range(1,count + 1):
            FollowerList.append(self.driver.find_element_by_xpath(f"""//*[@id="grid1"]/div[{i}]/div/div/div/div[2]/h2/a""").get_attribute("href"))
        return FollowerList

    def getFollowing(self):
        FollowingList = []
        self.driver.get("https://www.aparat.com/user/follow/followed")
        while 1:
            self.scroll()
            response = input("End page? ")
            if response == "Y":
                break
        count = len(self.driver.find_elements_by_css_selector("""#grid1 > div"""))
        for i in range(1,count + 1):
            FollowingList.append(self.driver.find_element_by_xpath(f"""//*[@id="grid1"]/div[{i}]/div/div/div/div[2]/h2/a""").get_attribute("href"))
        return FollowingList

    def Unfollow(self, link):
        self.driver.get(link)
        self.driver.find_element_by_xpath("""//*[@id="container"]/div/div/header/section[2]/div/div/div[1]/button""").click()

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


bot = Unfollowers()
bot.login(info.Email, info.PASSWORD)

Followers = bot.getFollower()
Following = bot.getFollowing()
for channel in Following:
    if channel not in Followers:
        bot.Unfollow(channel)

########################### END ###########################
