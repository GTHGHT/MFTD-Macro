import os
import random
import string
import time

import cv2
import numpy
import pyautogui
import pytesseract

import img_hash


def is_tutorial():
    next_btn_reg = (276, 325, 71, 29)
    next_btn_hash = "1111111100000000001000000011110000011100000111000000000000000000"

    ss = pyautogui.screenshot(region=next_btn_reg)
    ss = img_hash.calc_image_hash(numpy.array(ss))
    return True if img_hash.comp_hash(ss, next_btn_hash) < 2 else False


def acc_reroll(times: int, banner_to_summon: list, is_modded: bool):
    def del_config():
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
        del_pos11 = (315, 10)

        time.sleep(2)
        pyautogui.click(del_pos1)
        time.sleep(15)
        pyautogui.click(del_pos2)
        time.sleep(3)
        pyautogui.click(del_pos3)
        time.sleep(3)
        pyautogui.click(del_pos4)
        time.sleep(2)
        pyautogui.click(del_pos5)
        time.sleep(2)
        pyautogui.write("com.overlord", interval=0.5)
        time.sleep(2)
        pyautogui.click(del_pos6)
        time.sleep(2)
        pyautogui.click(del_pos7)
        time.sleep(2)
        pyautogui.mouseDown(del_pos8)
        time.sleep(2)
        pyautogui.mouseUp()
        time.sleep(2)
        pyautogui.click(del_pos9)
        time.sleep(2)
        pyautogui.click(del_pos10)
        time.sleep(2)
        pyautogui.moveTo(del_pos11)
        time.sleep(1)
        pyautogui.click()

    icon_pos = (243, 278)
    cls_mod_hash = "1111111111111111100000011000000110000001111111111111111111111111"
    black_hash = "0000000000000000000000000000000000000000000000000000000000000000"
    skip_ad = (18, 69)
    cls_ad = (596, 65)
    cls_mod_reg = (375, 239, 38, 20)
    tos_box1 = (173, 239)
    tos_box2 = (173, 257)
    ok_btn = (310, 310)
    skip_btn = (585, 60)
    input_nick_reg = (212, 224, 75, 21)
    input_nick_hash = "0000000000000000000001100000011100000111000001110000000000000000"
    next_btn_reg = (276, 325, 71, 29)
    confirm_btn_reg = (277, 326, 71, 26)
    confirm_btn_hash = "1111111100000000010010010111111001111110011111110000000000000000"
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
    summon_back_hash = "1111111100000000000000000011100000111100000110000000000000000000"
    close_game = (315, 10)

    for x in range(times):
        del_config()
        time.sleep(2)
        pyautogui.click(icon_pos)

        if is_modded:
            i = 0
            while i <= 15:
                time.sleep(2)
                ss = pyautogui.screenshot(region=cls_mod_reg)
                ss = img_hash.calc_image_hash(numpy.array(ss))
                if img_hash.comp_hash(ss, black_hash) < 2:
                    continue
                elif img_hash.comp_hash(ss, cls_mod_hash) < 2:
                    i += 1
                else:
                    time.sleep(7)
                    pyautogui.click(skip_ad)
                    time.sleep(1.5)
                    pyautogui.click(cls_ad)
            pyautogui.click(cls_mod_reg)
        else:
            while True:
                time.sleep(2)
                ss = pyautogui.screenshot(region=cls_mod_reg)
                ss = img_hash.calc_image_hash(numpy.array(ss))
                if img_hash.comp_hash(ss, black_hash) > 2:
                    pyautogui.click(ok_btn)
                    break

        time.sleep(3)
        pyautogui.click(ok_btn)

        wait_loading(lag_check=False)
        pyautogui.click(tos_box1)
        time.sleep(2)
        pyautogui.click(tos_box2)
        time.sleep(2)
        pyautogui.click(ok_btn)

        wait_loading()
        wait_loading(lag_check=False)

        pyautogui.click(ok_btn)
        time.sleep(6)
        pyautogui.click(skip_btn)
        time.sleep(3)
        pyautogui.click(ok_btn)
        time.sleep(10)
        pyautogui.click(ok_btn)

        while True:
            time.sleep(2)
            ss = pyautogui.screenshot(region=input_nick_reg)
            ss = img_hash.calc_image_hash(numpy.array(ss))
            if img_hash.comp_hash(ss, input_nick_hash) < 2:
                time.sleep(2)
                break

        pyautogui.click(input_nick_reg)
        time.sleep(3)
        pyautogui.write("Reroll", interval=0.6)
        pyautogui.doubleClick(ok_btn, interval=2)
        pyautogui.moveTo(5, 5)
        time.sleep(10)
        while True:
            time.sleep(2)
            if is_tutorial():
                time.sleep(2)
                pyautogui.click(next_btn_reg, interval=2, clicks=3)
                break

        i = 0
        while i < 2:
            pyautogui.moveTo(5, 5)
            time.sleep(3)
            ss = pyautogui.screenshot(region=confirm_btn_reg)
            ss = img_hash.calc_image_hash(numpy.array(ss))
            if img_hash.comp_hash(ss, confirm_btn_hash) < 2:
                pyautogui.click(confirm_btn_reg)
                time.sleep(7)
                if i == 1:
                    wait_loading()
                i += 1
            elif i == 1:
                time.sleep(2)
                break
            else:
                pyautogui.click(ok_btn)

        pyautogui.click(box_btn)
        wait_loading(lag_check=False)
        pyautogui.click(receive_btn)
        wait_loading(lag_check=False)
        pyautogui.click(ok_btn)
        wait_loading(lag_check=False)
        pyautogui.click(menu_btn)
        time.sleep(2)
        pyautogui.click(menu_summon_btn)
        wait_loading()

        for i in banner_to_summon:
            pyautogui.mouseDown(90, 300)
            pyautogui.moveTo(90, 190, duration=3)
            pyautogui.mouseUp()
            time.sleep(2)
            if i == 1:
                pyautogui.click(summon_1_btn)
            elif i == 2:
                pyautogui.click(summon_2_btn)
            elif i == 3:
                pyautogui.click(summon_3_btn)
            elif i == 4:
                pyautogui.click(summon_4_btn)
            elif i == 5:
                pyautogui.click(summon_5_btn)
            else:
                return False
            time.sleep(2)
            pyautogui.click(summon_banner)
            time.sleep(3)
            pyautogui.click(ok_btn)
            wait_loading(lag_check=False)
            pyautogui.doubleClick(skip_btn, interval=2)
            while True:
                time.sleep(2)
                ss = pyautogui.screenshot(region=summon_back_reg)
                ss = img_hash.calc_image_hash(numpy.array(ss))
                if is_tutorial():
                    time.sleep(2)
                    pyautogui.click(next_btn_reg, interval=2, clicks=3)
                    time.sleep(5)
                elif img_hash.comp_hash(ss, summon_back_hash) < 2:
                    folder_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
                    os.mkdir(folder_name)
                    pyautogui.screenshot("{}/ori.png".format(folder_name))
                    pyautogui.screenshot("{}/1.png".format(folder_name), region=(51, 118, 40, 40))
                    pyautogui.screenshot("{}/2.png".format(folder_name), region=(167, 118, 40, 40))
                    pyautogui.screenshot("{}/3.png".format(folder_name), region=(283, 118, 40, 40))
                    pyautogui.screenshot("{}/4.png".format(folder_name), region=(400, 118, 40, 40))
                    pyautogui.screenshot("{}/5.png".format(folder_name), region=(516, 118, 40, 40))
                    pyautogui.screenshot("{}/6.png".format(folder_name), region=(51, 226, 40, 40))
                    pyautogui.screenshot("{}/7.png".format(folder_name), region=(167, 226, 40, 40))
                    pyautogui.screenshot("{}/8.png".format(folder_name), region=(283, 226, 40, 40))
                    pyautogui.screenshot("{}/9.png".format(folder_name), region=(400, 226, 40, 40))
                    pyautogui.screenshot("{}/10.png".format(folder_name), region=(516, 226, 40, 40))
                    time.sleep(5)
                    pyautogui.click(summon_back_reg)
                    break
                else:
                    pyautogui.click(summon_skip)
            wait_loading()
            pyautogui.mouseDown(90, 110)
            pyautogui.moveTo(90, 450, duration=1)
            pyautogui.mouseUp()
            time.sleep(2)
            pyautogui.mouseDown(90, 110)
            pyautogui.moveTo(90, 450, duration=1)
            pyautogui.mouseUp()
            time.sleep(3)
            pyautogui.click(summon_1_btn)
            time.sleep(2)

        pyautogui.moveTo(close_game)
        time.sleep(1)
        pyautogui.click()


def wait_loading(emulator_position=0, lag_check=True):
    loading_hash = "0000000000000000000000001000000010111111111111111111111100000000"
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
        if img_hash.comp_hash(loading_ss, loading_hash) > 2:
            if lag_check:
                screen_ss = pyautogui.screenshot(region=screen_reg)
                screen_ss = img_hash.calc_image_hash(numpy.array(screen_ss)[:, :, ::-1])
                if last_screen_hash is not None:
                    if img_hash.comp_hash(last_screen_hash, screen_ss) > 0:
                        loading = False
                        time.sleep(4)
                last_screen_hash = screen_ss
            else:
                loading = False
                time.sleep(4)


def mp_grind():
    def get_room_number():
        left = 280
        top = 163
        width = 63
        height = 25
        ss = pyautogui.screenshot(region=(left, top, width, height))
        ss.save("Bluestacks/room_code.png")
        ss = cv2.cvtColor(numpy.array(ss), cv2.COLOR_BGR2GRAY)
        ss = cv2.GaussianBlur(ss, (5, 5), 1.0)
        ss_mean = numpy.mean(ss)
        _, threshold = cv2.threshold(ss, ss_mean, 255, cv2.THRESH_BINARY_INV)
        room_number = pytesseract.image_to_string(ss, config="--psm 6")
        length = str.find(room_number, "\n")
        return room_number[:length]

    room1_pos = (453, 157)  # posisi room yang dijalankan emulator 1
    rsetup1_pos = (451, 353)  # posisi tombol room setup emulator 1
    priv1_pos = (257, 320)  # posisi tombol private emulator 1
    okbtn1_pos = (551, 352)  # posisi tombol ok emulator 1
    room2_pos = (928, 155)  # posisi room mp emulator 2
    lock2_pos = (1232, 97)  # posisi tombol kunci emulator 2
    input2_pos = (950, 234)  # posisi textbox room code emulator 2
    okbtn2_pos = (995, 316)  # posisi tombol ok emulator 2

    time.sleep(1)
    pyautogui.click(room1_pos)
    time.sleep(8)
    pyautogui.click(rsetup1_pos)
    time.sleep(2)
    pyautogui.click(priv1_pos)
    wait_loading()
    room_code = get_room_number()
    time.sleep(2)
    pyautogui.doubleClick(okbtn1_pos, interval=1)
    pyautogui.click(lock2_pos)
    time.sleep(3)
    pyautogui.click(input2_pos)
    time.sleep(2)
    if len(room_code) == 4:
        pyautogui.write(room_code, interval=0.65)
    else:
        return
    pyautogui.doubleClick(okbtn2_pos, interval=1)
    time.sleep(1)
    wait_loading()
    pyautogui.click(room2_pos)
    time.sleep(9)
    pyautogui.click(okbtn1_pos)


if __name__ == "__main__":
    acc_reroll(10, [6, 3, 3], is_modded=False)
