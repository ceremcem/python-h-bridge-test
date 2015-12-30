import RPi.GPIO as GPIO
import time

# Pin Definitons:
fw = 4 # Broadcom pin 18 (P1 pin 12)
bw = 17 # Broadcom pin 23 (P1 pin 16)

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(fw, GPIO.OUT) # LED pin set as output
GPIO.setup(bw, GPIO.OUT) # PWM pin set as output

dead_time = 0.05
forward_time = 0.08
backwards_time = forward_time

def stop():
    GPIO.output(bw, False)
    GPIO.output(fw, False)
    time.sleep(dead_time)
    

def forward():
    stop()
    GPIO.output(fw, True)
    time.sleep(forward_time)
    GPIO.output(fw, False)

def backwards():
    stop()
    GPIO.output(bw, True)
    time.sleep(backwards_time)
    GPIO.output(bw, False)

period = 0.05

try: 
    coins_given = 0 
    while True: 
        forward()
        backwards()
        coins_given += 1
        print "total coins given: ", coins_given 
        time.sleep(period)
except: 
    print "Exception, stopping!"
    stop()
    GPIO.cleanup()

