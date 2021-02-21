import os
import random
import string
import time
import numpy
import pyautogui
import img_hash
import csv
from collections import namedtuple

class BSReroll:
    del_pos1 = (145, 279)
    del_pos2 = (127, 75)
    del_pos3 = (310, 140)
    del_pos4 = (85, 220)
    del_pos5 = (575, 75)
    del_pos6 = (30, 140)
    del_pos7 = (310, 140)
    del_pos8 = (85, 140)
    del_pos9 = (310, 370)
    del_pos10 = (400, 290)
    close_tab = (315, 10)

    icon_pos = (243, 278)
    cls_mod_hash = "1111111111111111100000011000000110000001111111111111111111111111"
    black_hash = "0000000000000000000000000000000000000000000000000000000000000000"
    loading_hash = "0000000000000000000000001000000010111111111111111111111100000000"
    input_nick_hash = "0000000000000000000001100000011100000111000001110000000000000000"
    next_btn_hash = "1111111100000000001000000011110000011100000111000000000000000000"
    confirm_btn_hash = "1111111100000000010010010111111001111110011111110000000000000000"
    summon_back_hash = "1111111100000000000000000011100000111100000110000000000000000000"
    skip_ad = (18, 69)
    cls_ad = (596, 65)
    cls_mod_reg = (375, 239, 38, 20)
    tos_box1 = (173, 239)
    tos_box2 = (173, 257)
    ok_btn = (310, 310)
    skip_btn = (585, 60)
    input_nick_reg = (212, 224, 75, 21)
    next_btn_reg = (276, 325, 71, 29)
    confirm_btn_reg = (277, 326, 71, 26)
    box_btn = (35, 155)
    receive_btn = (525, 100)
    menu_btn = (600, 60)
    menu_summon_btn = (425, 345)
    summon_1_btn = (90, 120)
    summon_2_btn = (90, 175)
    summon_3_btn = (90, 230)
    summon_4_btn = (90, 285)
    summon_5_btn = (90, 320)
    summon_banner = (565, 325)
    summon_skip = (595, 90)
    summon_back_reg = (221, 319, 76, 30)
    summon_list: list
    Summon = namedtuple("Summon", ["hash_", "name", "summon_type", "star", "score"])

    def load_summon_list(self):
        if os.path.exists("Bluestacks/summon_list.csv"):
            with open("Bluestacks/summon_list.csv", "r") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=";")
                list_ = []
                row = 0
                for hash_, name, summon_type, star, score in csv_reader:
                    if row != 0:
                        list_ += [self.Summon(hash_, name, summon_type, int(star), int(score))]
                    row += 1
                self.summon_list = list_
        else:
            if not os.path.exists("Bluestacks/"):
                os.mkdir("Bluestacks/")
            with open("Bluestacks/summon_list.csv", "w", newline='') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=";")
                csv_writer.writerow([
                    "Hash",
                    "Name",
                    "Type",
                    "Star",
                    "Weight"
                ])
            print("summon_list.csv not found, populate the created csv first")
            exit(0)

    def __init__(self):
        self.load_summon_list()

    def _is_tutorial(self):
        ss = pyautogui.screenshot(region=self.next_btn_reg)
        ss = img_hash.calc_image_hash(numpy.array(ss)[:, :, ::-1])
        return True if img_hash.comp_hash(ss, self.next_btn_hash) < 2 else False

    def _wait_loading(self, emulator_position=0, lag_check=True):
        loading_reg = (543 if emulator_position == 0 else 1226, 341, 48, 29)
        screen_reg = (0, 0, 665, 390)
        loading = True
        last_screen_hash = None
        while loading:
            time.sleep(2.5)
            loading_ss = pyautogui.screenshot(region=loading_reg)
            # PIL Menggunakan ARGB Sedangkan OpenCv Menggunakan BGRA
            loading_ss = img_hash.calc_image_hash(numpy.array(loading_ss)[:, :, ::-1])
            # Margin of errornya cuma 2 walaupun harusnya 1
            if img_hash.comp_hash(loading_ss, self.loading_hash) > 2:
                if lag_check:
                    screen_ss = pyautogui.screenshot(region=screen_reg)
                    screen_ss = img_hash.calc_image_hash(numpy.array(screen_ss)[:, :, ::-1])
                    if last_screen_hash:
                        if img_hash.comp_hash(last_screen_hash, screen_ss) > 0:
                            loading = False
                            time.sleep(4)
                    last_screen_hash = screen_ss
                else:
                    loading = False
                    time.sleep(4)

    def _del_config(self):

        time.sleep(2)
        pyautogui.click(self.del_pos1)
        time.sleep(15)
        pyautogui.click(self.del_pos2)
        time.sleep(3)
        pyautogui.click(self.del_pos3)
        time.sleep(3)
        pyautogui.click(self.del_pos4)
        time.sleep(2)
        pyautogui.click(self.del_pos5)
        time.sleep(2)
        pyautogui.write("com.overlord", interval=0.5)
        time.sleep(2)
        pyautogui.click(self.del_pos6)
        time.sleep(2)
        pyautogui.click(self.del_pos7)
        time.sleep(2)
        pyautogui.mouseDown(self.del_pos8, duration=1)
        time.sleep(3)
        pyautogui.mouseUp()
        time.sleep(2)
        pyautogui.click(self.del_pos9)
        time.sleep(2)
        pyautogui.click(self.del_pos10)
        time.sleep(2)
        pyautogui.moveTo(self.close_tab)
        time.sleep(1)
        pyautogui.click()

    def identify_summon(self, img):
        hash_ = img_hash.calc_image_hash(img)
        for i in self.summon_list:
            if img_hash.comp_hash(i.hash_, hash_) < 3:
                return i

    def acc_reroll(self, times: int, banner_to_summon: list, is_modded: bool):
        for x in range(times):
            summoned_list: list = []
            summoned_folder: list = []
            self._del_config()
            time.sleep(2)
            pyautogui.click(self.icon_pos)

            if is_modded:
                i = 0
                while i <= 15:
                    time.sleep(2)
                    ss = pyautogui.screenshot(region=self.cls_mod_reg)
                    ss = img_hash.calc_image_hash(numpy.array(ss)[:, :, ::-1])
                    if img_hash.comp_hash(ss, self.black_hash) < 2:
                        continue
                    elif img_hash.comp_hash(ss, self.cls_mod_hash) < 2:
                        i += 1
                    else:
                        time.sleep(7)
                        pyautogui.click(self.skip_ad)
                        time.sleep(1.5)
                        pyautogui.click(self.cls_ad)
                pyautogui.click(self.cls_mod_reg)
            else:
                while True:
                    time.sleep(2)
                    ss = pyautogui.screenshot(region=self.cls_mod_reg)
                    ss = img_hash.calc_image_hash(numpy.array(ss)[:, :, ::-1])
                    if img_hash.comp_hash(ss, self.black_hash) > 2:
                        pyautogui.click(self.ok_btn)
                        break

            time.sleep(3)
            pyautogui.click(self.ok_btn)

            self._wait_loading(lag_check=False)
            pyautogui.click(self.tos_box1)
            time.sleep(2)
            pyautogui.click(self.tos_box2)
            time.sleep(2)
            pyautogui.click(self.ok_btn)

            self._wait_loading()
            self._wait_loading(lag_check=False)

            pyautogui.click(self.ok_btn)
            time.sleep(6)
            pyautogui.click(self.skip_btn)
            time.sleep(3)
            pyautogui.click(self.ok_btn)
            time.sleep(10)
            pyautogui.click(self.ok_btn)

            while True:
                time.sleep(2)
                ss = pyautogui.screenshot(region=self.input_nick_reg)
                ss = img_hash.calc_image_hash(numpy.array(ss)[:, :, ::-1])
                if img_hash.comp_hash(ss, self.input_nick_hash) < 2:
                    time.sleep(2)
                    break

            pyautogui.click(self.input_nick_reg)
            time.sleep(4)
            pyautogui.write("Reroll", interval=0.6)
            pyautogui.doubleClick(self.ok_btn, interval=2)
            pyautogui.moveTo(5, 5)
            time.sleep(10)
            while True:
                time.sleep(2)
                if self._is_tutorial():
                    time.sleep(4)
                    pyautogui.click(self.next_btn_reg, interval=2, clicks=4)
                    break

            i = 0
            while i < 2:
                pyautogui.moveTo(5, 5)
                time.sleep(3)
                ss = pyautogui.screenshot(region=self.confirm_btn_reg)
                ss = img_hash.calc_image_hash(numpy.array(ss)[:, :, ::-1])
                if img_hash.comp_hash(ss, self.confirm_btn_hash) < 2:
                    pyautogui.click(self.confirm_btn_reg)
                    time.sleep(8)
                    if i == 1:
                        self._wait_loading()
                    i += 1
                elif i == 1:
                    time.sleep(2)
                    break
                else:
                    pyautogui.click(self.ok_btn)

            pyautogui.click(self.box_btn)
            self._wait_loading(lag_check=False)
            pyautogui.click(self.receive_btn)
            self._wait_loading(lag_check=False)
            pyautogui.click(self.ok_btn)
            self._wait_loading(lag_check=False)
            pyautogui.click(self.menu_btn)
            time.sleep(2)
            pyautogui.click(self.menu_summon_btn)
            self._wait_loading()

            for i in banner_to_summon:
                pyautogui.mouseDown(90, 300)
                pyautogui.moveTo(90, 190, duration=3)
                pyautogui.mouseUp()
                time.sleep(2)
                if i == 1:
                    pyautogui.click(self.summon_1_btn)
                elif i == 2:
                    pyautogui.click(self.summon_2_btn)
                elif i == 3:
                    pyautogui.click(self.summon_3_btn)
                elif i == 4:
                    pyautogui.click(self.summon_4_btn)
                elif i == 5:
                    pyautogui.click(self.summon_5_btn)
                elif i == 6:
                    pyautogui.mouseDown(90, 300)
                    pyautogui.moveTo(90, 90, duration=1)
                    pyautogui.mouseUp()
                    time.sleep(3)
                    pyautogui.click(self.summon_1_btn)
                elif i == 7:
                    pyautogui.mouseDown(90, 300)
                    pyautogui.moveTo(90, 90, duration=1)
                    pyautogui.mouseUp()
                    time.sleep(3)
                    pyautogui.click(self.summon_2_btn)
                elif i == 8:
                    pyautogui.mouseDown(90, 300)
                    pyautogui.moveTo(90, 90, duration=1)
                    pyautogui.mouseUp()
                    time.sleep(3)
                    pyautogui.click(self.summon_3_btn)
                elif i == 9:
                    pyautogui.mouseDown(90, 300)
                    pyautogui.moveTo(90, 90, duration=1)
                    pyautogui.mouseUp()
                    time.sleep(3)
                    pyautogui.click(self.summon_4_btn)
                elif i == 10:
                    pyautogui.mouseDown(90, 300)
                    pyautogui.moveTo(90, 90, duration=1)
                    pyautogui.mouseUp()
                    time.sleep(3)
                    pyautogui.click(self.summon_5_btn)
                else:
                    return False
                time.sleep(2)
                pyautogui.click(self.summon_banner)
                time.sleep(3)
                pyautogui.click(self.ok_btn)
                self._wait_loading(lag_check=False)
                pyautogui.doubleClick(self.skip_btn, interval=2)
                while True:
                    time.sleep(2)
                    ss = pyautogui.screenshot(region=self.summon_back_reg)
                    ss = img_hash.calc_image_hash(numpy.array(ss)[:, :, ::-1])
                    if self._is_tutorial():
                        time.sleep(2)
                        pyautogui.click(self.next_btn_reg, interval=2, clicks=3)
                        time.sleep(5)
                    elif img_hash.comp_hash(ss, self.summon_back_hash) < 2:
                        folder_name = "Bluestacks/Result/" + \
                                      ''.join(random.choice(string.ascii_letters) for _ in range(10))
                        os.mkdir(f"{folder_name}")
                        pyautogui.screenshot("{}/ori.png".format(folder_name))
                        summon_reg = ((51, 118, 40, 40),
                                      (167, 118, 40, 40),
                                      (283, 118, 40, 40),
                                      (400, 118, 40, 40),
                                      (516, 118, 40, 40),
                                      (51, 226, 40, 40),
                                      (167, 226, 40, 40),
                                      (283, 226, 40, 40),
                                      (400, 226, 40, 40),
                                      (516, 226, 40, 40))
                        for j in range(10):
                            ss = pyautogui.screenshot("{}/{}.png".format(folder_name, j + 1), region=summon_reg[j])
                            summoned = self.identify_summon(numpy.array(ss)[:, :, ::-1])
                            if summoned:
                                summoned_list.append(summoned)
                        summoned_folder.append([folder_name])
                        time.sleep(5)
                        pyautogui.click(self.summon_back_reg)
                        break
                    else:
                        pyautogui.click(self.summon_skip)
                self._wait_loading()
                pyautogui.mouseDown(90, 110)
                pyautogui.moveTo(90, 450, duration=1)
                pyautogui.mouseUp()
                time.sleep(2)
                pyautogui.mouseDown(90, 110)
                pyautogui.moveTo(90, 450, duration=1)
                pyautogui.mouseUp()
                time.sleep(3)
                pyautogui.click(self.summon_1_btn)
                time.sleep(2)

            pyautogui.moveTo(self.close_tab)
            time.sleep(1)
            pyautogui.click(self.close_tab)
            print(x)
            print(summoned_folder)
            print(summoned_list)


if __name__ == "__main__":
    bsreroll = BSReroll()
    bsreroll.acc_reroll(5, [3, 3, 3, 3], False)
