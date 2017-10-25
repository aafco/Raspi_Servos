# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

pwm.set_pwm(0, 0, servoMax)
pwm.set_pwm(1, 0, servoMax)
pwm.set_pwm(2, 0, servoMax)
pwm.set_pwm(3, 0, servoMax)
pwm.set_pwm(4, 0, servoMax)
pwm.set_pwm(5, 0, servoMax)
pwm.set_pwm(6, 0, servoMax)
pwm.set_pwm(7, 0, servoMax)
pwm.set_pwm(8, 0, servoMin)
pwm.set_pwm(9, 0, servoMin)
pwm.set_pwm(10, 0, servoMin)
pwm.set_pwm(11, 0, servoMin)
pwm.set_pwm(12, 0, servoMin)
pwm.set_pwm(13, 0, servoMin)
pwm.set_pwm(14, 0, servoMin)
pwm.set_pwm(15, 0, servoMin)

while (True):
  for x in range(0, 8, 1):
    pwm.set_pwm(x, 0, servoMin)
    time.sleep(0.08)
  time.sleep(0.3)
  for x in range(8, 16, 1):
    pwm.set_pwm(x, 0, servoMax)
    time.sleep(0.08)
  time.sleep(0.3)

  for x in range(0, 8, 1):
      pwm.set_pwm(x, 0, servoMax)
      time.sleep(0.08)
  time.sleep(0.3)
  for x in range(8, 16, 1):
      pwm.set_pwm(x, 0, servoMin)
      time.sleep(0.08)
  time.sleep(0.3)

  for x in range(0, 8, 1):
    pwm.set_pwm(x, 0, servoMin)
    pwm.set_pwm(x+8, 0, servoMax)
    time.sleep(0.08)
  time.sleep(0.3)
  for x in range(7, -1, -1):
    pwm.set_pwm(x, 0, servoMax)
    pwm.set_pwm(x+8, 0, servoMin)
    time.sleep(0.08)
  time.sleep(0.3)
  for x in range(0, 3, 1):

pwm.set_pwm(0, 0, servoMin)
          pwm.set_pwm(1, 0, servoMin)
          pwm.set_pwm(2, 0, servoMin)
          pwm.set_pwm(3, 0, servoMin)
          pwm.set_pwm(4, 0, servoMin)
          pwm.set_pwm(5, 0, servoMin)
          pwm.set_pwm(6, 0, servoMin)
          pwm.set_pwm(7, 0, servoMin)
          pwm.set_pwm(8, 0, servoMax)
          pwm.set_pwm(9, 0, servoMax)
          pwm.set_pwm(10, 0, servoMax)
          pwm.set_pwm(11, 0, servoMax)
          pwm.set_pwm(12, 0, servoMax)
          pwm.set_pwm(13, 0, servoMax)
          pwm.set_pwm(14, 0, servoMax)
          pwm.set_pwm(15, 0, servoMax)
          time.sleep(0.3)
          pwm.set_pwm(0, 0, servoMax)
          pwm.set_pwm(1, 0, servoMax)
          pwm.set_pwm(2, 0, servoMax)
          pwm.set_pwm(3, 0, servoMax)
          pwm.set_pwm(4, 0, servoMax)
          pwm.set_pwm(5, 0, servoMax)
          pwm.set_pwm(6, 0, servoMax)
          pwm.set_pwm(7, 0, servoMax)
          pwm.set_pwm(8, 0, servoMin)
          pwm.set_pwm(9, 0, servoMin)
          pwm.set_pwm(10, 0, servoMin)
          pwm.set_pwm(11, 0, servoMin)
          pwm.set_pwm(12, 0, servoMin)
          pwm.set_pwm(13, 0, servoMin)
          pwm.set_pwm(14, 0, servoMin)
          pwm.set_pwm(15, 0, servoMin)
          time.sleep(0.3)

