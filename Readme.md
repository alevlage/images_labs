# Курс лабораторних робіт "Цифрова обробка зображень"

Курс призначений для ознайомлення студентів із засобами цифрової обробки зображень (OpenCV, Numpy, Matplotlib) мовою програмування Python.

## Послідовність виконання

1. Intro to Numpy
2. Intro to Matplotlib
3. Lab1
4. Lab2
5. Lab3
6. Lab4
7. Lab5
8. Lab6
9. Lab7
10. Sliders
11. Video

## Налаштування робочого середовища (Ubuntu)

### 1. Встановити бібліотеки та пакети у командній консолі:

- *sudo apt-get install python3-dev python3-pip python3-venv*
- *sudo -H pip3 install -U pip numpy*
- *sudo apt-get install libx11-dev libgtk-3-dev libboost-python-dev*
- *sudo apt-get install build-essential checkinstall cmake pkg-config yasm*
- *sudo apt-get install git*

### 2. Перейти в каталог Documents та створити віртуальне середовище myenv:

- *cd ~/Documents*
- *python3 -m venv myenv/*

### 3. Активувати віртуальне середовище myenv у командній консолі:

- *source myenv/bin/activate*

Активне віртуальне середовище відображається префіксом ***(myenv)*** на початку командної консолі.

### 4. Оновити pip - систему керування пакетами Python:

- *pip3 install --upgrade pip*

### 5. Встановити бібліотеку OpenCV версії 3.4.x:

- *pip install opencv-python==3.4.5.20*

Дана команда встановить всі необхідні пакети для коректної роботи OpenCV

### 6. Перевірити версію встановленої бібліотеки OpenCV:

Запустити інтерпретатор Python у командній консолі:
- *python*

Імпортувати бібліотеку OpenCV:
- *import cv2*

Перевірити версію бібліотеки:
- *cv2.__version__*

Вийти з інтерпретатору Python:
- *exit()*

### 7. Встановити бібліотеку Matplotlib:

- *pip install matplotlib*

### 8. Встановити Jupyter Notebook:

- *pip install jupyter*

### 9. Вийти з віртуального середовища:

- *deactivate*

### 10. Завантажити лабораторні роботи:

- *git clone https://github.com/mosolab/DIP.git*
