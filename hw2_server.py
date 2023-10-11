import socket 
import json
import numpy as np
import matplotlib.pyplot as plot
HOST = '192.168.0.104' # IP address
PORT = 8080 # Port to listen on (use ports > 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Starting server at: ", (HOST, PORT))
    conn, addr = s.accept()
    fig, ax = plot.subplots(2,2)
    with conn:
        print("Connected at", addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            print("data = ", data)
            print("Received from socket server:", data)
            if (data.count('{') != 1):
            # Incomplete data are received.
                choose = 0
                buffer_data = data.split('}')
                while buffer_data[choose][0] != '{':
                    choose += 1
                data = buffer_data[choose] + '}'
            obj = json.loads(data)
            print(obj)

            
            # fig.add_subplot(211)
            t = obj['s']
            ax[0][0].scatter(t, obj['TEMPERATURE'], c='blue')
            ax[0][0].set_xlabel("sample num")
            ax[0][0].set_ylabel("temperature (Celcius)")

            # fig.add_subplot(212)
            ax[0][1].scatter(t, obj['HUMIDITY'], c='blue')
            ax[0][1].set_xlabel("sample num")
            ax[0][1].set_ylabel("humidity (%)")

            # fig.add_subplot(221)
            ax[1][0].scatter(t, obj['PRESSURE'], c='blue')
            ax[1][0].set_xlabel("sample num")
            ax[1][0].set_ylabel("pressure (mBar)")

            # fig.add_subplot(222)
            t = obj['s']
            ax[1][1].scatter(t, obj['x'], c='blue') # x, y, z, gx, gy, gz
            ax[1][1].set_xlabel("sample num")
            ax[1][1].set_ylabel("X axis acceleration")
            
            fig.tight_layout()
            plot.pause(0.0001)
            # plot.show()