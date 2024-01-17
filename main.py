#import tkinter as tk
import streamlit as st
# import serial
# #import time
#import serial.tools.list_ports
# Create the main window
#ports = serial.tools.list_ports.comports()
#for port, desc, hwid in sorted(ports):
#    print(f"{port}: {desc} [{hwid}]")
#print(st.__version__)

st.set_page_config(
     page_title="웹 연습",
     page_icon="./images/아존이2.jpg"
)

st.title('Web 시리얼 모니터!')
st.write("This is a simple text")
st.write("시작하자")
st.image("./images/아존이1.jpg")
st.image("./images/아존이_공간능력.jpg")

# ports = []
# for port in serial.tools.list_ports.comports():
#      ports.append(port.name)
# print(ports)


# window = tk.Tk()
# window.title("Hello world")
# window.geometry("300x300")

# hello = tk.Label(text="Hello world!")
# hello.pack()
# button = tk.Button(text="Click me!")
# button.pack()

# tk.mainloop()

# Replace 'COMx' with your specific serial port (e.g., '/dev/ttyUSB0' on Linux, 'COM3' on Windows)

# ser = serial.Serial('COM8', baudrate=9600, timeout=1)

# try:
#   while True:
#     # Reading data from the serial port
#     data = ser.readline().decode('utf-8').strip()

#     if data:
#       print(f"Received: {data}")

#     # Writing data to the serial port
#     ser.write("Hello, Arduino!\n".encode('utf-8'))

#     time.sleep(1)

# except KeyboardInterrupt:
#   ser.close()
#   print("Serial port closed.")

