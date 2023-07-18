from field import Field


class Phone(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.value = value  # Проверка на корректность производится с помощью сеттера

    @Field.value.setter
    def value(self, new_value):
        if not self.validate_phone(new_value):
            raise ValueError("Неверный формат номера телефона")
        self._value = new_value

    @staticmethod
    def validate_phone(phone):
        # Здесь может быть ваша логика проверки корректности номера телефона
        # Для простоты давайте считать, что любая непустая строка считается корректным номером.
        return bool(phone)
