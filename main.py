from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, height=600, width=650)
canvas.pack()

label1 = tk.Label(root, text="Enter Pin: ")
canvas.create_window(325, 50, window=label1)

gamePinEntry = tk.Entry(root)
canvas.create_window(325, 75, window=gamePinEntry)

label2 = tk.Label(root, text="Enter Bot Name: ")
canvas.create_window(325, 100, window=label2)
botNameEntry = tk.Entry(root)
canvas.create_window(325, 125, window=botNameEntry)

label3 = tk.Label(root, text="Enter Bot Amount: ")
canvas.create_window(325, 150, window=label3)
botAmountEntry = tk.Entry(root)
canvas.create_window(325, 175, window=botAmountEntry)


def runBot():
    a = 0
    botNumber = 0
    gamePin = str(gamePinEntry.get())
    botName = str(botNameEntry.get())
    botAmount = int(botAmountEntry.get())

    while a < botAmount:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        a += 1
        botNumber += 1
        botNamer = f"{botName}{botNumber}"
        browser.get("https://kahoot.it")
        browser.find_element_by_id("game-input").send_keys(gamePin)
        browser.find_element_by_id("game-input").send_keys(Keys.RETURN)

        time.sleep(1)
        try:
            browser.find_element_by_id("nickname").send_keys(botNamer)
            browser.find_element_by_id("nickname").send_keys(Keys.RETURN)

        except:
            browser.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div[2]/button').click()
            time.sleep(3)
            browser.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div[2]/button[2]').click()


submit = tk.Button(root, text="Submit", command=runBot)
canvas.create_window(325, 205, window=submit)

root.mainloop()
