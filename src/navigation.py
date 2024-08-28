import RPi.GPIO as GPIO
import time

class Navigator:
    def __init__(self):
        self.left_motor_pin = 17
        self.right_motor_pin = 18

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.left_motor_pin, GPIO.OUT)
        GPIO.setup(self.right_motor_pin, GPIO.OUT)

        self.left_pwm = GPIO.PWM(self.left_motor_pin, 50)
        self.right_pwm = GPIO.PWM(self.right_motor_pin, 50)

        self.left_pwm.start(0)
        self.right_pwm.start(0)

    def navigate_to(self, obj):
        target_x = obj.get('x', 0)
        target_y = obj.get('y', 0)

        if target_y > 0:
            self.left_pwm.ChangeDutyCycle(100)
            self.right_pwm.ChangeDutyCycle(100)
            time.sleep(1)

        self.left_pwm.ChangeDutyCycle(0)
        self.right_pwm.ChangeDutyCycle(0)

    def cleanup(self):
        self.left_pwm.stop()
        self.right_pwm.stop()
        GPIO.cleanup()
