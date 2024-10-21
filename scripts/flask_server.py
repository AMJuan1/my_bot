from flask import Flask, request
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory

app = Flask(__name__)

# Connect to the local pigpio daemon
factory = PiGPIOFactory()

# Define servos with their respective pulse width ranges
servo1 = Servo(17, min_pulse_width=0.0004, max_pulse_width=0.0025, pin_factory=factory)
servo2 = Servo(18, min_pulse_width=0.0010, max_pulse_width=0.0018, pin_factory=factory)

# Set initial positions
initial_position1 = 0  # Change this value to your desired starting position for servo1
initial_position2 = 0  # Change this value to your desired starting position for servo2

servo1.value = initial_position1 / 100.0
servo2.value = initial_position2 / 100.0

@app.route('/move_servos', methods=['POST'])
def move_servos():
    data = request.json
    servo1_value = data.get('servo1', 0) / 100.0
    servo2_value = data.get('servo2', 0) / 100.0

    servo1.value = servo1_value
    servo2.value = servo2_value

    return 'Servos moved', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
