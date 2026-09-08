import pyautogui,time,random; [(pyautogui.moveTo(random.randint(0,pyautogui.size().width-1),random.randint(0,pyautogui.size().height-1)),time.sleep(random.uniform(3,8))) for _ in iter(int,1)]
