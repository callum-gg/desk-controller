import RPi.GPIO as GPIO

'''

2 = USB
24 = USB

14 = HDMI
15 = HDMI

17 = HDMI
18 = HDMI

3 = HDMI
4 = HDMI

23 = HDMI
27 = HDMI

'''

controllers = []

class Control():
    def __init__(self, nums, default=False):
        self.num = nums
        self.SetInput(default)
        for num in nums:
            GPIO.setup(num, GPIO.OUT)
        controllers.append(self)

    def SetInput(self, inp):
        self.active = inp
        for num in self.num:
            if self.active:
                GPIO.output(num, GPIO.HIGH)
            else:
                GPIO.output(num, GPIO.LOW)

    def ChangeInput(self):
        self.SetInput(not self.active)

def ChangeInput(inp):
    print(inp)
    for controller in controllers:
        controller.ChangeInput()

GPIO.setmode(GPIO.BOARD)

Control([2])
Control([24])
Control([14, 15])
Control([17, 18])
Control([3, 4])
Control([23, 27])