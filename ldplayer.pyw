import time
import cv2
import numpy
import pyautogui
import pytesseract
import img_hash


def wait_loading(lag_check=True, position=1):
    loading_hash = "0000000000000000000000001000100010011110101111100111111101111111"
    if position == 1:
        loading_reg = (558, 354, 63, 17)
        screen_reg = (0, 36, 641, 354)
    elif position == 2:
        loading_reg = (1241, 354, 63, 17)
        screen_reg = (683, 36, 641, 354)
    else:
        loading_reg = (558, 354, 63, 17)
        screen_reg = (0, 36, 641, 354)
    loading = True
    last_screen_hash = None
    while loading:
        time.sleep(3)
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


def wait_match(position=1):
    back_hash = "1000000010000000011001000111111001111110001111100000000000000000"
    back_reg = (10 if position == 1 else 693, 41, 37, 20)
    while True:
        time.sleep(3.5)
        ss = pyautogui.screenshot(region=back_reg)
        ss = cv2.GaussianBlur(numpy.array(ss), (5, 5), 1)
        ss_hash = img_hash.calc_image_hash(ss)
        if img_hash.comp_hash(ss_hash, back_hash) < 2:
            break
        else:
            pyautogui.click(20 if position == 1 else 703, 200)


def mp_grind(times: int, room_place: int = 1):
    def get_room_number():
        room_code_reg = (291, 162, 63, 26)
        ss = pyautogui.screenshot(region=room_code_reg)
        ss.save("LDPlayer/room_code.png")
        ss = cv2.cvtColor(numpy.array(ss), cv2.COLOR_BGR2GRAY)
        # (7, 7) Sebenarnya Overkill, (5, 5) Sudah Cukup
        ss = cv2.GaussianBlur(ss, (7, 7), 1.0)
        ss_mean = numpy.mean(ss)
        _, threshold = cv2.threshold(ss, ss_mean, 255, cv2.THRESH_BINARY_INV)
        room_number = pytesseract.image_to_string(ss, config="--psm 6")
        length = str.find(room_number, "\n")
        return room_number[:length]

    room_code = None
    room1_pos = (480, 150)  # posisi room1 di emulator 1
    room2_pos = (480, 230)
    room3_pos = (480, 310)
    room4_pos = (480, 370)
    rsetup_pos = (470, 360)  # posisi tombol room setup emulator 1
    priv_pos = (265, 325)  # posisi tombol private emulator 1
    okbtn1_pos = (570, 360)  # posisi tombol ok emulator 1
    lobby_pos = (906, 152)  # posisi room mp emulator 2
    lock_pos = (1252, 94)  # posisi tombol kunci emulator 2
    input_pos = (950, 235)  # posisi textbox room code emulator 2
    okbtn2_pos = (1007, 319)  # posisi tombol ok emulator 2
    for i in range(times):
        time.sleep(1)
        if room_place == 1:
            pyautogui.click(room1_pos)
        elif room_place == 2:
            pyautogui.click(room2_pos)
        elif room_place == 3:
            pyautogui.click(room3_pos)
        elif room_place == 4:
            pyautogui.click(room4_pos)
        else:
            pyautogui.click(room1_pos)
        time.sleep(10)
        pyautogui.click(rsetup_pos)
        time.sleep(2)
        pyautogui.click(priv_pos)
        wait_loading(False)
        room_code = get_room_number()
        time.sleep(2)
        pyautogui.doubleClick(okbtn1_pos, interval=1)
        pyautogui.click(lock_pos)
        time.sleep(3)
        pyautogui.click(input_pos)
        time.sleep(2)
        if room_code is not None:
            pyautogui.write(room_code, interval=0.6)
        else:
            exit()
        time.sleep(4)
        pyautogui.doubleClick(okbtn2_pos, interval=1)
        time.sleep(2)
        wait_loading(True, 2)
        pyautogui.click(lobby_pos)
        wait_loading(True, 2)
        wait_loading(False)
        pyautogui.click(okbtn1_pos)
        time.sleep(70)
        wait_match()
        wait_match(2)


if __name__ == "__main__":
    mp_grind(20, 1)
