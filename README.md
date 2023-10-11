# EmbeddedSystem_hw2
嵌入式系統作業二 R11921008 羅恩至

## How to implement
1. 開啟Mbed Studio，點選左上角的file -> import program
![image](https://github.com/ehjhihlo/EmbeddedSystem_hw2/assets/75471051/953e4dd1-1421-483a-ac52-6634ef175a5c)

3. 在URL欄位貼上網址: https://github.com/ARMmbed/mbed-os-example-sockets，把Mbed socket的範例程式載下來  
![image](https://github.com/ehjhihlo/EmbeddedSystem_hw2/assets/75471051/25bfd7b1-d534-4d89-98be-7f879cf561a7)  
4. 重複上述步驟，貼上網址：https://os.mbed.com/teams/ST/code/DISCO_L475VG_IOT01-Sensors-BSP/，把STM32 sensor讀值的範例程式載下來  
5. 下載本repo的所有檔案
```
git clone https://github.com/ehjhihlo/EmbeddedSystem_hw2
```
5. 點開mbed-os-example-sockets這個program，進行以下修改：  
- 將本repo的main.cpp取代source/main.cpp  
- 將本repo的mbed_app.json取代原本mbed_app.json，或是點開原本的mbed_app.json，更改hostname的value為wifi網路的ip位址，"nsapi.default-wifi-ssid"填上連到的wifi名稱，"nsapi.default-wifi-password"填上wifi密碼  
- 把本repo中BSP_B-L475E-IOT01的資料夾檔案，複製到mbed-os-example-sockets裡面，將讀取sensor的.h檔放入program中  
- 點開repo中的mbed_os/targets/targets.json檔案，把"printf_lib"改成"std"  
6. 開啟repo的hw2_server.py，將HOST更改為連到的wifi之ip位址
7. 執行本repo的hw2_server.py檔案，開啟server
8. 在Mbed Studio執行main.cpp(Client)，即可將STM32感測器數值傳到server端

## 執行結果
在此專案中，選用了STM32感測器中的溫度、濕度、壓力以及x方向的加速度資訊，每10毫秒進行一次傳值，並在hw2_server.py中用matplotlib套件實作資料可視化。  
實作結果如下圖所示：
![image](https://github.com/ehjhihlo/EmbeddedSystem_hw2/assets/75471051/80865f61-24ea-462e-bd64-d0ae9e5389ab)
