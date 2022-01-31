# Virtual Mouse 
 
Manipulação do mouse através de gestos com a mão <br><br>
<img src = "https://github.com/Italoko/Virtual-Mouse/blob/main/screenshot_example/example.gif?raw=true" />
<br>

<img src = "https://google.github.io/mediapipe/images/mobile/hand_landmarks.png" />
*Fonte <a href="https://google.github.io/mediapipe/">MediaPipe</a>

## Dependencias
* OpenCV - Para processamento das imagens <br>
```pip install opencv-python```
* MediaPipe - Para reconhecimento das mãos <br>
```pip install mediapipe```
* PyAutoGUI - Para manipulação do mouse <br>
```pip install PyAutoGUI```
* Numpy - Para manipulação de arrays <br>
```pip install numpy```

## Ações implementadas

* O mouse se movimenta baseado na "ponta" do dedo indicador ```KEY 8. [INDEX_FINGER_TIP]``` da mão reconhecida em proporção ao tamanho da tela (monitor). 

* O mouse clica com botão principal (1x) quando a "ponta" do dedo polegar ```KEY 4. [THUMB_TIP]``` se conecta com o um dos pontos ```KEY 10. [MIDDLE_FINGER_PIP]``` ou ```KEY 11. [MIDDLE_FINGER_DIP]```.
  * <img src = "https://github.com/Italoko/Virtual-Mouse/blob/main/screenshot_example/click_example.png?raw=true" style="width: 150px; height:150px;"/>

* O mouse permanece com botão principal pressionado quando a "ponta" do dedo indicador ```KEY 8. [INDEX_FINGER_TIP]``` se conecta com a "ponta" do dedo polegar ```KEY 4. [THUMB_TIP]``` .

  * <img src = "https://github.com/Italoko/Virtual-Mouse/blob/main/screenshot_example/pressed_example.png?raw=true" style="width: 150px; height:150px;"/>

## Como usar

Para usar em seu projeto siga os passos abaixo: 

1. Clone o repositório em sua maquina
 ```bash git clone https://github.com/Italoko/Virtual-Mouse ```

2. Execute o aquivo ```main.py``` python file.

## Conteúdo
* O módulo ```hands_detector.py``` contém funcionalidades baseadas no resultado do processamento e rastreamento das mãos e seus pontos chaves. 
  * Repositório do ```hands_detector.py``` : ```https://github.com/Italoko/Hands-Detector```
* O arquivo ```main.py``` contém o lógica principal para execução das ações baseados em algum gesto. ```hands_detector.py```.
   
