class Smartphone:
    # 1. Конструктор (создает телефон и дает ему имя и заряд)
    def __init__(self, brand, battery):
        self.brand = brand      # Сохраняем марку в объект
        self.battery = battery  # Сохраняем заряд в объект

    # 2. Метод для проверки состояния
    def info(self):
        print(f"Смартфон: {self.brand}, Заряд: {self.battery}%")

    # 3. Метод "отправить сообщение" (тратит 5% заряда)
    def send_message(self, text):
        if self.battery >= 5:
            self.battery -= 5
            print(f"Отправлено сообщение: '{text}'. Осталось заряда: {self.battery}%")
        else:
            print("Слишком низкий заряд! Сообщение не отправлено.")

# --- ПРАКТИКА ---

# Создаем твой первый объект (экземпляр класса)
my_phone = Smartphone("iPhone 15", 100)

# Проверяем инфо
my_phone.info()

# Пробуем отправить сообщение
my_phone.send_message("Привет, я учу ООП!")