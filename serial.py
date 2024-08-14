import serial

# Configure the serial port
port = '/dev/ttyS0'  # Replace with your serial port
baudrate = 115200    # Replace with your baud rate
timeout = 1          # Timeout for read operations in seconds

try:
    # Open the serial port
    ser = serial.Serial(port, baudrate, timeout=timeout)

    # Write data to the serial port
    ser.write(b'Hello, Serial Port!\n')

    print("Write Complete.")
    # Read data from the serial port
    response = ser.readline().decode('utf-8').strip()
    print(f"Received: {response}")

finally:
    # Close the serial port
    ser.close()