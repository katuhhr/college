import sys
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow,QLabel,QPushButton,QDialog,QVBoxLayout,QScrollArea,QWidget,QLineEdit, QHBoxLayout)
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QFont, QPixmap, QRegExpValidator

   
#создаем правила игры
class RulesDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Правила игры")
        self.setFixedSize(400, 300)

        main_layout = QVBoxLayout(self)

        # Создаем область прокрутки
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet(
            """
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                border: none;
                background-color: rgba(255, 255, 255, 0.1);
                width: 10px;
                margin: 0px;
            }
            QScrollBar::handle:vertical {
                background-color: rgba(0, 0, 0, 0.3);
                border-radius: 5px;
                min-height: 20px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """
        )

        # Создаем контейнер для содержимого
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)

        # Текст правил
        rules_text = """
Правила игры "Быки и коровы":

1. Компьютер загадывает 4-значное число, все цифры которого различны (первая цифра не может быть нулём).

2. Игрок делает ходы, пытаясь отгадать число.

3. В ответ компьютер показывает:
   - "Быки" - цифры, которые стоят на правильных местах
   - "Коровы" - цифры, которые есть в числе, но стоят не на своих местах

4. Игра продолжается до тех пор, пока игрок не отгадает все число.

Пример

Первая попытка:
Загадано: 5234
Ответ: 5346
Результат: 1 бык (5) и 1 корова (3)

Втрая попытка:
Загадано: 5234
Ответ: 5284
Результат: 2 быка (5,4) и 0 коров

Третья попытка:
Загадано: 5234
Ответ: 5234
Результат: 4 быка - Победа!

Советы:
• Старайтесь использовать информацию из предыдущих ходов
• Используйте логику для исключения невозможных вариантов

Удачи в игре!
"""
        #редактируем текст
        rules_label = QLabel(rules_text)
        rules_label.setFont(QFont("Arial", 12))
        rules_label.setStyleSheet(
            """
            QLabel {
                color: black;
                background-color: white;
                padding: 15px;
                border-radius: 10px;
            }
        """
        )
        rules_label.setWordWrap(True)
        content_layout.addWidget(rules_label)
        scroll.setWidget(content_widget)
        main_layout.addWidget(scroll)

        self.setStyleSheet(
            """
            QDialog {
                background-color: rgb(255, 192, 203);
            }
        """
        )
        self.center_dialog()
        
    def center_dialog(self):
        """Центрирует окно на экране"""
        screen = QApplication.primaryScreen().geometry()
        window_geometry = self.geometry()
        x = (screen.width() - window_geometry.width()) // 2
        y = (screen.height() - window_geometry.height()) // 2
        self.move(x, y)

class WinDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Поздравляем!")
        self.setFixedSize(400, 200)
        self.setup_ui()
        self.center_dialog()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)

        congrats_text = QLabel("Поздравляем!\nВы отгадали число!")
        congrats_text.setAlignment(Qt.AlignCenter)
        congrats_text.setStyleSheet("""
            QLabel {
                color: black;
                font-size: 24px;
                font-weight: bold;
                font-family: Arial;
            }
        """)
        layout.addWidget(congrats_text)
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(20)

        # Создаем кнопки
        play_again_button = QPushButton("ИГРАТЬ СНОВА")
        exit_button = QPushButton("ВЫХОД")

        button_style = """
            QPushButton {
                background-color: rgba(255, 255, 255, 0.81);
                color: black;
                border: none;
                border-radius: 25px;
                font-size: 18px;
                font-weight: bold;
                padding: 8px 20px;
                min-width: 120px;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: rgb(255, 255, 255);
            }
        """
        play_again_button.setStyleSheet(button_style)
        exit_button.setStyleSheet(button_style)

        # Добавляем кнопки в горизонтальный layout
        buttons_layout.addWidget(play_again_button)
        buttons_layout.addWidget(exit_button)

        # Добавляем layout с кнопками в основной layout
        layout.addLayout(buttons_layout)

        # Стилизуем окно
        self.setStyleSheet("""
            QDialog {
                background-color: rgb(255, 192, 203);
            }
        """)

        # Подключаем обработчики кнопок
        play_again_button.clicked.connect(self.play_again)
        exit_button.clicked.connect(self.exit_game)

    def center_dialog(self):
        """Центрирует окно на экране"""
        screen = QApplication.primaryScreen().geometry()
        window_geometry = self.geometry()
        x = (screen.width() - window_geometry.width()) // 2
        y = (screen.height() - window_geometry.height()) // 2
        self.move(x, y)

    def play_again(self):
        """Обработчик кнопки 'Играть снова'"""
        self.done(1)  # Возвращаем 1 для обозначения "играть снова"

    def exit_game(self):
        """Обработчик кнопки 'Выход'"""
        self.done(0)  # Возвращаем 0 для обозначения "выход"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.secret_number = ""  # Здесь будем хранить загаданное число
        self.attempts = []  # Список для хранения попыток
        self.initUI()
        self.center_window()
        
    def initUI(self):
        self.setWindowTitle("Быки и коровы")
        self.setGeometry(100, 100, 800, 500)
        self.setFixedSize(800, 500)

        self.background = QLabel(self)
        self.background.setGeometry(0, 0, 800, 500)

        # первый фон
        self.start_background = QPixmap("C:/Users/User/Desktop/bulls_cows/background.jpg")
        self.game_background = QPixmap( "C:/Users/User/Desktop/bulls_cows/game_background.jpg") # второй фон для игры
    
        self.start_background = self.start_background.scaled(800, 500, Qt.AspectRatioMode.IgnoreAspectRatio)
        self.game_background = self.game_background.scaled(800, 500, Qt.AspectRatioMode.IgnoreAspectRatio)
        self.background.setPixmap(self.start_background)

        self.background.lower()

        # делаем надпись
        self.welcome_label = QLabel("Добро пожаловать в игру!", self)
        self.welcome_label.setFont(QFont("Arial", 20, QFont.Bold))
        self.welcome_label.setStyleSheet(
            """
            QLabel {
                color: white;
                background-color: rgba(0, 0, 0, 0.98);
                padding: 10px;
                border-radius: 15px;
            }
        """
        )
        # Устанавливаем размер надписи автоматически
        self.welcome_label.adjustSize()
        # размещение
        welcome_x = (800 - self.welcome_label.width()) // 2
        welcome_y = (500 - 100) // 2 - 60  
        self.welcome_label.move(welcome_x, welcome_y)

        # кнопка "НАЧАТЬ ИГРУ"
        self.start_button = QPushButton("НАЧАТЬ ИГРУ", self)
        button_width = 300
        button_height = 100
        self.start_button.setGeometry( (800 - button_width) // 2, (500 - button_height) // 2, button_width, button_height,)

        # кнопка "ПРАВИЛА"
        self.rules_button = QPushButton("ПРАВИЛА", self)
        rules_button_width = 150
        rules_button_height = 50
        self.rules_button.setGeometry(84, 500 - rules_button_height - 20, rules_button_width, rules_button_height,)
        # скрываем кнопку 
        self.rules_button.hide()

        # Создаем поле для ввода
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(90, 70, 200, 50)
        self.input_field.setStyleSheet(
            """
            QLineEdit {
                background-color: rgba(255, 255, 255, 0.9);
                border: none;
                border-radius: 20px;
                padding: 10px;
                font-size: 20px;
                font-weight: bold;
                color: black;
            }
            QLineEdit:focus {
                background-color: white;
                outline: none;
            }
        """
        )
        self.input_field.setAlignment(Qt.AlignCenter)
        self.input_field.setPlaceholderText("Введите число")

        # Устанавливаем валидатор для ввода только 4 цифр
        validator = QRegExpValidator(QRegExp("^[0-9]{0,4}$"))
        self.input_field.setValidator(validator)

        # максимальная длина
        #self.input_field.setMaxLength(4)

        # Подключаем обработчик изменения текста
        self.input_field.textChanged.connect(self.check_input)

        # скрываем поле 
        self.input_field.hide()

        # кнопка "ПРОВЕРИТЬ"
        self.check_button = QPushButton("ПРОВЕРИТЬ", self)
        self.check_button.setGeometry(300, 70, 147, 50)
       
        # скрываем 
        self.check_button.hide()
        self.check_button.clicked.connect(self.check_number)

        # стиль для кнопок
        button_style = """
            QPushButton {
                background-color: rgba(255, 255, 255, 0.81);
                color: black;
                border: none;
                border-radius: 20px;
                font-size: 24px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: rgb(255, 255, 255);
            }
        """

        # применяем стиль
        self.start_button.setStyleSheet(button_style)
        self.rules_button.setStyleSheet(
            button_style.replace("font-size: 24px", "font-size: 18px"))
        self.check_button.setStyleSheet( button_style.replace("font-size: 24px", "font-size: 18px"))

        # Подключаем обработчики нажатия кнопок
        self.start_button.clicked.connect(self.start_game)
        self.rules_button.clicked.connect(self.show_rules)

        # Добавляем область для отображения результатов
        self.result_label = QLabel(self)
        self.result_label.setGeometry(90, 130, 356, 250)
        self.result_label.setStyleSheet(
            """
            QLabel {
                color: black;
                background-color: rgb(255, 255, 255);
                border-radius: 20px;
                padding: 15px;
            }
        """
        )
        self.result_label.setAlignment(Qt.AlignTop)  # Выравнивание текста по верху
        self.result_label.hide()  # Скрываем при запуске

        # Создаем инструкцию для игры
        self.cow_instruction = QLabel("я есть, но я\n не на месте", self)
        self.cow_instruction.setGeometry(460, 120, 100, 80)
        self.cow_instruction.setStyleSheet(
            """
            QLabel {
                color: black;
                background-color: rgba(255, 255, 255, 0.9);
                border-radius: 10px;
                padding: 5px;
                font-size: 14px;
                font-weight: bold;
            }
        """
        )
        self.cow_instruction.setAlignment(Qt.AlignCenter)
        self.cow_instruction.hide()  # Скрываем при запуске
        
        self.bull_instruction = QLabel("я есть\nи я на месте", self)
        self.bull_instruction.setGeometry(460, 260, 100, 80)
        self.bull_instruction.setStyleSheet(
            """
            QLabel {
                color: black;
                background-color: rgba(255, 255, 255, 0.9);
                border-radius: 10px;
                padding: 5px;
                font-size: 14px;
                font-weight: bold;
            }
        """
        )
        self.bull_instruction.setAlignment(Qt.AlignCenter)
        self.bull_instruction.hide()  # Скрываем при запуске
        
    def generate_number(self):
        # Создаем список всех возможных цифр (кроме 0 для первой позиции)
        first_digit = list(range(1, 10))  # 1-9 для первой позиции
        other_digits = list(range(10))  # 0-9 для остальных позиций

        # Генерируем первую цифру
        first = random.choice(first_digit)
        remaining_digits = other_digits.copy()
        remaining_digits.remove(first)  # Удаляем использованную цифру

        # Генерируем оставшиеся 3 цифры
        rest = random.sample(remaining_digits, 3)

        # Собираем число
        self.secret_number = str(first) + "".join(map(str, rest))
        print(f"Загаданное число: {self.secret_number}")  # выводим для проверки

    def start_game(self):
        # Очищаем историю попыток
        self.attempts = []
        self.result_label.setText("")

        # Генерируем новое число
        self.generate_number()

        # Скрываем кнопку и приветственную надпись
        self.start_button.hide()
        self.welcome_label.hide()

        # Меняем фон
        self.background.setPixmap(self.game_background)

        # Показываем элементы игры
        self.rules_button.show()
        self.input_field.show()
        self.check_button.show()
        self.result_label.show()
        self.cow_instruction.show() 
        self.bull_instruction.show()

    def show_rules(self): # Создаем и показываем диалоговое окно с правилами
        dialog = RulesDialog(self)
        dialog.exec_()

    def check_input(self, text):
        if text.startswith("0"):
            self.input_field.setText(text[1:])
            return

        # Проверяем на уникальность цифр
        unique_digits = ""
        for digit in text:
            if digit not in unique_digits:
                unique_digits += digit

        if len(unique_digits) < len(text):
            self.input_field.setText(unique_digits)
            self.input_field.setCursorPosition(len(unique_digits))

    def check_number(self):
        # Получаем введенное число
        guess = self.input_field.text()
        if len(guess) != 4:
            return

        # Подсчитываем быков и коров
        bulls = 0
        cows = 0

        for i in range(4):
            if guess[i] == self.secret_number[i]:
                bulls += 1
            elif guess[i] in self.secret_number:
                cows += 1

        # Добавляем попытку в историю
        attempt = (f"Попытка {len(self.attempts) + 1}: {guess} - {bulls} быков, {cows} коров")
        self.attempts.append(attempt)

        history_text = "История попыток:\n\n" + "\n".join(self.attempts[-8:])
        self.result_label.setText(history_text)

        self.input_field.clear()

        # Проверяем на победу
        if bulls == 4:
            self.result_label.clear()
            win_dialog = WinDialog(self)
            result = win_dialog.exec()
            if result == 1:  
                self.start_game()
            else: 
                self.close()
                
    def center_window(self):
        """Центрирует окно на экране"""
        screen = QApplication.primaryScreen().geometry()
        window_geometry = self.geometry()
        x = (screen.width() - window_geometry.width()) // 2
        y = (screen.height() - window_geometry.height()) // 2
        self.move(x, y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
